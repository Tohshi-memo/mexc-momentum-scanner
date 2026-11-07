# Decision Report

- generated_at: 2026-11-07T00:46:29.195692+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18335**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=18335, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.04% | **+0.99%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.59% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.81% | **+0.69%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.22% | **+0.56%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.63% | **+0.54%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,480.69** / 初期 $100.00 (+1380.69%)
- 確定: 7036件 (Win 2023 / Loss 2247 / Flat 2766) / skip 7860件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $1,480.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$392.10** / 初期 $100.00 (+292.10%)
- 確定: 4705件 (Win 1266 / Loss 1037 / Flat 2402) / skip 7041件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0488 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $392.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6498件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T00:46:11.523349+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=75884.1
- Funnel: target 1089 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +21.26% | $11,994,453.17 |
| AIN/USDT:USDT | +15.60% | $4,901,736.81 |
| BTW/USDT:USDT | +8.33% | $7,458,026.18 |
| IDOL/USDT:USDT | +6.85% | $4,788,292.70 |
| JCT/USDT:USDT | +6.85% | $5,220,106.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +4.44% | +4.34% |
| AKE/USDT:USDT | below_1h_threshold | +1.71% | +1.62% |
| ALGO/USDT:USDT | below_1h_threshold | +1.56% | +1.46% |
| INJ/USDT:USDT | below_1h_threshold | +1.51% | +1.41% |
| XPL/USDT:USDT | below_1h_threshold | +1.21% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
