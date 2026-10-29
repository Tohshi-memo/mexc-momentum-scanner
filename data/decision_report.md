# Decision Report

- generated_at: 2026-10-29T14:46:22.401652+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17778**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=17778, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +2.06% | **+1.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.13% | **+1.01%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.85% | **+0.63%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.05% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.29% | **-0.14%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.82% | **-0.25%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.46% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6803件 (Win 1975 / Loss 2180 / Flat 2648) / skip 7536件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HYPE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.74** / 初期 $100.00 (+264.74%)
- 確定: 4299件 (Win 1164 / Loss 977 / Flat 2158) / skip 6890件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0133 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.08% 残高後 $364.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5939件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T14:46:11.037424+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.17% price=81217.3
- Funnel: target 1085 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +70.79% | $4,682,137.29 |
| BEAT/USDT:USDT | +26.19% | $17,317,810.06 |
| LSK/USDT:USDT | +23.67% | $1,177,602.53 |
| ON/USDT:USDT | +17.01% | $1,135,139.99 |
| UAI/USDT:USDT | +16.17% | $2,566,195.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CBRSSTOCK/USDT:USDT | below_1h_threshold | +4.63% | +3.46% |
| IDOL/USDT:USDT | below_1h_threshold | +4.17% | +2.99% |
| PEPE/USDT:USDT | below_1h_threshold | +3.69% | +2.52% |
| ZRO/USDT:USDT | below_1h_threshold | +3.29% | +2.11% |
| BEAT/USDT:USDT | below_1h_threshold | +2.80% | +1.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
