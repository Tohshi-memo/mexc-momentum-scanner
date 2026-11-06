# Decision Report

- generated_at: 2026-11-06T23:16:08.638597+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18333**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.52% / filled 20/20。**
- 全期間 MARKET基準: n=18333, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.62% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.52% | **+1.29%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.87% | **+1.03%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.22% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.37% | **+0.34%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7859件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.82** / 初期 $100.00 (+291.82%)
- 確定: 4703件 (Win 1265 / Loss 1037 / Flat 2401) / skip 7041件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0462 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MRNASTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $391.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6495件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T23:16:00.163463+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=75873.3
- Funnel: target 1089 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +23.17% | $8,977,080.62 |
| IDOL/USDT:USDT | +11.76% | $4,611,273.51 |
| BTW/USDT:USDT | +9.86% | $7,479,779.42 |
| UVXY/USDT:USDT | +6.40% | $2,705,159.69 |
| CLSKSTOCK/USDT:USDT | +5.88% | $1,067,292.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +2.87% | +2.87% |
| BTW/USDT:USDT | below_1h_threshold | +1.29% | +1.29% |
| BEAT/USDT:USDT | below_1h_threshold | +0.90% | +0.90% |
| XTZ/USDT:USDT | below_1h_threshold | +0.72% | +0.72% |
| UVXY/USDT:USDT | below_1h_threshold | +0.31% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
