# Decision Report

- generated_at: 2026-10-14T11:21:21.592494+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16678**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16678, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.50% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.16% | **+0.99%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.78% | **+0.71%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.65% | **+0.58%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,278.87** / 初期 $100.00 (+1178.87%)
- 確定: 6296件 (Win 1845 / Loss 2018 / Flat 2433) / skip 6943件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RSR/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,278.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$270.76** / 初期 $100.00 (+170.76%)
- 確定: 3654件 (Win 1015 / Loss 864 / Flat 1775) / skip 6435件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $270.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4836件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000082 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-14T11:21:11.069594+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=83418.9
- Funnel: target 1085 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +61.24% | $1,597,519.29 |
| WAL/USDT:USDT | +38.46% | $2,858,304.60 |
| BTW/USDT:USDT | +32.40% | $44,069,043.24 |
| TRUTH/USDT:USDT | +32.00% | $3,712,015.58 |
| AVA/USDT:USDT | +17.93% | $1,351,317.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAT/USDT:USDT | below_1h_threshold | +2.16% | +2.17% |
| GRASS/USDT:USDT | below_1h_threshold | +0.89% | +0.91% |
| BTW/USDT:USDT | below_1h_threshold | +0.88% | +0.90% |
| AVA/USDT:USDT | below_1h_threshold | +0.77% | +0.79% |
| PYTH/USDT:USDT | below_1h_threshold | +0.71% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
