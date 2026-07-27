# Decision Report

- generated_at: 2026-07-27T07:36:16.558792+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9618**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9618, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.42% | **+1.21%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.88% | **+0.85%** |
| LIMIT_4PCT | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.01% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 19/20 | 95.0% | +2.19% | **+2.08%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.83% | **+1.47%** |
| LIMIT_BB3S_LONG | 14/17 | 82.4% | +1.61% | **+1.32%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.97% | **+1.08%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.25% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$450.42** / 初期 $100.00 (+350.42%)
- 確定: 3411件 (Win 1081 / Loss 1112 / Flat 1218) / skip 2768件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $450.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1806件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0081 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.71** / 初期 $100.00 (+7.71%)
- 確定: 642件 (Win 212 / Loss 245 / Flat 185) / pending 2件 / skip 443件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000156 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $107.71

## 6. Latest Market Context

- 更新: 2026-07-27T07:36:08.208166+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=65323.2
- Funnel: target 903 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +43.10% | $33,149,388.28 |
| BTW/USDT:USDT | +32.92% | $1,948,025.86 |
| DIA/USDT:USDT | +29.40% | $8,113,784.46 |
| ON/USDT:USDT | +20.47% | $4,062,274.76 |
| NIL/USDT:USDT | +14.41% | $1,755,441.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +2.85% | +2.95% |
| BTW/USDT:USDT | below_1h_threshold | +2.31% | +2.41% |
| EVAA/USDT:USDT | below_1h_threshold | +2.25% | +2.34% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.92% | +2.02% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.80% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
