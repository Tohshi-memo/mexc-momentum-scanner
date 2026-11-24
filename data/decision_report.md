# Decision Report

- generated_at: 2026-11-24T04:16:25.423320+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19552**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.02% / filled 20/20。**
- 全期間 MARKET基準: n=19552, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 12/20 | 60.0% | +1.97% | **+1.18%** |
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.45% | **+1.02%** |
| LIMIT_3PCT | 7/20 | 35.0% | +1.81% | **+0.63%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.01% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.53% | **+1.26%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.32% | **+0.70%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.88% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 286件 (TP 104 / SL 174 / EXP 8)
- 最新: NVD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,030.58** / 初期 $100.00 (+1930.58%)
- 確定: 7589件 (Win 2186 / Loss 2435 / Flat 2968) / skip 8524件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LISTA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $2,030.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7744件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7710件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000058 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-24T04:16:11.148201+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=60385.7
- Funnel: target 1088 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +42.64% | $1,229,892.59 |
| MMT/USDT:USDT | +21.35% | $3,229,498.25 |
| ARIA/USDT:USDT | +20.87% | $10,067,561.42 |
| NVD/USDT:USDT | +18.61% | $2,494,669.00 |
| LISTA/USDT:USDT | +16.15% | $1,325,242.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +3.04% | +2.92% |
| KORU/USDT:USDT | below_1h_threshold | +2.54% | +2.41% |
| ARIA/USDT:USDT | below_1h_threshold | +2.45% | +2.32% |
| NVD/USDT:USDT | below_1h_threshold | +1.52% | +1.39% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.27% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
