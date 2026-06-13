# Decision Report

- generated_at: 2026-06-13T01:07:34.145211+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6554**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.82% / filled 20/20。**
- 全期間 MARKET基準: n=6554, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+3.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.82% | **+3.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.82% | **+3.82%** |
| ASK | 20/20 | 100.0% | +3.28% | **+3.28%** |
| LIMIT_ATR | 5/20 | 25.0% | +5.38% | **+1.34%** |
| LIMIT_1PCT | 12/20 | 60.0% | +1.92% | **+1.15%** |
| LIMIT_2PCT | 10/20 | 50.0% | +1.82% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.84% | **-0.21%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -1.56% | **-0.94%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$162.85** / 初期 $100.00 (+62.85%)
- 確定: 1427件 (Win 388 / Loss 464 / Flat 575) / skip 1688件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $162.85

## 4. Latest Market Context

- 更新: 2026-06-13T01:07:30.938251+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63607.5
- Funnel: target 774 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +18.68% | $63,999,016.25 |
| RIF/USDT:USDT | +16.53% | $1,116,629.15 |
| SQD/USDT:USDT | +13.76% | $1,006,160.23 |
| EDGE/USDT:USDT | +12.61% | $1,095,831.73 |
| ORCA/USDT:USDT | +10.90% | $1,668,645.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +2.56% | +2.50% |
| ORDI/USDT:USDT | below_1h_threshold | +0.78% | +0.72% |
| CHIP/USDT:USDT | below_1h_threshold | +0.74% | +0.68% |
| GRASS/USDT:USDT | below_1h_threshold | +0.72% | +0.66% |
| WLD/USDT:USDT | below_1h_threshold | +0.68% | +0.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
