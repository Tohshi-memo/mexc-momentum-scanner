# Decision Report

- generated_at: 2026-07-01T03:55:04.802258+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7943**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.50% / filled 20/20。**
- 全期間 MARKET基準: n=7943, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +2.35% | **+1.64%** |
| ASK | 20/20 | 100.0% | +1.56% | **+1.56%** |
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.52% | **+1.29%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.62% | **+1.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.65% | **+0.42%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.50% | **+0.30%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.52% | **+0.29%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.19% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$256.55** / 初期 $100.00 (+156.55%)
- 確定: 2356件 (Win 714 / Loss 787 / Flat 855) / skip 2148件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $256.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.52** / 初期 $100.00 (+6.52%)
- 確定: 485件 (Win 125 / Loss 121 / Flat 239) / skip 869件
- 成長率目線: 平均log +0.000130 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0338 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.52

## 5. Latest Market Context

- 更新: 2026-07-01T03:54:58.565540+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=59196.8
- Funnel: target 818 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1, 4h RSI 81.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYDX/USDT:USDT | +18.94% | $3,660,410.37 |
| TAIKO/USDT:USDT | +16.85% | $1,688,380.70 |
| M/USDT:USDT | +16.11% | $4,588,489.50 |
| BTW/USDT:USDT | +15.88% | $11,280,739.98 |
| BEAT/USDT:USDT | +15.28% | $20,341,957.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.46% | +3.24% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.97% | +2.75% |
| BASED/USDT:USDT | below_1h_threshold | +2.94% | +2.71% |
| ADA/USDT:USDT | below_1h_threshold | +2.66% | +2.44% |
| TAC/USDT:USDT | below_1h_threshold | +2.62% | +2.39% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
