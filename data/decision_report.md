# Decision Report

- generated_at: 2026-05-22T18:04:00.089080+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4732**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4732, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +4.29% | **+1.29%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.75% | **+0.87%** |
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.85% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.72% | **+2.23%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.65% | **+1.64%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.44% | **+1.20%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 578件 (Win 149 / Loss 187 / Flat 242) / skip 715件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-22T18:03:57.718259+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=76744.3
- Funnel: target 765 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +72.90% | $31,108,664.48 |
| BILL/USDT:USDT | +9.62% | $13,147,491.53 |
| BEAT/USDT:USDT | +8.60% | $33,000,330.54 |
| GUA/USDT:USDT | +6.60% | $1,072,972.07 |
| PEAQ/USDT:USDT | +6.13% | $1,294,811.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.42% | +3.39% |
| PEAQ/USDT:USDT | below_1h_threshold | +2.93% | +2.89% |
| BSB/USDT:USDT | below_1h_threshold | +2.69% | +2.66% |
| NEX/USDT:USDT | below_1h_threshold | +0.68% | +0.64% |
| GUA/USDT:USDT | below_1h_threshold | +0.49% | +0.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
