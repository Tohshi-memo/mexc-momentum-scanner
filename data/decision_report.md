# Decision Report

- generated_at: 2026-10-11T10:11:11.685147+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16549**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16549, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.47% | **+0.17%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.90% | **-0.36%** |
| LIMIT_FIB1272 | 13/20 | 65.0% | -0.70% | **-0.46%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.66% | **-0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.38% | **+2.25%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.68% | **+2.14%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.01% | **+1.81%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.84% | **+1.57%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.24% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,298.24** / 初期 $100.00 (+1198.24%)
- 確定: 6289件 (Win 1845 / Loss 2015 / Flat 2429) / skip 6821件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGIC/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,298.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$273.08** / 初期 $100.00 (+173.08%)
- 確定: 3637件 (Win 1010 / Loss 854 / Flat 1773) / skip 6323件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $273.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4710件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000211 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-11T10:11:00.640943+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=83013.1
- Funnel: target 1087 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +51.71% | $7,096,456.93 |
| CHIP/USDT:USDT | +26.47% | $39,592,302.39 |
| MAGIC/USDT:USDT | +23.91% | $16,481,133.78 |
| SI/USDT:USDT | +23.76% | $2,132,605.52 |
| BATON/USDT:USDT | +19.91% | $1,745,892.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +2.07% | +2.05% |
| RLC/USDT:USDT | below_1h_threshold | +1.87% | +1.86% |
| ZEC/USDT:USDT | below_1h_threshold | +0.39% | +0.38% |
| FLOW/USDT:USDT | below_1h_threshold | +0.37% | +0.36% |
| BAT/USDT:USDT | below_1h_threshold | +0.33% | +0.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
