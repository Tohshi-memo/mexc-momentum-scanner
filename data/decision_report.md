# Decision Report

- generated_at: 2026-09-26T16:11:31.450774+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15605**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=15605, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.63% | **+0.48%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.37% | **+0.41%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.38% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.82% | **+1.41%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.76% | **+1.14%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.22% | **+1.11%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.01% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,266.13** / 初期 $100.00 (+1166.13%)
- 確定: 5966件 (Win 1764 / Loss 1916 / Flat 2286) / skip 6200件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,266.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5483件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1092 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.64** / 初期 $100.00 (+19.64%)
- 確定: 3190件 (Win 939 / Loss 1264 / Flat 987) / pending 6件 / skip 3883件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000373 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.64

## 6. Latest Market Context

- 更新: 2026-09-26T16:11:17.933107+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=84103.0
- Funnel: target 1070 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.3 >= 65=1, 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +6.97% | $3,154,971.99 |
| ORDI/USDT:USDT | +5.25% | $2,363,685.86 |
| GRASS/USDT:USDT | +2.11% | $3,033,287.66 |
| FLOW/USDT:USDT | +1.79% | $1,245,329.52 |
| WLD/USDT:USDT | +1.69% | $69,680,127.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +2.11% | +2.12% |
| FLOW/USDT:USDT | below_1h_threshold | +1.88% | +1.89% |
| WLD/USDT:USDT | below_1h_threshold | +1.66% | +1.67% |
| BTW/USDT:USDT | below_1h_threshold | +1.48% | +1.49% |
| CC/USDT:USDT | below_1h_threshold | +1.35% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
