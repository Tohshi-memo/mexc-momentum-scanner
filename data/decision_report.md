# Decision Report

- generated_at: 2026-07-04T05:08:10.858257+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8220**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8220, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.90% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| ASK_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.38% | **+0.69%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$306.61** / 初期 $100.00 (+206.61%)
- 確定: 2537件 (Win 788 / Loss 845 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $306.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.73** / 初期 $100.00 (+6.73%)
- 確定: 616件 (Win 149 / Loss 149 / Flat 318) / skip 1015件
- 成長率目線: 平均log +0.000106 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0833 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $106.73

## 5. Latest Market Context

- 更新: 2026-07-04T05:08:04.683289+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=62579.5
- Funnel: target 834 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +84.06% | $4,428,355.48 |
| TLM/USDT:USDT | +61.23% | $40,453,517.95 |
| HMSTR/USDT:USDT | +36.39% | $3,011,822.39 |
| BAS/USDT:USDT | +30.32% | $4,070,332.07 |
| MAGMA/USDT:USDT | +25.46% | $15,259,529.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +1.66% | +1.79% |
| UB/USDT:USDT | below_1h_threshold | +1.27% | +1.40% |
| NOM/USDT:USDT | below_1h_threshold | +0.68% | +0.81% |
| TRB/USDT:USDT | below_1h_threshold | +0.57% | +0.70% |
| HMSTR/USDT:USDT | below_1h_threshold | +0.39% | +0.52% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
