# Decision Report

- generated_at: 2026-11-23T14:12:41.006168+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19463**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19463, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.98% | **-1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.30% | **+0.92%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.42% | **+0.78%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 14/20 | 70.0% | +0.38% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.28% | **+4.28%** |
| MARKET_LONG | 20/20 | 100.0% | +1.68% | **+1.68%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +3.79% | **+1.51%** |
| LIMIT_1PCT_LONG | 10/20 | 50.0% | +2.67% | **+1.33%** |
| LIMIT_2PCT_LONG | 5/20 | 25.0% | +2.41% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,895.92** / 初期 $100.00 (+1795.92%)
- 確定: 7561件 (Win 2167 / Loss 2427 / Flat 2967) / skip 8463件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NBISSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,895.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7655件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0761 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7641件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000301 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T14:12:07.667536+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.03% price=63188.9
- Funnel: target 1088 → liquid 129 → pre 50 → checked 50 → surge 19 → strict 8
- Surge前reject: below_1h_threshold=31, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 73.3 >= 65=1, 4h RSI 76.4 >= 65=1, 4h RSI 67.3 >= 65=1, 4h RSI 66.1 >= 65=1, 4h RSI 68.1 >= 65=1, 4h RSI 68.0 >= 65=1, 4h RSI 70.9 >= 65=1, 4h RSI 67.4 >= 65=1, 4h RSI 67.8 >= 65=1, 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +104.84% | $2,615,668.70 |
| NVDL/USDT:USDT | +42.28% | $1,253,794.71 |
| ELSA/USDT:USDT | +36.81% | $2,616,120.12 |
| ARIA/USDT:USDT | +32.35% | $5,575,291.02 |
| SOXL/USDT:USDT | +30.63% | $358,514,653.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +5.77% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +3.99% | +5.02% |
| PROM/USDT:USDT | below_1h_threshold | +2.32% | +3.35% |
| FET/USDT:USDT | below_1h_threshold | +1.75% | +2.78% |
| DOT/USDT:USDT | below_1h_threshold | +1.30% | +2.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
