# Decision Report

- generated_at: 2026-10-21T07:06:19.884244+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17102**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17102, expectancy=+0.02%
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
| LIMIT_ATR | 15/20 | 75.0% | +1.69% | **+1.27%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.28% | **+0.96%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.02% | **+0.86%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

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
- 確定: 6489件 (Win 1890 / Loss 2071 / Flat 2528) / skip 7174件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SMCISTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.60% 残高後 $1,352.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$279.61** / 初期 $100.00 (+179.61%)
- 確定: 3822件 (Win 1051 / Loss 893 / Flat 1878) / skip 6691件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $279.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5262件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000130 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-21T07:06:07.487995+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=82770.0
- Funnel: target 1084 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IOST/USDT:USDT | +38.77% | $3,645,004.64 |
| DOOD/USDT:USDT | +30.90% | $2,919,232.08 |
| ICNT/USDT:USDT | +26.92% | $5,110,576.22 |
| BIRB/USDT:USDT | +25.15% | $1,115,942.87 |
| CVX/USDT:USDT | +19.42% | $1,503,018.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +2.90% | +2.88% |
| DOOD/USDT:USDT | below_1h_threshold | +1.04% | +1.02% |
| COMP/USDT:USDT | below_1h_threshold | +0.89% | +0.87% |
| ICNT/USDT:USDT | below_1h_threshold | +0.66% | +0.64% |
| AKE/USDT:USDT | below_1h_threshold | +0.65% | +0.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
