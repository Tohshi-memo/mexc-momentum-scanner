# Decision Report

- generated_at: 2026-05-19T20:14:35.975778+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4498**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4498, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +2.54% | **+1.27%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_BB3S | 6/11 | 54.5% | +1.05% | **+0.57%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +3.39% | **+1.88%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.39% | **+1.87%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.01% | **+1.51%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.12% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 586件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T20:14:34.002525+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=76910.9
- Funnel: target 760 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +49.09% | $23,269,435.63 |
| EDEN/USDT:USDT | +27.57% | $12,561,606.69 |
| VVV/USDT:USDT | +14.62% | $10,630,835.44 |
| LAB/USDT:USDT | +10.07% | $85,954,944.60 |
| LIT/USDT:USDT | +9.43% | $2,092,080.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +1.14% | +0.97% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.12% | +0.95% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.12% | +0.95% |
| FIDA/USDT:USDT | below_1h_threshold | +0.76% | +0.59% |
| APE/USDT:USDT | below_1h_threshold | +0.70% | +0.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
