# Decision Report

- generated_at: 2026-05-16T03:33:21.628022+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4365**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=4365, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.04% | **+0.62%** |
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.02% | **+0.56%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.38% | **-0.08%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.19% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 391件 (Win 97 / Loss 136 / Flat 158) / skip 535件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T03:33:18.371471+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79105.2
- Funnel: target 759 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +30.99% | $3,838,740.88 |
| ARCSOL/USDT:USDT | +28.47% | $1,490,872.35 |
| LAB/USDT:USDT | +22.00% | $151,764,114.72 |
| STORJ/USDT:USDT | +20.51% | $6,202,223.78 |
| GUA/USDT:USDT | +13.66% | $1,614,664.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +3.32% | +3.33% |
| LAB/USDT:USDT | below_1h_threshold | +1.71% | +1.72% |
| SIREN/USDT:USDT | below_1h_threshold | +1.40% | +1.41% |
| STORJ/USDT:USDT | below_1h_threshold | +1.13% | +1.14% |
| QNT/USDT:USDT | below_1h_threshold | +0.92% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
