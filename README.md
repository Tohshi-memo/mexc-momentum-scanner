# MEXC Momentum Scanner

MEXC USDT-M 先物の急騰アルトコインを検出し、テクニカル・ファンダ・統計フィルターで
フィルタリングして、**ショート**エントリーを提案／執行する自動売買システム。

## 概要

- **スキャン**: BTC レジーム判定 + 1h ≥ +5% の急騰銘柄抽出 (`core/scanner.py`)
- **テクニカル分析**: RSI / BB / ATR / 出来高トレンド / 4h RSI (`core/analyzer.py`)
- **ファンダ分析**: 無料 RSS + Reddit で材料の有無を判定 (`core/fundamental.py`)
- **損失低減フィルター**: Cooldown / Circuit Breaker / ATR ベース SL
- **Live フィルター (Tier S/A/B)**: シャドウ集計で期待値プラスが確認された
  組み合わせのみを実トレードに昇格 (`core/live_filter.py`)
- **Live 戦略**: 方向・エントリー方式・サイズ・トレーリングを統合 (`core/live_strategy.py`)
- **仮想ポートフォリオ**: $100 ベースで戦略パフォーマンスを追跡 (`core/live_portfolio.py`)
- **シャドウトレード**: STRICT 通過／外れに関わらず全候補を追跡し、フィルター
  粒度を再評価するための統計を蓄積 (`core/experiment.py`)
- **通知**: Discord Webhook でシグナル検知・TP/SL ヒット・期限切れを通知
- **実行環境**: GitHub Actions でスケジュール実行、`data/*.json` をコミットして永続化

## クイックスタート

```bash
git clone <this-repo>
cd mexc-momentum-scanner
pip install -r requirements.txt
cp .env.example .env
# .env を編集 (MEXC_API_KEY / MEXC_SECRET_KEY など)
python main.py
```

## 実トレード ⇄ バーチャルトレードの切り替え

`.env` の `DRY_RUN` 1 行で切り替わります。

```ini
# バーチャル (シミュレーション) — デフォルト
DRY_RUN=true

# 実トレード (MEXC に実注文)
DRY_RUN=false
```

### 動作の違い

| 項目 | `DRY_RUN=true` | `DRY_RUN=false` |
|---|---|---|
| 注文 | ログ出力のみ | MEXC USDT-M 先物に実発注 |
| SL/TP | 仮想追跡 (価格到達で outcome 判定) | 発注時に取引所へ attach |
| バーチャル残高 (`data/live_portfolio.json`) | 更新される | 更新される |
| 実績統計 (`data/stats.json`) | 更新される | 更新される |
| シャドウトレード (`data/experiments.json`) | 更新される | 更新される |
| API 権限 | Read-only で可 | **Futures Trade 権限必須** |

### `DRY_RUN=false` に切り替える前のチェックリスト

1. **API キー権限**
   - MEXC の API 管理画面で `Futures Trade` をオンにする
   - IP 制限を設定している場合は実行環境の IP を許可
2. **残高確認**
   ```bash
   python tools/show_balance.py
   # または GitHub Actions の "Show MEXC Balance" を workflow_dispatch
   ```
3. **リスクパラメーター確認** (`.env`)
   ```ini
   LIVE_BASE_RISK_PCT=0.5        # 1 トレードで失う可能性がある残高比率
   LIVE_MAX_RISK_PCT=1.5         # クリップ上限
   LIVE_MAX_LEVERAGE=3.0         # 名目額の上限 (× 残高)
   LIVE_MIN_BALANCE_USDT=5.0     # 残高がこれを下回ると発注停止
   LIVE_MAX_OPEN_POSITIONS=3     # 同時保有上限
   ```
4. **サーキットブレーカー状態** (詳細は後述の「サーキットブレーカーの挙動」)
   - 直近 `CIRCUIT_BREAKER_LOOKBACK_HOURS` 時間内に closed した記録のうち、
     直近 `CIRCUIT_BREAKER_WINDOW` 件中 `CIRCUIT_BREAKER_LOSSES` 件以上 SL なら当サイクル全スキップ

### 実トレード時の安全装置 (`core/executor.py` `LiveExecutor`)

発注ごとに以下のガードが順番にチェックされ、1 つでも抵触すると発注されません。

1. `fundamental == AVOID` → スキップ
2. 残高 `< LIVE_MIN_BALANCE_USDT` → スキップ
3. 同シンボルに既存ポジション → スキップ
4. 開いているポジション数 ≥ `LIVE_MAX_OPEN_POSITIONS` → スキップ
5. SL/TP が不正 (SHORT なら SL は entry より上 / TP は下) → エラー
6. 最小ロットまたは最小名目額を下回る → スキップ

