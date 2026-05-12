# Decision Report

- generated_at: 2026-05-12T03:22:50.035836+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4093**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4093, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.03% | **+1.01%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.80% | **+0.68%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.54% | **+1.91%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.82% | **+1.64%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.53% | **+1.52%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.41% | **+1.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.64% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.18** / 初期 $100.00 (+11.18%)
- 確定: 230件 (Win 60 / Loss 80 / Flat 90) / skip 424件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $111.18

## 4. Latest Market Context

- 更新: 2026-05-12T03:22:46.870223+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=81162.0
- Funnel: target 762 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +55.11% | $2,063,778.70 |
| SKYAI/USDT:USDT | +42.73% | $40,621,378.44 |
| USELESS/USDT:USDT | +20.65% | $4,424,433.25 |
| SAGA/USDT:USDT | +20.61% | $7,480,356.61 |
| GUA/USDT:USDT | +18.69% | $1,166,591.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +3.14% | +3.22% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.49% | +2.56% |
| SAGA/USDT:USDT | below_1h_threshold | +2.39% | +2.47% |
| RIF/USDT:USDT | below_1h_threshold | +2.12% | +2.19% |
| BILL/USDT:USDT | below_1h_threshold | +1.82% | +1.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
