# MEXC Momentum Scanner

MEXC USDT-M 先物の急騰アルトコインを検出し、テクニカル・ファンダ・統計フィルターで
フィルタリングして、**ショート**エントリーを提案／執行する自動売買システム。

## 概要

- **スキャン**: BTC レジーム判定 + 1h ≥ +5% の急騰銘柄抽出 (`core/scanner.py`)
- **テクニカル分析**: RSI / BB / ATR / 出来高トレンド / 4h RSI (`core/analyzer.py`)
- **ファンダ分析**: 無料 RSS + Reddit で材料の有無を判定 (`core/fundamental.py`)
- **損失低減フィルター**: Cooldown / Circuit Breaker / ATR ベース SL
- **Live フィルター**: シャドウ結果を時系列分割して再現した「日足RED＋1時間陽線
  3～4本」のMARKETショートだけを承認候補にする (`core/live_filter.py`)
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
# .env を編集（ローカル/DryRun用のread-only MEXC_API_KEY / MEXC_SECRET_KEYなど）
python main.py
```

## GitHub Actions の運用

このリポジトリでは、データ収集用と本番発注用の Action を分けています。
通常のデータ収集では実注文されません。

| Action | 用途 | 注文 | データ保存 |
|---|---|---|---|
| `MEXC Momentum Scanner` | データ収集・DryRun・シグナル追跡 | しない (`DRY_RUN=true` 固定) | `data/` を commit/push |
| `MEXC Momentum Analysis` | 重い分析レポート生成 | しない | `analysis-results` の `reports/` を更新 |
| 別リポジトリ `mexc-live-trader` | MEXC 本番注文 | 全安全ゲート通過時のみ実注文 | さくらへ監査イベントを保存 |

`MEXC Momentum Scanner` は外部 cron から5分ごとに呼び出す想定です。GitHub Actions 内蔵の
`schedule` は使わず、二重起動を避けています。

## MEXC 本番トレードにする方法

本番注文は非公開の `mexc-live-trader` リポジトリからだけ行います。
`MEXC Momentum Scanner` はDryRun固定で、署名付き候補をさくらへ保存します。

### 1. MEXC API キーを用意する

MEXC の API 管理画面で、用途を分離した2組の API キーを作成します。

- scanner / DryRun用は **Read-only** とし、`MEXC_API_KEY` / `MEXC_SECRET_KEY` に使います。
- 本番専用キーだけに `Futures Trade` 権限を与え、scanner用キーと使い回しません。
- IP 制限を使う場合は、GitHub Actions の実行元 IP の扱いに注意してください。固定IPが必要なら GitHub Actions より VPS 運用の方が向いています。

### 2. GitHub Secrets を設定する

GitHub の repository settings には、scanner用のread-only secretsを登録します。

```text
MEXC_API_KEY       # scanner専用・read-only
MEXC_SECRET_KEY    # scanner専用・read-only
DISCORD_WEBHOOK_URL
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
```

`DISCORD_WEBHOOK_URL` は任意ですが、本番注文では発注・スキップ・失敗理由を確認するため設定推奨です。
`MEXC_API_KEY` / `MEXC_SECRET_KEY` に本番取引権限を与えないでください。

`TELEGRAM_BOT_TOKEN` と `TELEGRAM_CHAT_ID` を設定すると、確認済みの
実弾約定、実弾注文エラー／緊急クローズ、ライブWorkflow失敗を通知します。
`MEXC Live API Health` は毎日09:10 JSTに1回だけ認証済みread endpointを確認し、
API異常と復旧の状態変化時だけTelegramへ通知します。MEXC画面に失効日時が
表示されるキーは、GitHub repository variable `MEXC_LIVE_API_EXPIRES_AT` に
タイムゾーン付きISO-8601形式（例: `2026-10-28T20:46:00+09:00`）で登録すると、
5日前・1日前・期限到達時だけ追加通知します。期限なしのキーは未設定にします。

### 3. GitHub Environment を作る

`MEXC Live Trader` は `environment: live-trading` を使います。
GitHub の `Settings` → `Environments` で `live-trading` を作成してください。

このEnvironmentのsecretsに、本番専用キーを次の名前で登録します。

```text
MEXC_LIVE_API_KEY
MEXC_LIVE_SECRET_KEY
```

本番キーはrepository secretsやローカルの `.env` には置かず、`live-trading`
Environment内だけに保存します。workflowは本番stepの実行中だけ、これらをコードが読む
`MEXC_API_KEY` / `MEXC_SECRET_KEY` へ割り当てます。

必須の保護設定:

- `Required reviewers` を有効にする
- workflow の入力確認とは別に、Environment の手動承認なしで本番Actionが進まないようにする
- deployment branch ruleでdefault branchだけを許可する

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

本番 workflow は、これらの二重ロックに加えて次も強制します。

- repository の **default branch** からの dispatch だけを許可
- dispatch 時点の `${{ github.sha }}` を指定して、不変の commit SHA を checkout
- `live-trading` Environment の承認を workflow 入力とは別に要求
- unit test と read-only の MEXC preflight が成功するまで `main.py` を実行しない

実注文を許可する最終操作は、毎回の `workflow_dispatch` と
`live-trading` Environment 承認です。設定だけで定期的に実注文へ移行する仕組みではありません。

### 6. 初期の本番リスク設定

`MEXC Live Trader` の初期設定は、小さく試す前提です。

```yaml
LIVE_MAX_ORDERS_PER_RUN: '1'
LIVE_MAX_NEW_ENTRIES_PER_UTC_DAY: '1'
LIVE_MAX_OPEN_POSITIONS: '1'
LIVE_BASE_RISK_PCT: '0.10'
LIVE_MAX_RISK_PCT: '0.10'
LIVE_MAX_LEVERAGE: '3.0'
LIVE_MIN_BALANCE_USDT: '5.0'
LIVE_MARGIN_MODE: 'isolated'
LIVE_POSITION_MODE: 'hedged'
```

1ポジションの計画リスクは口座残高の最大 **0.10%**、1回のActionで最大1注文、
同時保有も最大1ポジションです。証拠金は isolated、ポジションモードは hedged、
レバレッジ上限は3倍です。数量は口座リスク0.10%とSL幅から逆算するため、レバレッジを
上げても計画損失上限は増えません。検証履歴を増やす目的でリスク上限や
ポジション数を緩めないでください。

### 7. 本番判定と発注のフェイルクローズ設計

本番注文は `core/executor.py` の `LiveExecutor` が担当します。
不足・不明・不整合は許可とみなさず、すべてREJECTまたは実行エラーにします。

1. **read-only preflight**
   `tools/live_preflight.py` が、ccxt/MEXC APIの必要メソッド、認証、有限なUSDT残高、
   hedgedモード、既存ポジション数を照合します。この段階では注文の作成・変更・取消を行いません。
2. **フィルター一致の因果実績ゲート**
   `Mexc-trading-BOT` がシグナルと結果を結合し、日足RED＋1時間陽線3～4本、
   Funding≥-0.05%のMARKETショートだけを評価します。同一銘柄・同一足の重複を除外し、
   UTC1日1件・同銘柄48時間・同時保有1件を適用した履歴で、手数料0.16%・
   スリッページ0.20%・Funding予備0.15%控除後の全期間、直近20件、直近50件が
   +0.20%以上、30日以上に分散し、95%信頼下限が0%以上の場合だけ推薦します。
3. **最新L2の執行可能性ゲート**
   発注直前にorder bookを再取得し、データ鮮度10秒以内、シグナル価格からの乖離0.50%以内、
   spread 0.10%以内、想定slippage 0.10%以内、必要数量に対するdepth 1.0倍以上を確認します。
4. **`externalOid` による exactly-once**
   account・symbol・direction・entry style・signal candle から安定した注文intentを作り、
   決定的な `externalOid` を付与します。発注前と応答不明時はread-only APIで取引所を照合し、
   mutatingな注文作成は自動再試行しません。同じintentが見つかれば新規注文を出さず再照合します。
   さらにUTC当日の全symbol履歴を照合し、新規entryを1日1件までに制限します。
5. **約定・保護・実リスク検証**
   entryの約定と、全数量を覆うTP/SLを取引所側で確認します。実約定価格・SL・数量から
   actual riskを再計算し、計画値の1.05倍を超えないことまで確認して初めて成功扱いにします。
   いずれかが確認できずポジションが存在する場合は、`reduceOnly` の成行注文で緊急クローズし、
   その実行も取引所へread-only照合します。

スキャナー自身は推薦の可否を決めません。保存済みの全履歴から毎日再計算される
署名付き推薦と、スキャナーが今検出した同一戦略IDの候補が両方そろった場合だけ、
別リポジトリの本番処理が発注可否を判断します。

確認済みの実行結果はrunner-localの `logs/live-executions.jsonl` に追記され、
workflow終了時に `logs/` artifactとして14日保存されます。このledgerは監査用スナップショットで、
runner間の永続状態や重複防止の根拠ではありません。注文・約定・ポジション・保護注文の
source of truthは常にMEXCです。

## DryRun と本番の違い

| 項目 | DryRun (`MEXC Momentum Scanner`) | 本番 (`MEXC Live Trader`) |
|---|---|---|
| 実注文 | しない | 条件を満たすと行う |
| 実行頻度 | 外部 cron で5分ごと | 最初は手動推奨 |
| `DRY_RUN` | `true` 固定 | `false` 固定 |
| 追加ロック | 不要 | `true` + `LIVE`、default branch、不変SHA、Environment承認、preflight |
| `data/` push | する | しない |
| SL/TP | 仮想追跡 | MEXCで約定・保護を再照合。失敗時は緊急reduceOnly close |

### サーキットブレーカーの挙動

連敗時の資金防衛として、直近の SL 集中を検知すると当サイクルのエントリーを
全スキップします。GitHub Actions のログに以下が表示されます:

```
⊘  CIRCUIT BREAKER ACTIVE
Recent loss streak exceeded threshold.
All new entries are skipped this cycle.
```

#### 発動条件

1. 直近 `CIRCUIT_BREAKER_LOOKBACK_HOURS` 時間内に closed した記録のみ対象
2. 上記 pool が `CIRCUIT_BREAKER_MIN_SAMPLES` 件以上ある
3. 各記録から `CIRCUIT_BREAKER_COST_PCT` を控除したネット損益を計算
4. 次のどちらかなら新規エントリーを停止
   - `CIRCUIT_BREAKER_WINDOW` 件が揃い、SL_HIT が
     `CIRCUIT_BREAKER_LOSSES` 件以上、かつネット損益がマイナス
   - 最低サンプル数が揃い、ネット損益が
     `CIRCUIT_BREAKER_SEVERE_NET_LOSS_PCT` 以下

`CIRCUIT_BREAKER_WARN_LOSSES` 件以上は警戒ログだけを出し、停止はしません。

デフォルト: **直近48hの10件で5敗は警戒、7敗以上かつネットマイナス、
またはネット合計−8%以下で発動**（1件あたり想定コスト0.51%）。

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

残高 $28 で本番設定 (`LIVE_BASE_RISK_PCT=0.10`, `SL≈2%`) の場合:

```
risk_usdt = 28 × 0.10% = $0.028
notional  = 0.028 / 0.02 = $1.40
```

銘柄ごとのMEXC最小ロット・最小名目額を下回る場合は `skipped_below_min_cost` となり、
注文しないのが正常です。注文を成立させるために `LIVE_BASE_RISK_PCT` やレバレッジを
引き上げず、DryRunで同一ポリシーの検証履歴を蓄積してください。

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

## さくらへの増分データ同期

GitHub Actions はスキャン/実弾runの終了後に
`tools/sync_trading_data.py` を実行します。送信先は
`https://leatherwallet.sakura.ne.jp/trading-ingest`、repo namespace は
`mexc-momentum-scanner` で固定しています。

