# Decision Report

- generated_at: 2026-08-01T02:01:23.187403+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10045**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=10045, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.24% | **+1.79%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.83% | **+0.50%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.96% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.56% | **+0.39%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.49% | **+0.12%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.48% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.84** / 初期 $100.00 (+466.84%)
- 確定: 3597件 (Win 1150 / Loss 1178 / Flat 1269) / skip 3009件
- 成長率目線: 平均log +0.000482 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $566.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2177件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.58** / 初期 $100.00 (+11.58%)
- 確定: 865件 (Win 280 / Loss 343 / Flat 242) / pending 5件 / skip 649件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000186 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.58

## 6. Latest Market Context

- 更新: 2026-08-01T02:01:14.317140+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=62946.9
- Funnel: target 921 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +19.18% | $1,129,098.74 |
| BTW/USDT:USDT | +18.09% | $2,051,795.74 |
| GIGGLE/USDT:USDT | +13.78% | $22,528,824.01 |
| FLOW/USDT:USDT | +12.52% | $1,531,764.56 |
| TLM/USDT:USDT | +11.75% | $1,793,710.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KOMA/USDT:USDT | below_1h_threshold | +2.20% | +2.19% |
| BANK/USDT:USDT | below_1h_threshold | +1.26% | +1.26% |
| LAB/USDT:USDT | below_1h_threshold | +0.64% | +0.63% |
| DASH/USDT:USDT | below_1h_threshold | +0.54% | +0.54% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +0.54% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
