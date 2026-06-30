# Decision Report

- generated_at: 2026-06-30T15:08:12.137481+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7913**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7913, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.09% | **-2.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.57% | **+0.77%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.83% | **+0.68%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.78% | **+0.57%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.69% | **+0.47%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.73% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.46% | **+2.46%** |
| ASK_LONG | 20/20 | 100.0% | +2.12% | **+2.12%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.58% | **+0.90%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +1.72% | **+0.43%** |
| LIMIT_5PCT_LONG | 5/20 | 25.0% | +1.31% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2119件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.73** / 初期 $100.00 (+6.73%)
- 確定: 463件 (Win 124 / Loss 120 / Flat 219) / skip 861件
- 成長率目線: 平均log +0.000141 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0340 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $106.73

## 5. Latest Market Context

- 更新: 2026-06-30T15:08:06.049384+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=58307.7
- Funnel: target 818 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IN/USDT:USDT | +91.37% | $5,598,743.98 |
| ANSEM/USDT:USDT | +40.10% | $1,158,539.03 |
| SYN/USDT:USDT | +37.28% | $58,771,039.48 |
| AIGENSYN/USDT:USDT | +35.12% | $14,778,052.53 |
| H/USDT:USDT | +27.08% | $11,108,375.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.62% | +2.88% |
| SOXL/USDT:USDT | below_1h_threshold | +1.75% | +2.01% |
| SYN/USDT:USDT | below_1h_threshold | +1.63% | +1.88% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.46% | +1.72% |
| KORU/USDT:USDT | below_1h_threshold | +1.41% | +1.67% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
