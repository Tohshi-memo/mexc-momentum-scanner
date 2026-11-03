# Decision Report

- generated_at: 2026-11-03T03:46:27.955379+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18055**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.56% / filled 20/20。**
- 全期間 MARKET基準: n=18055, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.56% | **+2.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.56% | **+2.56%** |
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.58% | **+1.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.63% | **+0.22%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.33% | **+0.21%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.23% | **-0.14%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.58% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 260件 (TP 96 / SL 156 / EXP 8)
- 最新: EVAA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,521.09** / 初期 $100.00 (+1421.09%)
- 確定: 6907件 (Win 2000 / Loss 2216 / Flat 2691) / skip 7709件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,521.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.70** / 初期 $100.00 (+281.70%)
- 確定: 4483件 (Win 1204 / Loss 1000 / Flat 2279) / skip 6983件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0485 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $381.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6215件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000272 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-03T03:46:14.511799+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=76775.2
- Funnel: target 1093 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +33.02% | $3,984,307.04 |
| IDOL/USDT:USDT | +28.64% | $17,466,463.17 |
| ICNT/USDT:USDT | +11.58% | $1,044,285.76 |
| JCT/USDT:USDT | +10.95% | $2,505,955.84 |
| EVAA/USDT:USDT | +10.73% | $7,184,619.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOT/USDT:USDT | below_1h_threshold | +2.25% | +2.14% |
| EVAA/USDT:USDT | below_1h_threshold | +1.76% | +1.65% |
| SOXS/USDT:USDT | below_1h_threshold | +1.01% | +0.90% |
| IDOL/USDT:USDT | below_1h_threshold | +0.99% | +0.88% |
| XMR/USDT:USDT | below_1h_threshold | +0.90% | +0.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