GitHub Actions のsecretに `TD_HMAC_SECRET` を登録すると同期が有効になります。
未登録中は同期だけがno-opになり、既存スキャン・DryRun・実弾安全判定には
影響しません。secretは32 bytes以上とし、リポジトリへ保存しないでください。

同期するのは累積JSONそのものではなく、次のappend-only eventです。

- `mexc.shadow_signal`: STRICT却下を含む全候補、判定時点feature、時刻
- `mexc.live_decision` / `mexc.live_reject`: 採用・見送り理由とpolicy
- `mexc.outcome`: 親outcome、MFE/MAE、全entry variantの最終結果
- `mexc.execution`: 検証済み実弾fill・SL/TP保護・実リスク
- `mexc.policy`: policy version、fingerprint、非secret判定設定

`event_time` と `available_at` を分け、同じmarket observationの反復runは
`signal_group_id` でまとめられます。event IDとPOST idempotency keyは
決定的に生成されるため、通信断後に再送しても二重保存されません。

初回だけ既存のhot/archiveを読み、以後は
`data/trading_data_sync_state.json` のstream別high-water cursorより新しい
eventだけを送ります。cursorはサーバーがbatchを受理した後にだけ進みます。
runner-local outboxは受理済みprefixだけを削るため、途中失敗時も未送信分が
ログartifactに残ります。累積 `experiments.json` を毎回アップロードする
処理はありません。

```bash
# secret未設定なら安全にno-op
python tools/sync_trading_data.py --runtime-only

# gateway設定後: 既存履歴の初回backfill + 今後のincremental sync
python tools/sync_trading_data.py
```

移行期間中は従来のGit data commitも継続します。さくら側の件数・checksum・
判定再生結果を照合してから、別変更でGitへのdata commitを停止します。

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
