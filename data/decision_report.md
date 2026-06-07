# Decision Report

- generated_at: 2026-06-07T05:32:10.162193+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5926**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=5926, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.25% | **+1.30%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.96% | **+0.78%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| MARKET_LONG | 20/20 | 100.0% | +0.06% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$99.99** / 初期 $100.00 (-0.01%)
- 確定トレード: 3件 (TP 1 / SL 2 / EXP 0)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.39** / 初期 $100.00 (+37.39%)
- 確定: 1045件 (Win 251 / Loss 321 / Flat 473) / skip 1442件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $137.39

## 4. Latest Market Context

- 更新: 2026-06-07T05:32:07.035464+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=61680.0
- Funnel: target 771 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +56.41% | $4,223,412.70 |
| LAB/USDT:USDT | +39.77% | $64,404,850.71 |
| BLESS/USDT:USDT | +24.33% | $4,507,947.54 |
| EDEN/USDT:USDT | +19.62% | $1,449,787.08 |
| BTW/USDT:USDT | +17.80% | $9,397,436.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.46% | +4.74% |
| CLO/USDT:USDT | below_1h_threshold | +3.82% | +4.10% |
| EDEN/USDT:USDT | below_1h_threshold | +3.08% | +3.36% |
| BLESS/USDT:USDT | below_1h_threshold | +2.86% | +3.14% |
| ASTER/USDT:USDT | below_1h_threshold | +2.04% | +2.32% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
