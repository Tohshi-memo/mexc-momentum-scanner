# Decision Report

- generated_at: 2026-06-07T06:27:00.808286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5929**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=5929, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/15 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.55% | **+0.55%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.25% | **+0.90%** |
| MARKET_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$99.99** / 初期 $100.00 (-0.01%)
- 確定トレード: 3件 (TP 1 / SL 2 / EXP 0)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$138.07** / 初期 $100.00 (+38.07%)
- 確定: 1048件 (Win 252 / Loss 322 / Flat 474) / skip 1442件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $138.07

## 4. Latest Market Context

- 更新: 2026-06-07T06:26:57.726814+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=61807.1
- Funnel: target 771 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +55.46% | $5,269,159.47 |
| LAB/USDT:USDT | +37.90% | $64,299,866.19 |
| BSB/USDT:USDT | +26.79% | $4,787,287.10 |
| BLESS/USDT:USDT | +24.79% | $4,561,892.78 |
| EDEN/USDT:USDT | +21.81% | $1,639,432.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.24% | +4.08% |
| BLESS/USDT:USDT | below_1h_threshold | +2.78% | +2.62% |
| HOME/USDT:USDT | below_1h_threshold | +2.25% | +2.10% |
| ONDO/USDT:USDT | below_1h_threshold | +2.17% | +2.02% |
| CLO/USDT:USDT | below_1h_threshold | +2.15% | +1.99% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
