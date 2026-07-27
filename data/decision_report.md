# Decision Report

- generated_at: 2026-07-27T08:56:23.857351+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9620**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9620, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.29% | **+1.14%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.30% | **+1.11%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.55% | **+1.01%** |
| LIMIT_4PCT | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.81% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.91% | **+1.72%** |
| LIMIT_BB3S_LONG | 12/15 | 80.0% | +1.54% | **+1.23%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.97% | **+1.08%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.25% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$450.42** / 初期 $100.00 (+350.42%)
- 確定: 3412件 (Win 1081 / Loss 1112 / Flat 1219) / skip 2769件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $450.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1808件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0031 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.08** / 初期 $100.00 (+8.08%)
- 確定: 644件 (Win 213 / Loss 245 / Flat 186) / pending 4件 / skip 445件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000240 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.08

## 6. Latest Market Context

- 更新: 2026-07-27T08:56:15.682559+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=65155.1
- Funnel: target 901 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1, 4h RSI 91.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +45.56% | $37,609,021.87 |
| DIA/USDT:USDT | +44.07% | $9,792,267.21 |
| ON/USDT:USDT | +34.80% | $3,701,005.31 |
| BTW/USDT:USDT | +30.15% | $2,601,432.78 |
| TAG/USDT:USDT | +19.39% | $1,044,210.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.86% | +4.93% |
| TAG/USDT:USDT | below_1h_threshold | +2.77% | +2.83% |
| ZRO/USDT:USDT | below_1h_threshold | +2.14% | +2.20% |
| BANK/USDT:USDT | below_1h_threshold | +2.08% | +2.14% |
| KAS/USDT:USDT | below_1h_threshold | +1.59% | +1.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
