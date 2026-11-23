# Decision Report

- generated_at: 2026-11-23T14:27:47.610414+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19475**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19475, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.28% | **-2.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.56% | **+0.25%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.08% | **+0.06%** |
| LIMIT_FIB1272 | 14/20 | 70.0% | -0.55% | **-0.38%** |
| LIMIT_2PCT | 19/20 | 95.0% | -0.71% | **-0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.78% | **+2.78%** |
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +4.24% | **+2.54%** |
| LIMIT_1PCT_LONG | 5/20 | 25.0% | +3.74% | **+0.94%** |
| LIMIT_ATR_LONG | 4/20 | 20.0% | +3.02% | **+0.60%** |
| LIMIT_2PCT_LONG | 3/20 | 15.0% | +2.68% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,000.82** / 初期 $100.00 (+1900.82%)
- 確定: 7573件 (Win 2177 / Loss 2428 / Flat 2968) / skip 8463件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNDKSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $2,000.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7667件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7655件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000630 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T14:27:12.370561+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.61% price=64239.8
- Funnel: target 1088 → liquid 134 → pre 50 → checked 50 → surge 19 → strict 2
- Surge前reject: below_1h_threshold=29, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.3 >= 65=1, 4h RSI 66.3 >= 65=1, 4h RSI 74.5 >= 65=1, 4h RSI 78.9 >= 65=1, 4h RSI 72.0 >= 65=1, 4h RSI 67.0 >= 65=1, 4h RSI 66.8 >= 65=1, 4h RSI 68.7 >= 65=1, 4h RSI 67.4 >= 65=1, 4h RSI 74.3 >= 65=1, 4h RSI 70.8 >= 65=1, 4h RSI 71.0 >= 65=1, 4h RSI 67.8 >= 65=1, 4h RSI 71.6 >= 65=1, 4h RSI 72.3 >= 65=1, 4h RSI 70.2 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +109.94% | $2,658,098.74 |
| NVDL/USDT:USDT | +47.28% | $4,872,328.16 |
| SNXX/USDT:USDT | +36.93% | $8,645,045.79 |
| PROM/USDT:USDT | +36.39% | $1,267,202.89 |
| ELSA/USDT:USDT | +34.93% | $2,697,357.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_relative_strength | +5.58% | +4.97% |
| INTCSTOCK/USDT:USDT | below_relative_strength | +5.09% | +4.48% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +4.13% |
| ENA/USDT:USDT | below_1h_threshold | +4.63% | +4.01% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +3.99% | +3.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
