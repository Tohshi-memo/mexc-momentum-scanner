# Decision Report

- generated_at: 2026-11-23T14:52:52.381116+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19489**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19489, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.74% | **-1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.22% | **+0.13%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.31% | **+0.11%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.12% | **-0.09%** |
| LIMIT_2PCT | 19/20 | 95.0% | -0.37% | **-0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.31% | **+2.31%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.73% | **+1.78%** |
| LIMIT_BB3S_LONG | 10/14 | 71.4% | +1.21% | **+0.86%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.89% | **+0.85%** |
| LIMIT_2PCT_LONG | 7/20 | 35.0% | +2.22% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,040.93** / 初期 $100.00 (+1940.93%)
- 確定: 7585件 (Win 2185 / Loss 2432 / Flat 2968) / skip 8465件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $2,040.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7681件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1145 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7668件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000664 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T14:52:09.986839+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.18% price=63096.0
- Funnel: target 1088 → liquid 136 → pre 50 → checked 50 → surge 18 → strict 11
- Surge前reject: below_1h_threshold=32, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=2, 4h RSI 75.7 >= 65=1, 4h RSI 67.7 >= 65=1, 4h RSI 78.0 >= 65=1, 4h RSI 73.0 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +102.86% | $2,722,790.77 |
| PROM/USDT:USDT | +47.76% | $1,524,215.29 |
| NVDL/USDT:USDT | +46.22% | $5,785,220.50 |
| ELSA/USDT:USDT | +27.45% | $2,776,145.62 |
| EVAA/USDT:USDT | +24.81% | $38,755,702.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +5.92% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +3.99% | +5.16% |
| UNI/USDT:USDT | below_1h_threshold | +3.87% | +5.05% |
| LIT/USDT:USDT | below_1h_threshold | +3.72% | +4.90% |
| FET/USDT:USDT | below_1h_threshold | +2.62% | +3.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
