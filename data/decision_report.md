# Decision Report

- generated_at: 2026-05-20T01:03:40.794398+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4515**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4515, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +3.60% | **+1.44%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.06% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.30% | **+1.61%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.50% | **+0.90%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.03% | **+0.82%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.72% | **+0.82%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.54** / 初期 $100.00 (+24.54%)
- 確定: 478件 (Win 127 / Loss 165 / Flat 186) / skip 598件
- 成長率目線: 平均log +0.000459 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $124.54

## 4. Latest Market Context

- 更新: 2026-05-20T01:03:38.814467+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=76710.6
- Funnel: target 761 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +47.39% | $12,435,356.41 |
| EDEN/USDT:USDT | +25.20% | $17,112,657.33 |
| LIT/USDT:USDT | +18.49% | $4,569,749.36 |
| BANANAS31/USDT:USDT | +15.51% | $1,487,860.91 |
| BSB/USDT:USDT | +14.73% | $36,356,579.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +1.57% | +1.64% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.43% | +1.50% |
| PLAY/USDT:USDT | below_1h_threshold | +1.04% | +1.11% |
| BSB/USDT:USDT | below_1h_threshold | +0.61% | +0.68% |
| EDEN/USDT:USDT | below_1h_threshold | +0.60% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
