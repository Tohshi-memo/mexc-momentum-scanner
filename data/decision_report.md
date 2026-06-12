# Decision Report

- generated_at: 2026-06-12T22:21:11.394652+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6547**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.82% / filled 20/20。**
- 全期間 MARKET基準: n=6547, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+4.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.82% | **+4.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.82% | **+4.82%** |
| ASK | 20/20 | 100.0% | +4.27% | **+4.27%** |
| LIMIT_1PCT | 14/20 | 70.0% | +3.79% | **+2.65%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.51% | **+2.11%** |
| LIMIT_ATR | 7/20 | 35.0% | +5.05% | **+1.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +3.11% | **+0.93%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.22% | **+0.36%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_8PCT_LONG | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | -1.91% | **-1.34%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$163.82** / 初期 $100.00 (+63.82%)
- 確定: 1420件 (Win 388 / Loss 462 / Flat 570) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $163.82

## 4. Latest Market Context

- 更新: 2026-06-12T22:21:08.547208+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63507.6
- Funnel: target 774 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +16.04% | $1,423,644.21 |
| ESPORTS/USDT:USDT | +13.31% | $69,683,859.83 |
| AIN/USDT:USDT | +11.27% | $1,779,240.44 |
| HOME/USDT:USDT | +6.93% | $2,670,065.54 |
| H/USDT:USDT | +6.56% | $29,557,952.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +2.82% | +2.73% |
| COAI/USDT:USDT | below_1h_threshold | +1.77% | +1.68% |
| AIN/USDT:USDT | below_1h_threshold | +1.67% | +1.57% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.53% | +1.44% |
| GRASS/USDT:USDT | below_1h_threshold | +1.02% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
