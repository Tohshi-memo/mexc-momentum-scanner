# Decision Report

- generated_at: 2026-10-17T14:21:17.261190+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16879**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=16879, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.43% | **+0.39%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.49% | **+0.89%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.32% | **+0.27%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.21% | **+0.14%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.05% | **+0.03%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.54% | **-0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,265.35** / 初期 $100.00 (+1165.35%)
- 確定: 6353件 (Win 1855 / Loss 2033 / Flat 2465) / skip 7087件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,265.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3690件 (Win 1027 / Loss 878 / Flat 1785) / skip 6600件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0439 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5039件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000167 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T14:21:05.752321+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=81473.5
- Funnel: target 1084 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +95.45% | $20,034,533.12 |
| Q/USDT:USDT | +40.61% | $1,673,721.17 |
| EPIC/USDT:USDT | +29.60% | $1,620,675.34 |
| BTW/USDT:USDT | +24.44% | $23,824,673.86 |
| SAND/USDT:USDT | +17.43% | $14,115,366.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TMX/USDT:USDT | below_1h_threshold | +2.06% | +2.04% |
| LSK/USDT:USDT | below_1h_threshold | +1.73% | +1.72% |
| ICNT/USDT:USDT | below_1h_threshold | +1.50% | +1.49% |
| NIL/USDT:USDT | below_1h_threshold | +1.45% | +1.43% |
| SPX/USDT:USDT | below_1h_threshold | +1.31% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
