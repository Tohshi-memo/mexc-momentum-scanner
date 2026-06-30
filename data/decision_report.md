# Decision Report

- generated_at: 2026-06-30T15:36:11.603133+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7915**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7915, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.10% | **-2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.35% | **+1.17%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.22% | **+1.08%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.83% | **+0.97%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.80% | **+0.87%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.14% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.06% | **+2.06%** |
| ASK_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.26% | **+1.30%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.58% | **+0.77%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +2.12% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2121件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.35** / 初期 $100.00 (+6.35%)
- 確定: 465件 (Win 124 / Loss 121 / Flat 220) / skip 861件
- 成長率目線: 平均log +0.000132 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IN/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $106.35

## 5. Latest Market Context

- 更新: 2026-06-30T15:36:06.374861+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=58386.0
- Funnel: target 818 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.4 >= 65=1, 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IN/USDT:USDT | +97.84% | $9,200,666.59 |
| ANSEM/USDT:USDT | +44.02% | $1,185,080.73 |
| SYN/USDT:USDT | +42.09% | $60,773,685.67 |
| AIGENSYN/USDT:USDT | +31.19% | $14,982,538.49 |
| RIF/USDT:USDT | +29.56% | $1,065,709.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.52% | +4.64% |
| DYDX/USDT:USDT | below_1h_threshold | +3.78% | +3.91% |
| H/USDT:USDT | below_1h_threshold | +3.61% | +3.73% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.60% | +2.72% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.30% | +2.43% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
