# Decision Report

- generated_at: 2026-05-19T15:13:44.202226+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4473**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4473, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.09% | **-0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.04% | **+0.03%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.04% | **+0.02%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.12% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.17% | **+2.11%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.53% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.92% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.71** / 初期 $100.00 (+22.71%)
- 確定: 470件 (Win 124 / Loss 162 / Flat 184) / skip 564件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $122.71

## 4. Latest Market Context

- 更新: 2026-05-19T15:13:42.200314+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=76514.1
- Funnel: target 764 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +31.82% | $14,668,881.93 |
| PLAY/USDT:USDT | +30.97% | $5,940,610.77 |
| EDEN/USDT:USDT | +25.87% | $3,894,888.68 |
| ENJ/USDT:USDT | +18.61% | $1,429,354.45 |
| ONT/USDT:USDT | +10.89% | $2,302,250.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.79% | +2.60% |
| H/USDT:USDT | below_1h_threshold | +1.73% | +1.54% |
| ENJ/USDT:USDT | below_1h_threshold | +1.62% | +1.43% |
| KITE/USDT:USDT | below_1h_threshold | +0.86% | +0.67% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.83% | +0.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
