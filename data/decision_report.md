# Decision Report

- generated_at: 2026-06-07T09:15:48.666704+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5939**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5939, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.56% | **-1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.63% | **+0.63%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.93% | **+1.73%** |
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.33% | **+1.28%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.42% | **+1.06%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$143.00** / 初期 $100.00 (+43.00%)
- 確定: 1058件 (Win 258 / Loss 324 / Flat 476) / skip 1442件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $143.00

## 4. Latest Market Context

- 更新: 2026-06-07T09:15:45.712812+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=62790.1
- Funnel: target 771 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +55.91% | $6,570,254.32 |
| BTW/USDT:USDT | +41.81% | $10,538,657.46 |
| LAB/USDT:USDT | +39.93% | $63,183,072.46 |
| BSB/USDT:USDT | +29.57% | $6,466,260.37 |
| EDEN/USDT:USDT | +28.05% | $3,222,868.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +2.47% | +2.52% |
| SIREN/USDT:USDT | below_1h_threshold | +2.27% | +2.33% |
| LUNC/USDT:USDT | below_1h_threshold | +1.71% | +1.76% |
| B/USDT:USDT | below_1h_threshold | +1.59% | +1.65% |
| LAB/USDT:USDT | below_1h_threshold | +1.44% | +1.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
