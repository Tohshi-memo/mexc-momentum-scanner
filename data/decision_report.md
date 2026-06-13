# Decision Report

- generated_at: 2026-06-13T06:41:28.901195+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6561**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.05% / filled 20/20。**
- 全期間 MARKET基準: n=6561, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |
| ASK | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.53% | **+0.76%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_ATR | 7/20 | 35.0% | +1.56% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.17% | **-0.15%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -1.10% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1434件 (Win 389 / Loss 464 / Flat 581) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T06:41:26.326676+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63645.4
- Funnel: target 774 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +47.04% | $1,712,398.18 |
| EDGE/USDT:USDT | +25.74% | $2,490,362.22 |
| VVV/USDT:USDT | +14.28% | $5,206,767.53 |
| SKYAI/USDT:USDT | +13.67% | $16,393,690.60 |
| SQD/USDT:USDT | +9.59% | $1,284,158.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.29% | +4.14% |
| VVV/USDT:USDT | below_1h_threshold | +3.02% | +2.88% |
| JUP/USDT:USDT | below_1h_threshold | +2.31% | +2.16% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.15% | +2.00% |
| RIF/USDT:USDT | below_1h_threshold | +1.98% | +1.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
