# Decision Report

- generated_at: 2026-06-07T16:10:17.461211+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5976**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5976, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.11% | **-2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.90% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.85% | **+2.28%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.12% | **+2.27%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.29% | **+2.14%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.05% | **+2.02%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.82% | **+1.72%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.72** / 初期 $100.00 (+47.72%)
- 確定: 1093件 (Win 264 / Loss 329 / Flat 500) / skip 1444件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $147.72

## 4. Latest Market Context

- 更新: 2026-06-07T16:10:14.508453+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=61989.7
- Funnel: target 768 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIPPIN/USDT:USDT | +4.13% | $1,747,295.86 |
| RAVE/USDT:USDT | +4.09% | $1,811,239.63 |
| ESPORTS/USDT:USDT | +3.89% | $3,097,337.08 |
| VELVET/USDT:USDT | +3.61% | $2,133,020.19 |
| SKYAI/USDT:USDT | +2.84% | $45,349,671.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +4.14% | +4.27% |
| RAVE/USDT:USDT | below_1h_threshold | +3.80% | +3.93% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.70% | +3.83% |
| VELVET/USDT:USDT | below_1h_threshold | +3.09% | +3.22% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.72% | +2.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