通過した場合のみ `market sell` + `stopLossPrice` / `takeProfitPrice` を同一注文に
attach して発行します。**SL/TP が必ずセットで出る**のが設計上の保証です。

### サーキットブレーカーの挙動

連敗時の資金防衛として、直近の SL 集中を検知すると当サイクルのエントリーを
全スキップします。GitHub Actions のログに以下が表示されます:

```
⊘  CIRCUIT BREAKER ACTIVE
Recent loss streak exceeded threshold.
All new entries are skipped this cycle.
```

#### 発動条件 (AND)

1. 直近 `CIRCUIT_BREAKER_LOOKBACK_HOURS` 時間内に closed した記録のみ対象
2. 上記 pool が `CIRCUIT_BREAKER_WINDOW` 件以上ある
3. pool 末尾 `CIRCUIT_BREAKER_WINDOW` 件のうち SL_HIT が
   `CIRCUIT_BREAKER_LOSSES` 件以上

デフォルト: **直近 48h 以内の 10 件中 5 件以上が SL なら発動**

#### 自動解除

新規トレードが途絶えて lookback 時間が経過すれば、pool が縮小・空になり
**自動で解除** されます（手動リセットは不要）。

| 状態 | 挙動 |
|---|---|
| lookback 内の記録 < WINDOW | 発動しない（pool 不足） |
| lookback 内で SL < LOSSES | 発動しない |
| lookback 内で SL ≥ LOSSES | 発動（当サイクル全スキップ） |
| 24h 以上新規トレードなし | 古い連敗は対象外 → 解除 |

#### 手動リセット (緊急時)

`CIRCUIT_BREAKER_LOOKBACK_HOURS` で解決しない場合の最終手段として、
`StatsManager.reset_circuit_breaker()` を呼ぶと `data/stats_meta.json` に
`cb_reset_at` を書き込み、**それ以降の記録のみ**で判定するようになります。

#### `data/live_portfolio.json` との関係

**無関係です。** サーキットブレーカーは `data/stats.json`（tracker の outcome 結果）
のみで判定し、仮想ポートフォリオの残高・履歴は参照しません。

### 残高が少ない場合の注意

残高 $28 でデフォルト設定 (`LIVE_BASE_RISK_PCT=0.5`, `SL≈2%`) の場合:

```
risk_usdt = 28 × 0.5% = $0.14
notional  = 0.14 / 0.02 = $7
```

MEXC の最小名目額 (通常 $5 程度) を下回る銘柄も多く、`skipped_below_min_cost` で
多くの候補がスキップされます。少額テストの場合は `LIVE_BASE_RISK_PCT` を
2〜3% に引き上げるか、DRY_RUN でデータ蓄積を継続してください。

## トレード戦略の更新

戦略は**静的に保存**されており、AI エージェント (Claude) との手動相談で
`.env` のパラメーターや `core/live_filter.py` / `core/live_strategy.py` を
更新して反映します。サイクル毎に AI に判断を仰ぐ設計ではありません。

戦略チューニング時に参照する主な資料:

- `data/experiment_report.md` — シャドウトレード統計、Tier 別期待値
- `data/stats.json` — 実際に追跡した TrackedSymbol の outcome
- `data/live_portfolio.json` — $100 ベース仮想残高の推移

## 主要ディレクトリ

```
mexc-momentum-scanner/
├── main.py                    # エントリーポイント
├── core/
│   ├── scanner.py             # 急騰銘柄スキャン
│   ├── analyzer.py            # テクニカル分析
│   ├── fundamental.py         # ニュース・Reddit 材料判定
│   ├── executor.py            # DryRun / Live 注文執行
│   ├── live_filter.py         # Tier S/A/B ゲート (実トレード用)
│   ├── live_strategy.py       # 方向・エントリー・サイズ決定
│   ├── live_portfolio.py      # $100 ベース仮想残高
│   ├── tracker.py             # TP/SL 追跡
│   ├── stats.py               # 損益集計・CB 判定
│   └── experiment.py          # シャドウトレード
├── tools/
│   ├── analyze_experiments.py # experiment_report.md 生成
│   ├── virtual_portfolio.py   # バーチャル残高レポート
│   └── show_balance.py        # MEXC 先物残高表示
├── utils/
│   ├── mexc_client.py         # ccxt ラッパー
│   ├── display.py             # rich コンソール出力
│   └── notifier.py            # Discord Webhook
└── .github/workflows/
    ├── scanner.yml            # メインスキャナー (スケジュール)
    └── show_balance.yml       # 残高確認 (手動)
```

## ライセンス

Private / 自己責任でご利用ください。実トレードは元本を失う可能性があります。
