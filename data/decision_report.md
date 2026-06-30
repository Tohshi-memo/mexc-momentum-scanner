# Decision Report

- generated_at: 2026-06-30T14:24:20.526500+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7907**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7907, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.46% | **+0.49%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.81% | **+0.38%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.52% | **+0.26%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.90% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.84% | **+1.84%** |
| ASK_LONG | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_1PCT_LONG | 11/20 | 55.0% | +2.33% | **+1.28%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +1.88% | **+0.84%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.86% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2113件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.78** / 初期 $100.00 (+6.78%)
- 確定: 459件 (Win 122 / Loss 119 / Flat 218) / skip 859件
- 成長率目線: 平均log +0.000143 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0355 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $106.78

## 5. Latest Market Context

- 更新: 2026-06-30T14:24:13.416836+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.64% price=59089.5
- Funnel: target 818 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.0 >= 65=1, 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IN/USDT:USDT | +54.88% | $1,976,115.31 |
| SYN/USDT:USDT | +49.27% | $54,555,775.74 |
| ANSEM/USDT:USDT | +40.20% | $1,118,667.86 |
| AIGENSYN/USDT:USDT | +37.10% | $14,516,434.56 |
| CAP/USDT:USDT | +27.25% | $5,145,057.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PYTH/USDT:USDT | below_relative_strength | +5.15% | +4.51% |
| AEHRSTOCK/USDT:USDT | below_1h_threshold | +3.77% | +3.12% |
| TAC/USDT:USDT | below_1h_threshold | +3.27% | +2.63% |
| KORU/USDT:USDT | below_1h_threshold | +2.86% | +2.21% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +1.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
