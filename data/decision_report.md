# Decision Report

- generated_at: 2026-10-21T06:56:38.680735+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17101**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17101, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.92% | **+1.44%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.95% | **+1.48%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.07% | **+1.38%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.04% | **+1.12%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.70% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 249件 (TP 92 / SL 150 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,352.02** / 初期 $100.00 (+1252.02%)
- 確定: 6489件 (Win 1890 / Loss 2071 / Flat 2528) / skip 7173件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SMCISTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.60% 残高後 $1,352.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.59** / 初期 $100.00 (+180.59%)
- 確定: 3821件 (Win 1051 / Loss 892 / Flat 1878) / skip 6691件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0494 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $280.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5261件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000195 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-21T06:56:21.104530+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=82782.2
- Funnel: target 1084 → liquid 168 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IOST/USDT:USDT | +39.42% | $3,572,017.11 |
| DOOD/USDT:USDT | +32.86% | $2,886,997.60 |
| ICNT/USDT:USDT | +25.20% | $5,123,917.12 |
| BIRB/USDT:USDT | +24.95% | $1,108,450.89 |
| CVX/USDT:USDT | +19.55% | $1,515,659.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +2.03% | +1.86% |
| QNT/USDT:USDT | below_1h_threshold | +1.85% | +1.67% |
| STRK/USDT:USDT | below_1h_threshold | +1.72% | +1.55% |
| IOST/USDT:USDT | below_1h_threshold | +1.55% | +1.37% |
| ZRO/USDT:USDT | below_1h_threshold | +1.55% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
