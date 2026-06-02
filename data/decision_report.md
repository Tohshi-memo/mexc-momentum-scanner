# Decision Report

- generated_at: 2026-06-02T09:03:07.847724+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5435**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=5435, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.46% | **+1.46%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.02% | **+0.82%** |
| LIMIT_BB3S | 8/19 | 42.1% | +1.83% | **+0.77%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.66% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.22%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.17% | **+0.12%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.28% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 85件 (TP 24 / SL 58 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.96** / 初期 $100.00 (+34.96%)
- 確定: 947件 (Win 223 / Loss 284 / Flat 440) / skip 1049件
- 成長率目線: 平均log +0.000317 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $134.96

## 4. Latest Market Context

- 更新: 2026-06-02T09:03:04.846198+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=69616.8
- Funnel: target 772 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +40.31% | $2,083,537.24 |
| SKYAI/USDT:USDT | +35.76% | $19,535,538.18 |
| MRVLSTOCK/USDT:USDT | +25.10% | $3,587,879.32 |
| USELESS/USDT:USDT | +20.98% | $1,601,720.78 |
| RIF/USDT:USDT | +19.51% | $1,860,979.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +0.92% | +1.17% |
| UAI/USDT:USDT | below_1h_threshold | +0.71% | +0.95% |
| H/USDT:USDT | below_1h_threshold | +0.68% | +0.93% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.66% | +0.91% |
| EPIC/USDT:USDT | below_1h_threshold | +0.56% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
