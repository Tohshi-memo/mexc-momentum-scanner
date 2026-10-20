# Decision Report

- generated_at: 2026-10-20T18:36:28.290636+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17077**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.91% / filled 20/20。**
- 全期間 MARKET基準: n=17077, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.91% | **+1.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.91% | **+1.91%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.67% | **+1.50%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.41% | **+0.26%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.34% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -1.09% | **-0.54%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 248件 (TP 92 / SL 149 / EXP 7)
- 最新: USELESS/USDT:USDT TP_HIT PnL +7.06% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,332.81** / 初期 $100.00 (+1232.81%)
- 確定: 6487件 (Win 1888 / Loss 2071 / Flat 2528) / skip 7151件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COMP/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.65% 残高後 $1,332.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.10** / 初期 $100.00 (+180.10%)
- 確定: 3818件 (Win 1050 / Loss 892 / Flat 1876) / skip 6670件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0023 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $280.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5239件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000328 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T18:36:15.782461+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=82498.7
- Funnel: target 1084 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +14.61% | $1,377,932.00 |
| ICNT/USDT:USDT | +13.19% | $1,512,452.94 |
| APR/USDT:USDT | +11.59% | $1,900,945.33 |
| COMP/USDT:USDT | +6.58% | $2,454,153.77 |
| DNA/USDT:USDT | +5.14% | $1,712,957.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DNA/USDT:USDT | below_1h_threshold | +1.76% | +2.10% |
| APR/USDT:USDT | below_1h_threshold | +1.53% | +1.87% |
| ICNT/USDT:USDT | below_1h_threshold | +1.43% | +1.77% |
| DOOD/USDT:USDT | below_1h_threshold | +1.41% | +1.75% |
| COMP/USDT:USDT | below_1h_threshold | +1.36% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
