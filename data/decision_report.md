# Decision Report

- generated_at: 2026-11-22T08:51:27.375687+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19368**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=19368, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/19 | 52.6% | +3.25% | **+1.71%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.38% | **+1.31%** |
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.37% | **+1.03%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.67% | **+1.17%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.01% | **+0.70%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.15% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,776.95** / 初期 $100.00 (+1676.95%)
- 確定: 7482件 (Win 2149 / Loss 2409 / Flat 2924) / skip 8447件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.06% 残高後 $1,776.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$449.65** / 初期 $100.00 (+349.65%)
- 確定: 5132件 (Win 1365 / Loss 1103 / Flat 2664) / skip 7647件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0500 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $449.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7528件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000339 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T08:51:13.470937+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.96% price=59710.0
- Funnel: target 1086 → liquid 107 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +42.44% | $2,331,900.93 |
| PIEVERSE/USDT:USDT | +37.96% | $9,677,049.84 |
| BLESS/USDT:USDT | +24.00% | $57,633,472.02 |
| BTW/USDT:USDT | +13.81% | $5,640,533.85 |
| SKYAI/USDT:USDT | +9.46% | $2,187,303.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.75% | +3.80% |
| BLESS/USDT:USDT | below_1h_threshold | +3.40% | +2.44% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.44% | +1.49% |
| TIA/USDT:USDT | below_1h_threshold | +2.06% | +1.11% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.96% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
