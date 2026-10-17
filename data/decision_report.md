# Decision Report

- generated_at: 2026-10-17T16:36:32.856551+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16901**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16901, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.93% | **+0.87%** |
| LIMIT_8PCT | 8/20 | 40.0% | +1.89% | **+0.76%** |
| LIMIT_9PCT | 7/20 | 35.0% | +1.88% | **+0.66%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,308.68** / 初期 $100.00 (+1208.68%)
- 確定: 6375件 (Win 1861 / Loss 2038 / Flat 2476) / skip 7087件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,308.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3690件 (Win 1027 / Loss 878 / Flat 1785) / skip 6622件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5066件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000125 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T16:36:17.381369+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81226.3
- Funnel: target 1084 → liquid 152 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.6 >= 65=1, 4h RSI 76.6 >= 65=1, 4h RSI 74.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +17.66% | $4,850,158.57 |
| ICNT/USDT:USDT | +14.52% | $11,876,740.78 |
| AGT/USDT:USDT | +10.39% | $21,144,704.70 |
| BTW/USDT:USDT | +4.75% | $28,627,032.16 |
| ZEREBRO/USDT:USDT | +4.50% | $1,006,446.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.50% | +4.61% |
| BTW/USDT:USDT | below_1h_threshold | +4.26% | +4.37% |
| BAT/USDT:USDT | below_1h_threshold | +3.74% | +3.85% |
| A/USDT:USDT | below_1h_threshold | +2.64% | +2.75% |
| SIREN/USDT:USDT | below_1h_threshold | +2.46% | +2.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
