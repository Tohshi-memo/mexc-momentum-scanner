# Decision Report

- generated_at: 2026-10-20T21:41:22.630955+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17079**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.91% / filled 20/20。**
- 全期間 MARKET基準: n=17079, expectancy=+0.02%
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
| LIMIT_1PCT | 19/20 | 95.0% | +2.01% | **+1.90%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.01% | **+0.71%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.93% | **+0.61%** |
| LIMIT_BB3S | 5/14 | 35.7% | +1.46% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.76% | **+0.08%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 248件 (TP 92 / SL 149 / EXP 7)
- 最新: USELESS/USDT:USDT TP_HIT PnL +7.06% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,332.81** / 初期 $100.00 (+1232.81%)
- 確定: 6487件 (Win 1888 / Loss 2071 / Flat 2528) / skip 7153件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COMP/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.65% 残高後 $1,332.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.10** / 初期 $100.00 (+180.10%)
- 確定: 3818件 (Win 1050 / Loss 892 / Flat 1876) / skip 6672件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0021 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $280.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5241件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000336 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T21:41:11.247641+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=82795.0
- Funnel: target 1084 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ICNT/USDT:USDT | +22.24% | $3,271,177.07 |
| SMCISTOCK/USDT:USDT | +14.52% | $1,005,878.94 |
| IOST/USDT:USDT | +13.71% | $1,046,636.28 |
| COMP/USDT:USDT | +8.75% | $2,893,814.54 |
| DOOD/USDT:USDT | +8.54% | $1,574,787.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +4.60% | +4.62% |
| KORU/USDT:USDT | below_1h_threshold | +4.50% | +4.52% |
| ZRO/USDT:USDT | below_1h_threshold | +4.40% | +4.42% |
| ICNT/USDT:USDT | below_1h_threshold | +4.24% | +4.26% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.10% | +4.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
