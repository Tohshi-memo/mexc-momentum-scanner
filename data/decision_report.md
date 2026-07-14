# Decision Report

- generated_at: 2026-07-14T12:56:18.341438+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8691**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8691, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.27% | **+0.12%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.65% | **+1.72%** |
| LIMIT_BB3S_LONG | 10/11 | 90.9% | +1.56% | **+1.42%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.82% | **+1.36%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.72% | **+1.36%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$325.21** / 初期 $100.00 (+225.21%)
- 確定: 2857件 (Win 891 / Loss 928 / Flat 1038) / skip 2395件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $325.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.49** / 初期 $100.00 (+5.49%)
- 確定: 689件 (Win 161 / Loss 162 / Flat 366) / skip 1413件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0547 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 59件 (Win 19 / Loss 39 / Flat 1) / pending 0件 / skip 103件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SXT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-14T12:56:07.214578+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.60% price=63816.3
- Funnel: target 864 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +72.99% | $29,776,309.29 |
| AIOT/USDT:USDT | +23.42% | $8,655,764.39 |
| BSB/USDT:USDT | +22.29% | $4,444,649.27 |
| HEI/USDT:USDT | +21.23% | $1,385,183.00 |
| SXT/USDT:USDT | +19.09% | $7,932,356.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EGLD/USDT:USDT | below_1h_threshold | +3.55% | +1.94% |
| CRV/USDT:USDT | below_1h_threshold | +3.35% | +1.75% |
| SOXL/USDT:USDT | below_1h_threshold | +3.34% | +1.74% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.15% | +1.55% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.81% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
