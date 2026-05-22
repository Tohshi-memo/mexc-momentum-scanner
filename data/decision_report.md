# Decision Report

- generated_at: 2026-05-22T01:53:52.308626+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4658**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.85% / filled 20/20。**
- 全期間 MARKET基準: n=4658, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |
| ASK | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.14% | **+0.91%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.48% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +1.63% | **+0.65%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.02% | **+0.02%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 547件 (Win 138 / Loss 185 / Flat 224) / skip 672件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPOTSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T01:53:47.035313+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=77562.4
- Funnel: target 766 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLUME/USDT:USDT | +14.96% | $1,635,343.73 |
| GRASS/USDT:USDT | +13.34% | $3,412,480.04 |
| NEAR/USDT:USDT | +11.79% | $47,903,549.77 |
| PEAQ/USDT:USDT | +10.11% | $1,911,968.23 |
| BILL/USDT:USDT | +8.93% | $15,211,844.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLUME/USDT:USDT | below_1h_threshold | +3.13% | +2.85% |
| VVV/USDT:USDT | below_1h_threshold | +2.33% | +2.05% |
| NEAR/USDT:USDT | below_1h_threshold | +2.07% | +1.79% |
| LIT/USDT:USDT | below_1h_threshold | +2.03% | +1.75% |
| JTO/USDT:USDT | below_1h_threshold | +1.97% | +1.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
