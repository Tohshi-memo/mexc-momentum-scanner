# Decision Report

- generated_at: 2026-11-23T14:42:36.589123+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19485**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19485, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-3.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.16% | **-3.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +1.18% | **+0.30%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.32% | **+0.19%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.12% | **+0.06%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.57% | **-0.40%** |
| LIMIT_2PCT | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.16% | **+3.16%** |
| LIMIT_1PCT_LONG | 10/20 | 50.0% | +4.68% | **+2.34%** |
| LIMIT_BB3S_LONG | 9/14 | 64.3% | +3.52% | **+2.26%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +4.73% | **+1.42%** |
| LIMIT_2PCT_LONG | 4/20 | 20.0% | +6.72% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,071.85** / 初期 $100.00 (+1971.85%)
- 確定: 7582件 (Win 2185 / Loss 2429 / Flat 2968) / skip 8464件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $2,071.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7677件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1455 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7664件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000789 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T14:42:00.037590+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.85% price=63305.9
- Funnel: target 1088 → liquid 135 → pre 50 → checked 50 → surge 17 → strict 7
- Surge前reject: below_1h_threshold=33, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=2, 4h RSI 74.3 >= 65=1, 4h RSI 66.4 >= 65=1, 4h RSI 71.9 >= 65=1, 4h RSI 67.9 >= 65=1, 4h RSI 69.0 >= 65=1, 4h RSI 65.7 >= 65=1, 4h RSI 67.5 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +106.13% | $2,708,199.45 |
| PROM/USDT:USDT | +42.48% | $1,362,092.37 |
| NVDL/USDT:USDT | +37.01% | $5,633,803.82 |
| ELSA/USDT:USDT | +31.45% | $2,743,280.88 |
| SNXX/USDT:USDT | +26.02% | $10,354,464.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +5.59% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +3.99% | +4.84% |
| INJ/USDT:USDT | below_1h_threshold | +3.92% | +4.77% |
| LIT/USDT:USDT | below_1h_threshold | +3.73% | +4.58% |
| UNI/USDT:USDT | below_1h_threshold | +3.63% | +4.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
