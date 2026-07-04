# Decision Report

- generated_at: 2026-07-04T05:17:53.411905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8221**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8221, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.35% | **-1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +1.30% | **+0.65%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_BB3S | 5/18 | 27.8% | -0.29% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| ASK_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.21% | **+1.10%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.98% | **+0.89%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.94% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$308.15** / 初期 $100.00 (+208.15%)
- 確定: 2538件 (Win 789 / Loss 845 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $308.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.73** / 初期 $100.00 (+6.73%)
- 確定: 617件 (Win 149 / Loss 149 / Flat 319) / skip 1015件
- 成長率目線: 平均log +0.000106 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0833 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $106.73

## 5. Latest Market Context

- 更新: 2026-07-04T05:17:47.213880+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=62542.1
- Funnel: target 834 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +82.00% | $4,482,099.47 |
| TLM/USDT:USDT | +68.90% | $41,364,094.98 |
| HMSTR/USDT:USDT | +41.87% | $3,147,597.84 |
| BAS/USDT:USDT | +30.22% | $4,077,724.30 |
| MAGMA/USDT:USDT | +29.22% | $15,382,078.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +4.49% | +4.68% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.08% | +3.27% |
| NEX/USDT:USDT | below_1h_threshold | +2.45% | +2.64% |
| UB/USDT:USDT | below_1h_threshold | +1.76% | +1.95% |
| TRB/USDT:USDT | below_1h_threshold | +1.63% | +1.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
