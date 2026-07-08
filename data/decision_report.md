# Decision Report

- generated_at: 2026-07-08T09:10:50.796619+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8472**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.03% / filled 20/20。**
- 全期間 MARKET基準: n=8472, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.03% | **+3.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.03% | **+3.03%** |
| ASK | 20/20 | 100.0% | +2.41% | **+2.41%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.19% | **+0.84%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.14% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.27% | **-0.09%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |
| ASK_LONG | 20/20 | 100.0% | -0.31% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$104.11** / 初期 $100.00 (+4.11%)
- 確定トレード: 74件 (TP 27 / SL 46 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT TP_HIT PnL +6.66% 残高後 $104.11
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.40** / 初期 $100.00 (+223.40%)
- 確定: 2677件 (Win 849 / Loss 898 / Flat 930) / skip 2356件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXL/USDT:USDT `LIMIT_FIB1272` TP_HIT account +1.00% 残高後 $323.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1242件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T09:10:45.778628+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=61924.7
- Funnel: target 847 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +52.58% | $67,359,513.16 |
| EDGE/USDT:USDT | +38.26% | $17,513,863.66 |
| SYN/USDT:USDT | +14.37% | $5,229,794.67 |
| KMNO/USDT:USDT | +13.18% | $1,122,813.50 |
| NES/USDT:USDT | +13.15% | $1,641,492.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +2.96% | +3.06% |
| EVAA/USDT:USDT | below_1h_threshold | +1.13% | +1.24% |
| CLO/USDT:USDT | below_1h_threshold | +1.11% | +1.22% |
| SLX/USDT:USDT | below_1h_threshold | +0.91% | +1.01% |
| DEXE/USDT:USDT | below_1h_threshold | +0.60% | +0.71% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
