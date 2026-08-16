# Decision Report

- generated_at: 2026-08-16T06:21:25.858611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11718**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=11718, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.12% | **+1.90%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.24% | **+0.74%** |
| LIMIT_BB3S | 4/18 | 22.2% | +2.30% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.17% | **+0.70%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.67% | **+0.25%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.28% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4096件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.79** / 初期 $100.00 (+54.79%)
- 確定: 1771件 (Win 493 / Loss 416 / Flat 862) / skip 3358件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1564件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000120 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T06:21:17.272199+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63028.3
- Funnel: target 986 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +25.58% | $6,449,648.35 |
| H/USDT:USDT | +18.75% | $8,315,685.31 |
| SPORTFUN/USDT:USDT | +13.96% | $4,402,463.59 |
| BASED/USDT:USDT | +13.55% | $2,436,946.92 |
| CROSS/USDT:USDT | +13.01% | $1,201,175.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CROSS/USDT:USDT | below_1h_threshold | +1.62% | +1.62% |
| BICO/USDT:USDT | below_1h_threshold | +1.59% | +1.59% |
| AIO/USDT:USDT | below_1h_threshold | +1.57% | +1.58% |
| H/USDT:USDT | below_1h_threshold | +1.48% | +1.49% |
| CAP/USDT:USDT | below_1h_threshold | +1.48% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
