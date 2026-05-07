# Decision Report

- generated_at: 2026-05-07T16:27:45.352795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3658**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3658, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.86% | **+0.69%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.28% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.08% | **+1.56%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.86% | **+1.11%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.91% | **+0.96%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.83% | **+0.91%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 21件 (TP 6 / SL 13 / EXP 2)
- 最新: FHE/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.16** / 初期 $100.00 (+12.16%)
- 確定: 152件 (Win 46 / Loss 53 / Flat 53) / skip 67件
- 成長率目線: 平均log +0.000755 / 幾何平均 +0.076% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DYDX/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $112.16

## 4. Latest Market Context

- 更新: 2026-05-07T16:27:39.163221+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=79963.8
- Funnel: target 771 → liquid 181 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.4 >= 65=1, 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +22.13% | $4,340,647.39 |
| HIGH/USDT:USDT | +12.22% | $1,011,686.12 |
| FHE/USDT:USDT | +10.12% | $13,991,671.36 |
| LAB/USDT:USDT | +7.61% | $266,914,546.60 |
| BILL/USDT:USDT | +6.59% | $11,573,861.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +4.70% | +4.58% |
| M/USDT:USDT | below_1h_threshold | +3.83% | +3.71% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.64% | +3.51% |
| NOT/USDT:USDT | below_1h_threshold | +3.60% | +3.47% |
| AVNT/USDT:USDT | below_1h_threshold | +2.92% | +2.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
