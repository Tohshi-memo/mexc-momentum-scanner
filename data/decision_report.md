# Decision Report

- generated_at: 2026-11-22T06:01:12.316907+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19360**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19360, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/17 | 58.8% | +2.66% | **+1.56%** |
| LIMIT_4PCT | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_5PCT | 9/20 | 45.0% | +2.20% | **+0.99%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +2.52% | **+2.27%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.76% | **+1.67%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.29% | **+1.37%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.64% | **+1.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,778.01** / 初期 $100.00 (+1678.01%)
- 確定: 7481件 (Win 2149 / Loss 2408 / Flat 2924) / skip 8440件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ENSO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,778.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$451.30** / 初期 $100.00 (+351.30%)
- 確定: 5125件 (Win 1364 / Loss 1100 / Flat 2661) / skip 7646件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0285 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $451.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7519件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000351 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T06:01:01.431206+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=58978.3
- Funnel: target 1086 → liquid 112 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +34.48% | $2,189,276.23 |
| DCTY/USDT:USDT | +23.01% | $1,675,485.26 |
| BLESS/USDT:USDT | +19.05% | $58,362,610.37 |
| PIEVERSE/USDT:USDT | +16.93% | $5,954,357.04 |
| SKYAI/USDT:USDT | +13.44% | $1,602,459.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DCTY/USDT:USDT | below_1h_threshold | +0.56% | +0.43% |
| BLESS/USDT:USDT | below_1h_threshold | +0.49% | +0.35% |
| SOXL/USDT:USDT | below_1h_threshold | +0.46% | +0.33% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.42% | +0.29% |
| JUP/USDT:USDT | below_1h_threshold | +0.42% | +0.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
