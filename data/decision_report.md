# Decision Report

- generated_at: 2026-11-23T14:17:30.687341+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19466**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19466, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.52% | **-2.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.14% | **+1.07%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.29% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.72% | **+3.54%** |
| MARKET_LONG | 20/20 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_1PCT_LONG | 9/20 | 45.0% | +3.73% | **+1.68%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +4.23% | **+1.27%** |
| LIMIT_2PCT_LONG | 3/20 | 15.0% | +3.30% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,922.56** / 初期 $100.00 (+1822.56%)
- 確定: 7564件 (Win 2169 / Loss 2428 / Flat 2967) / skip 8463件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNDKSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,922.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7658件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0880 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7643件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T14:16:56.044742+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.83% price=63316.2
- Funnel: target 1088 → liquid 131 → pre 50 → checked 50 → surge 17 → strict 6
- Surge前reject: below_1h_threshold=33, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.6 >= 65=1, 4h RSI 74.3 >= 65=1, 4h RSI 77.3 >= 65=1, 4h RSI 68.3 >= 65=1, 4h RSI 65.6 >= 65=1, 4h RSI 67.5 >= 65=1, 4h RSI 69.7 >= 65=1, 4h RSI 69.2 >= 65=1, 4h RSI 71.3 >= 65=1, 4h RSI 66.1 >= 65=1, 4h RSI 70.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +102.67% | $2,636,421.62 |
| NVDL/USDT:USDT | +42.10% | $4,091,265.45 |
| ELSA/USDT:USDT | +34.53% | $2,632,076.23 |
| ARIA/USDT:USDT | +31.61% | $5,642,647.53 |
| SOXL/USDT:USDT | +30.07% | $385,433,571.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +5.58% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +3.99% | +4.82% |
| ELSA/USDT:USDT | below_1h_threshold | +3.27% | +4.10% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.98% | +3.82% |
| WLD/USDT:USDT | below_1h_threshold | +2.89% | +3.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
