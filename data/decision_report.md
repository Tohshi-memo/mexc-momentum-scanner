# Decision Report

- generated_at: 2026-07-16T09:36:21.457722+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8795**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=8795, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_BB3S | 6/13 | 46.2% | +1.72% | **+0.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.78% | **+0.70%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.64% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.59% | **+0.41%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.39% | **+0.27%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.32% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$107.41** / 初期 $100.00 (+7.41%)
- 確定トレード: 103件 (TP 38 / SL 63 / EXP 2)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$336.75** / 初期 $100.00 (+236.75%)
- 確定: 2910件 (Win 907 / Loss 945 / Flat 1058) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $336.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.05** / 初期 $100.00 (+7.05%)
- 確定: 757件 (Win 172 / Loss 169 / Flat 416) / skip 1449件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0320 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.48** / 初期 $100.00 (-1.52%)
- 確定: 67件 (Win 20 / Loss 43 / Flat 4) / pending 2件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000486 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.48

## 6. Latest Market Context

- 更新: 2026-07-16T09:36:10.655946+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64079.9
- Funnel: target 875 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +20.78% | $5,824,608.30 |
| CAP/USDT:USDT | +16.65% | $2,878,876.91 |
| US/USDT:USDT | +15.24% | $15,523,851.86 |
| AKE/USDT:USDT | +13.65% | $44,619,622.65 |
| BANK/USDT:USDT | +11.78% | $2,515,366.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.25% | +4.28% |
| BASED/USDT:USDT | below_1h_threshold | +3.35% | +3.38% |
| AKE/USDT:USDT | below_1h_threshold | +2.62% | +2.64% |
| RAVE/USDT:USDT | below_1h_threshold | +2.31% | +2.34% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +1.54% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
