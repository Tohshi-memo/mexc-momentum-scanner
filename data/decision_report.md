# Decision Report

- generated_at: 2026-11-06T12:16:40.315826+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18276**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18276, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +3.01% | **+1.05%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.18% | **+0.79%** |
| LIMIT_BB3S | 6/17 | 35.3% | +1.98% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.79% | **+3.19%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.26% | **+1.24%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.69% | **+1.10%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.37% | **+1.09%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.28% | **+1.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7802件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$377.48** / 初期 $100.00 (+277.48%)
- 確定: 4646件 (Win 1247 / Loss 1034 / Flat 2365) / skip 7041件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1473 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $377.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6439件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000284 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T12:16:22.269605+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=76122.9
- Funnel: target 1089 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +98.29% | $36,942,125.95 |
| UAI/USDT:USDT | +94.38% | $12,290,824.06 |
| CYBER/USDT:USDT | +64.42% | $5,181,845.85 |
| ONE/USDT:USDT | +35.55% | $2,178,325.73 |
| ICNT/USDT:USDT | +30.04% | $1,880,372.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +4.82% | +4.81% |
| SNXX/USDT:USDT | below_1h_threshold | +4.71% | +4.70% |
| INTW/USDT:USDT | below_1h_threshold | +3.35% | +3.34% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +3.20% | +3.19% |
| BTW/USDT:USDT | below_1h_threshold | +3.10% | +3.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
