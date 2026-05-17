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
- **実行環境**: 外部 cron から GitHub Actions を起動し、`data/*.json` をコミットして永続化

## クイックスタート

```bash
git clone <this-repo>
cd mexc-momentum-scanner
pip install -r requirements.txt
cp .env.example .env
# .env を編集 (MEXC_API_KEY / MEXC_SECRET_KEY など)
python main.py
```

## GitHub Actions の運用

このリポジトリでは、データ収集用と本番発注用の Action を分けています。
通常のデータ収集では実注文されません。

| Action | 用途 | 注文 | データ保存 |
|---|---|---|---|
| `MEXC Momentum Scanner` | データ収集・DryRun・シグナル追跡 | しない (`DRY_RUN=true` 固定) | `data/` を commit/push |
| `MEXC Momentum Analysis` | 重い分析レポート生成 | しない | `analysis-results` の `reports/` を更新 |
| `MEXC Live Trader` | MEXC 本番注文 | 条件を満たすと実注文 | `data/` は push しない |
| `Show MEXC Balance` | 残高確認 | しない | 保存なし |

`MEXC Momentum Scanner` は外部 cron から5分ごとに呼び出す想定です。GitHub Actions 内蔵の
`schedule` は使わず、二重起動を避けています。

## MEXC 本番トレードにする方法

本番注文は `MEXC Live Trader` Action からだけ行います。`MEXC Momentum Scanner` は
DryRun 固定なので、そこから本番注文に切り替えることはできません。

### 1. MEXC API キーを用意する

MEXC の API 管理画面で、USDT-M 先物の取引に使える API キーを作成します。

- DryRun だけなら Read-only で十分です。
- 本番注文には `Futures Trade` 権限が必要です。
- IP 制限を使う場合は、GitHub Actions の実行元 IP の扱いに注意してください。固定IPが必要なら GitHub Actions より VPS 運用の方が向いています。

### 2. GitHub Secrets を設定する

GitHub の repository settings で以下の secrets を登録します。

```text
MEXC_API_KEY
MEXC_SECRET_KEY
DISCORD_WEBHOOK_URL
```

`DISCORD_WEBHOOK_URL` は任意ですが、本番注文では発注・スキップ・失敗理由を確認するため設定推奨です。

### 3. GitHub Environment を作る

`MEXC Live Trader` は `environment: live-trading` を使います。
GitHub の `Settings` → `Environments` で `live-trading` を作成してください。

推奨設定:

- `Required reviewers` を有効にする
- 自分の承認なしに本番Actionが進まないようにする
- 本番用のAPIキーを environment secrets に分けて置く運用も可

### 4. 残高を確認する

本番前に `Show MEXC Balance` Action を手動実行します。

ローカルで確認する場合:

```bash
python tools/show_balance.py
```

### 5. 最初の本番注文を手動で実行する

GitHub Actions で `MEXC Live Trader` を選び、`Run workflow` から実行します。

入力値:

```text
live_trading_enabled = true
confirmation = LIVE
```

この2つが揃わない場合、Action は失敗して実注文しません。さらにコード側でも
`LIVE_TRADING_ENABLED=true` と `LIVE_TRADING_CONFIRMATION=LIVE` がない限り
`LiveExecutor` は起動しません。

### 6. 初期の本番リスク設定

`MEXC Live Trader` の初期設定は、小さく試す前提です。

```yaml
LIVE_MAX_ORDERS_PER_RUN: '1'
LIVE_MAX_OPEN_POSITIONS: '1'
LIVE_BASE_RISK_PCT: '0.25'
LIVE_MAX_RISK_PCT: '0.25'
LIVE_MAX_LEVERAGE: '2.0'
LIVE_MIN_BALANCE_USDT: '5.0'
```

つまり、1回のActionで最大1注文、同時保有も最大1ポジションです。
安定確認後に増やす場合も、まずは `LIVE_BASE_RISK_PCT` と `LIVE_MAX_OPEN_POSITIONS` を小さく保ってください。

### 7. SL/TP 付き発注の仕組み

本番注文は `core/executor.py` の `LiveExecutor` が担当します。
通過した場合のみ `market sell` に `stopLossPrice` と `takeProfitPrice` を付けて発注します。

発注前に以下のガードを通ります。

1. `fundamental == AVOID` ならスキップ
2. 残高 `< LIVE_MIN_BALANCE_USDT` ならスキップ
3. 同じシンボルに既存ポジションがあればスキップ
4. 開いているポジション数が `LIVE_MAX_OPEN_POSITIONS` 以上ならスキップ
5. SL/TP が不正ならエラー
6. 最小ロットまたは最小名目額を下回るならスキップ

通過した場合だけ、SL/TP を付けた注文をMEXCへ送ります。

## DryRun と本番の違い

| 項目 | DryRun (`MEXC Momentum Scanner`) | 本番 (`MEXC Live Trader`) |
|---|---|---|
| 実注文 | しない | 条件を満たすと行う |
| 実行頻度 | 外部 cron で5分ごと | 最初は手動推奨 |
| `DRY_RUN` | `true` 固定 | `false` 固定 |
| 追加ロック | 不要 | `live_trading_enabled=true` + `confirmation=LIVE` |
| `data/` push | する | しない |
| SL/TP | 仮想追跡 | 注文時にMEXCへ送信 |

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

### シャドウトレードのアーカイブ (肥大化対策)

`data/experiments.json` は日々 200 件以上の closed 記録が追加されるため、
放置すると単ファイルが GitHub 上限 (100MB) に接近します。以下の仕組みで
**分析精度を落とさずに** ホットファイルを軽く保ちます。

```
data/
├── experiments.json              # ホット (直近 EXPERIMENT_HOT_MAX 件)
└── archive/
    ├── experiments_2026-04.json.gz   # 月次 gzip アーカイブ
    ├── experiments_2026-05.json.gz
    └── ...
```

#### ローテーションの動作

- `core/experiment.py` がサイクル毎に `_enforce_history_cap()` を実行
- ホット件数 > `EXPERIMENT_HOT_MAX` (デフォルト **500**) を超えたら、
  古い方から `closed_at` の YYYY-MM で分類し `data/archive/` に gzip で追記
- 分析ツール `tools/analyze_experiments.py` は **ホット + 全 archive を結合**
  して読み込むため、全期間統計は常に計算可能

#### 容量比較 (参考値)

| 形式 | 1120 件 | 10000 件相当 |
|---|---|---|
| JSON (現状) | 13 MB | ~115 MB |
| gzip (圧縮) | ~4 MB | ~35 MB |

gzip により **約 70% 削減**。月次で分割することで個別ファイルも
50MB 警告ライン以下に収まります。

#### archive 無しで分析したい場合

```bash
python tools/analyze_experiments.py --no-archives
```

ホット `experiments.json` のみで report を生成します (直近分析用)。

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
    ├── scanner.yml            # DryRun専用スキャナー (外部cronから起動)
    ├── analysis.yml           # 重い分析レポート生成
    ├── live-trade.yml         # MEXC本番注文用 (手動・二重ロック)
    └── show_balance.yml       # 残高確認 (手動)
```

## ライセンス

Private / 自己責任でご利用ください。実トレードは元本を失う可能性があります。
