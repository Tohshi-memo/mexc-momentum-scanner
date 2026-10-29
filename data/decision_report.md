# Decision Report

- generated_at: 2026-10-29T15:51:42.139737+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17781**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=17781, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.52% | **+0.83%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.77% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.23% | **+0.21%** |
| LIMIT_5PCT | 3/20 | 15.0% | +1.20% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.48% | **+0.26%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.24% | **+0.13%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.08% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6803件 (Win 1975 / Loss 2180 / Flat 2648) / skip 7539件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HYPE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.74** / 初期 $100.00 (+264.74%)
- 確定: 4302件 (Win 1164 / Loss 977 / Flat 2161) / skip 6890件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0062 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $364.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5946件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T15:51:25.576302+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.62% price=81649.2
- Funnel: target 1086 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1, 4h RSI 74.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +76.55% | $5,033,847.25 |
| BEAT/USDT:USDT | +28.46% | $21,908,762.91 |
| LSK/USDT:USDT | +26.82% | $2,394,558.46 |
| APR/USDT:USDT | +21.36% | $3,489,299.59 |
| HYPE/USDT:USDT | +17.78% | $157,964,343.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_relative_strength | +5.49% | +4.87% |
| VVV/USDT:USDT | below_1h_threshold | +4.82% | +4.21% |
| LIT/USDT:USDT | below_1h_threshold | +4.64% | +4.02% |
| HYPE/USDT:USDT | below_1h_threshold | +3.35% | +2.73% |
| ZEC/USDT:USDT | below_1h_threshold | +3.02% | +2.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
