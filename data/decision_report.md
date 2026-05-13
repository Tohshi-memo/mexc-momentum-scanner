# Decision Report

- generated_at: 2026-05-13T13:08:00.810434+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4223**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4223, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.09% | **+0.09%** |
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |
| LIMIT_2PCT | 15/20 | 75.0% | -0.38% | **-0.28%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.49% | **-0.44%** |
| LIMIT_5PCT | 6/20 | 30.0% | -1.52% | **-0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.97% | **+0.68%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 443件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T13:07:57.315935+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=80258.4
- Funnel: target 765 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +40.18% | $131,377,849.28 |
| COS/USDT:USDT | +32.57% | $1,798,210.98 |
| JCT/USDT:USDT | +27.99% | $1,026,991.79 |
| UB/USDT:USDT | +26.43% | $9,917,537.85 |
| INJ/USDT:USDT | +25.96% | $149,623,313.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUTH/USDT:USDT | below_1h_threshold | +3.20% | +3.08% |
| INJ/USDT:USDT | below_1h_threshold | +2.15% | +2.02% |
| COS/USDT:USDT | below_1h_threshold | +2.07% | +1.95% |
| SATO/USDT:USDT | below_1h_threshold | +1.59% | +1.47% |
| UB/USDT:USDT | below_1h_threshold | +1.31% | +1.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
