# Decision Report

- generated_at: 2026-10-26T08:51:29.674606+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17467**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.44% / filled 20/20。**
- 全期間 MARKET基準: n=17467, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.44% | **+2.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.44% | **+2.44%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.23% | **+2.01%** |
| LIMIT_ATR | 7/20 | 35.0% | +4.58% | **+1.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_BB3S | 3/18 | 16.7% | +5.27% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.15% | **+0.13%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,534.60** / 初期 $100.00 (+1434.60%)
- 確定: 6719件 (Win 1956 / Loss 2151 / Flat 2612) / skip 7309件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,534.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$313.75** / 初期 $100.00 (+213.75%)
- 確定: 4010件 (Win 1111 / Loss 950 / Flat 1949) / skip 6868件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0379 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DOOD/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $313.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5625件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000181 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T08:51:17.235789+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=80328.0
- Funnel: target 1072 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +69.65% | $1,216,756.97 |
| KIMCHI/USDT:USDT | +38.30% | $3,278,760.68 |
| DODO/USDT:USDT | +12.51% | $1,339,862.72 |
| BR/USDT:USDT | +9.96% | $9,366,850.51 |
| PHA/USDT:USDT | +5.52% | $1,103,137.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KIMCHI/USDT:USDT | below_1h_threshold | +4.16% | +3.75% |
| SPX/USDT:USDT | below_1h_threshold | +3.80% | +3.39% |
| TIA/USDT:USDT | below_1h_threshold | +3.00% | +2.59% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.85% | +2.44% |
| AKE/USDT:USDT | below_1h_threshold | +2.82% | +2.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
