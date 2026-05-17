# Decision Report

- generated_at: 2026-05-17T08:13:36.025462+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4391**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4391, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.75% | **+0.55%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.33% | **+0.15%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.07% | **+0.05%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.98% | **+1.29%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.17% | **+0.76%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| ASK_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 559件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T08:13:32.427282+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78117.2
- Funnel: target 760 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +28.36% | $10,196,969.86 |
| CGPT/USDT:USDT | +24.93% | $2,050,170.99 |
| BSB/USDT:USDT | +19.45% | $4,916,960.05 |
| ASTEROID/USDT:USDT | +15.86% | $4,349,371.92 |
| AIGENSYN/USDT:USDT | +12.38% | $2,546,141.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.59% | +2.62% |
| CHZ/USDT:USDT | below_1h_threshold | +1.17% | +1.19% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.83% | +0.86% |
| AIA/USDT:USDT | below_1h_threshold | +0.72% | +0.74% |
| ATOM/USDT:USDT | below_1h_threshold | +0.43% | +0.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
