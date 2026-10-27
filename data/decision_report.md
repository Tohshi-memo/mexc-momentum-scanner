# Decision Report

- generated_at: 2026-10-27T16:06:45.360317+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17617**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17617, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.89% | **+1.79%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.36% | **+1.77%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.31% | **+0.92%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.43% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 254件 (TP 94 / SL 152 / EXP 8)
- 最新: APR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,538.53** / 初期 $100.00 (+1438.53%)
- 確定: 6726件 (Win 1958 / Loss 2153 / Flat 2615) / skip 7452件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,538.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$338.84** / 初期 $100.00 (+238.84%)
- 確定: 4146件 (Win 1133 / Loss 961 / Flat 2052) / skip 6882件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0635 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $338.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5779件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000259 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T16:06:27.623413+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80511.1
- Funnel: target 1083 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +14.55% | $10,274,246.16 |
| AKE/USDT:USDT | +6.39% | $3,881,605.26 |
| CBRSSTOCK/USDT:USDT | +4.09% | $1,490,979.19 |
| APR/USDT:USDT | +2.84% | $3,083,519.23 |
| BCH/USDT:USDT | +1.92% | $3,683,101.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +3.42% | +3.44% |
| SOXL/USDT:USDT | below_1h_threshold | +2.84% | +2.86% |
| BCH/USDT:USDT | below_1h_threshold | +1.92% | +1.95% |
| AIN/USDT:USDT | below_1h_threshold | +1.66% | +1.69% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.55% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
