# Decision Report

- generated_at: 2026-06-21T01:15:35.872157+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7283**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7283, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.52% | **+0.18%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.47% | **+2.98%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +3.14% | **+2.36%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.39% | **+1.44%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.89% | **+1.32%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.19% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.04** / 初期 $100.00 (+135.04%)
- 確定: 2012件 (Win 595 / Loss 659 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALICE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $235.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 384件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0178 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T01:15:30.319617+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64229.1
- Funnel: target 796 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +45.55% | $48,093,194.94 |
| ALICE/USDT:USDT | +39.03% | $2,568,754.23 |
| RESOLV/USDT:USDT | +25.66% | $3,306,605.75 |
| ASTEROID/USDT:USDT | +9.78% | $1,590,576.64 |
| AXS/USDT:USDT | +9.13% | $12,527,420.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MANA/USDT:USDT | below_1h_threshold | +2.52% | +2.58% |
| CHIP/USDT:USDT | below_1h_threshold | +1.57% | +1.63% |
| SAND/USDT:USDT | below_1h_threshold | +1.14% | +1.20% |
| AERO/USDT:USDT | below_1h_threshold | +0.76% | +0.82% |
| JUP/USDT:USDT | below_1h_threshold | +0.70% | +0.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
