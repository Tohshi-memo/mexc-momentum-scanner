# Decision Report

- generated_at: 2026-07-04T04:58:22.098023+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8219**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8219, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.90% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| ASK_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.38% | **+0.69%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.89% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$303.58** / 初期 $100.00 (+203.58%)
- 確定: 2536件 (Win 787 / Loss 845 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $303.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.73** / 初期 $100.00 (+6.73%)
- 確定: 615件 (Win 149 / Loss 149 / Flat 317) / skip 1015件
- 成長率目線: 平均log +0.000106 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0788 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.73

## 5. Latest Market Context

- 更新: 2026-07-04T04:58:16.624456+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62625.8
- Funnel: target 834 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1, 4h RSI 68.3 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +90.23% | $4,397,797.62 |
| TLM/USDT:USDT | +44.17% | $40,657,646.38 |
| HMSTR/USDT:USDT | +35.95% | $2,961,835.45 |
| BAS/USDT:USDT | +29.77% | $4,194,660.09 |
| MAGMA/USDT:USDT | +25.96% | $15,530,503.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POPCAT/USDT:USDT | below_1h_threshold | +4.49% | +4.46% |
| VELVET/USDT:USDT | below_1h_threshold | +4.12% | +4.10% |
| NEX/USDT:USDT | below_1h_threshold | +3.61% | +3.59% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.50% | +3.47% |
| LAB/USDT:USDT | below_1h_threshold | +2.84% | +2.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
