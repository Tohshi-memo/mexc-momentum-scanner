# Decision Report

- generated_at: 2026-05-20T07:48:53.271005+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4531**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4531, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.30% | **+0.18%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.06% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |
| ASK_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.14% | **+0.04%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.07% | **+0.04%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.78** / 初期 $100.00 (+23.78%)
- 確定: 493件 (Win 129 / Loss 170 / Flat 194) / skip 599件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $123.78

## 4. Latest Market Context

- 更新: 2026-05-20T07:48:50.039051+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=77245.1
- Funnel: target 762 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1, 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +38.33% | $1,961,160.53 |
| PROMPT/USDT:USDT | +28.58% | $12,358,864.28 |
| SKYAI/USDT:USDT | +26.60% | $8,945,158.95 |
| LIT/USDT:USDT | +22.33% | $7,903,729.34 |
| EDEN/USDT:USDT | +20.90% | $21,295,112.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +2.79% | +2.97% |
| STRK/USDT:USDT | below_1h_threshold | +1.99% | +2.16% |
| UP/USDT:USDT | below_1h_threshold | +1.91% | +2.09% |
| PROMPT/USDT:USDT | below_1h_threshold | +1.70% | +1.87% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.66% | +1.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
