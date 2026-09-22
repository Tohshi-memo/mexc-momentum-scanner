# Decision Report

- generated_at: 2026-09-22T22:46:21.523899+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15369**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=15369, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +2.01% | **+1.71%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.16% | **+1.52%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.62% | **+1.44%** |
| LIMIT_BB3S | 7/14 | 50.0% | +2.41% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.91% | **+1.31%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.15% | **+0.86%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,155.82** / 初期 $100.00 (+1055.82%)
- 確定: 5847件 (Win 1729 / Loss 1880 / Flat 2238) / skip 6083件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,155.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5427件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.50** / 初期 $100.00 (+22.50%)
- 確定: 3117件 (Win 916 / Loss 1222 / Flat 979) / pending 4件 / skip 3724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000153 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PYTH/USDT:USDT `MARKET` EXPIRED account +0.22% 残高後 $122.50

## 6. Latest Market Context

- 更新: 2026-09-22T22:46:10.884809+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=86204.2
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUSEBOOK/USDT:USDT | +30.37% | $1,040,756.09 |
| DRIFT/USDT:USDT | +27.23% | $1,635,819.21 |
| FOLKS/USDT:USDT | +24.36% | $2,305,953.96 |
| 4/USDT:USDT | +18.73% | $2,308,921.60 |
| MUBARAK/USDT:USDT | +16.58% | $17,001,568.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.02% | +2.95% |
| ENA/USDT:USDT | below_1h_threshold | +2.94% | +2.87% |
| ARB/USDT:USDT | below_1h_threshold | +2.73% | +2.65% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.56% | +2.49% |
| ALLO/USDT:USDT | below_1h_threshold | +2.49% | +2.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
