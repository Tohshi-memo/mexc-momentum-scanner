# Decision Report

- generated_at: 2026-05-20T22:28:52.532070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4583**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4583, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_9PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |
| LIMIT_10PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |
| LIMIT_5PCT | 11/20 | 55.0% | -1.11% | **-0.61%** |
| LIMIT_6PCT | 9/20 | 45.0% | -1.36% | **-0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +6.22% | **+3.89%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.49% | **+2.37%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.87** / 初期 $100.00 (+23.87%)
- 確定: 541件 (Win 138 / Loss 181 / Flat 222) / skip 603件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $123.87

## 4. Latest Market Context

- 更新: 2026-05-20T22:28:50.503587+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=77397.0
- Funnel: target 758 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +37.52% | $27,319,990.22 |
| FIDA/USDT:USDT | +21.59% | $10,865,474.10 |
| NIL/USDT:USDT | +16.61% | $2,585,387.17 |
| JTO/USDT:USDT | +10.31% | $2,554,639.61 |
| BANANAS31/USDT:USDT | +10.07% | $4,119,369.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HYPE/USDT:USDT | below_1h_threshold | +1.82% | +1.90% |
| LIT/USDT:USDT | below_1h_threshold | +1.24% | +1.33% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.88% | +0.97% |
| EDEN/USDT:USDT | below_1h_threshold | +0.86% | +0.95% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.84% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
