# Decision Report

- generated_at: 2026-06-13T08:43:01.890831+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6567**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=6567, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.77% | **+0.19%** |
| LIMIT_5PCT | 3/20 | 15.0% | +1.16% | **+0.17%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.07% | **+0.04%** |
| LIMIT_2PCT | 15/20 | 75.0% | -0.08% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.77% | **+0.31%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.26% | **+0.23%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.36% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1440件 (Win 389 / Loss 464 / Flat 587) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T08:42:58.142136+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=63871.8
- Funnel: target 774 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.7 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +49.60% | $3,310,869.81 |
| EDGE/USDT:USDT | +22.36% | $2,869,105.21 |
| RIF/USDT:USDT | +20.49% | $1,856,747.90 |
| SQD/USDT:USDT | +15.37% | $1,383,594.68 |
| VVV/USDT:USDT | +14.77% | $6,271,731.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.77% | +3.69% |
| OP/USDT:USDT | below_1h_threshold | +3.40% | +3.32% |
| SQD/USDT:USDT | below_1h_threshold | +3.14% | +3.06% |
| ORDI/USDT:USDT | below_1h_threshold | +1.91% | +1.83% |
| RENDER/USDT:USDT | below_1h_threshold | +1.04% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
