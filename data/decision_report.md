# Decision Report

- generated_at: 2026-05-14T15:28:19.402168+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4301**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4301, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +5.14% | **+1.54%** |
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.57% | **+0.90%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.92% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.46% | **+1.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.61** / 初期 $100.00 (+19.61%)
- 確定: 356件 (Win 95 / Loss 127 / Flat 134) / skip 506件
- 成長率目線: 平均log +0.000503 / 幾何平均 +0.050% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.61

## 4. Latest Market Context

- 更新: 2026-05-14T15:28:16.235105+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=80971.4
- Funnel: target 763 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +72.97% | $13,186,533.31 |
| PLAY/USDT:USDT | +33.87% | $3,507,534.58 |
| UP/USDT:USDT | +27.39% | $1,730,916.84 |
| GIGA/USDT:USDT | +27.16% | $1,153,073.10 |
| TROLLSOL/USDT:USDT | +26.77% | $2,261,599.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDSSTOCK/USDT:USDT | below_1h_threshold | +3.67% | +3.62% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +2.71% | +2.66% |
| PLAY/USDT:USDT | below_1h_threshold | +2.65% | +2.60% |
| RIVER/USDT:USDT | below_1h_threshold | +1.96% | +1.91% |
| UB/USDT:USDT | below_1h_threshold | +1.44% | +1.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
