# Decision Report

- generated_at: 2026-08-12T00:51:39.377992+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11310**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=11310, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.01% | **+0.86%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.56% | **+0.50%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.89% | **+0.49%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.72% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.75% | **+0.83%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.77% | **+0.69%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.44%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.65% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3939件 (Win 1230 / Loss 1285 / Flat 1424) / skip 3932件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.95** / 初期 $100.00 (+43.95%)
- 確定: 1564件 (Win 437 / Loss 363 / Flat 764) / skip 3157件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.03** / 初期 $100.00 (+15.03%)
- 確定: 1332件 (Win 408 / Loss 525 / Flat 399) / pending 3件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +0.34% 残高後 $115.03

## 6. Latest Market Context

- 更新: 2026-08-12T00:51:25.809793+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=63714.0
- Funnel: target 967 → liquid 190 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1, 4h RSI 78.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +33.33% | $1,688,013.92 |
| HOLO/USDT:USDT | +19.66% | $3,955,778.90 |
| CRWVSTOCK/USDT:USDT | +16.75% | $3,720,318.97 |
| BMT/USDT:USDT | +16.36% | $2,856,665.77 |
| CAP/USDT:USDT | +15.39% | $8,392,577.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +3.57% | +3.35% |
| LIGHT/USDT:USDT | below_1h_threshold | +2.62% | +2.40% |
| LSK/USDT:USDT | below_1h_threshold | +2.53% | +2.31% |
| CRV/USDT:USDT | below_1h_threshold | +2.26% | +2.04% |
| GUA/USDT:USDT | below_1h_threshold | +2.05% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
