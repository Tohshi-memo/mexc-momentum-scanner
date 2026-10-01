# Decision Report

- generated_at: 2026-10-01T18:36:48.088252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15932**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=15932, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.40% | **+1.62%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.78% | **+1.33%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.20% | **+0.78%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.99% | **+0.64%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.15% | **+0.63%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,289.58** / 初期 $100.00 (+1189.58%)
- 確定: 6041件 (Win 1790 / Loss 1948 / Flat 2303) / skip 6452件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,289.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.86** / 初期 $100.00 (+176.86%)
- 確定: 3585件 (Win 999 / Loss 832 / Flat 1754) / skip 5758件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1146 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $276.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4099件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000336 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T18:36:28.064434+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=85015.5
- Funnel: target 1097 → liquid 171 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +14.94% | $6,133,046.77 |
| LONGXIA/USDT:USDT | +8.20% | $10,450,138.56 |
| MOVR/USDT:USDT | +7.99% | $26,194,642.68 |
| ZRO/USDT:USDT | +7.58% | $5,639,024.70 |
| USELESS/USDT:USDT | +6.34% | $3,431,112.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.61% | +3.44% |
| KORU/USDT:USDT | below_1h_threshold | +3.59% | +3.41% |
| SOXL/USDT:USDT | below_1h_threshold | +3.39% | +3.21% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.88% | +2.71% |
| ZRO/USDT:USDT | below_1h_threshold | +2.69% | +2.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
