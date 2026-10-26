# Decision Report

- generated_at: 2026-10-26T02:01:24.147662+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17453**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=17453, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.04% | **+0.57%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.20% | **+0.13%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.09% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,542.22** / 初期 $100.00 (+1442.22%)
- 確定: 6706件 (Win 1952 / Loss 2143 / Flat 2611) / skip 7308件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,542.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$312.75** / 初期 $100.00 (+212.75%)
- 確定: 3996件 (Win 1109 / Loss 947 / Flat 1940) / skip 6868件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0454 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $312.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5613件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000285 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T02:01:11.734838+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=79682.9
- Funnel: target 1070 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +40.92% | $2,564,687.41 |
| CLAUDIA/USDT:USDT | +13.26% | $1,022,737.36 |
| BR/USDT:USDT | +9.35% | $7,030,911.52 |
| DODO/USDT:USDT | +7.78% | $1,010,915.28 |
| AXIS/USDT:USDT | +7.20% | $2,062,847.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KIMCHI/USDT:USDT | below_1h_threshold | +1.35% | +1.38% |
| UNITREE/USDT:USDT | below_1h_threshold | +1.11% | +1.15% |
| AXIS/USDT:USDT | below_1h_threshold | +0.50% | +0.54% |
| IRYS/USDT:USDT | below_1h_threshold | +0.47% | +0.51% |
| WINBONDSTOCK/USDT:USDT | below_1h_threshold | +0.27% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
