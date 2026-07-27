# Decision Report

- generated_at: 2026-07-27T08:06:25.286899+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9619**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9619, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.30% | **+1.11%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.79% | **+0.90%** |
| LIMIT_4PCT | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.09% | **+0.71%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.81% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 19/20 | 95.0% | +2.23% | **+2.12%** |
| LIMIT_BB3S_LONG | 13/16 | 81.2% | +2.04% | **+1.66%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.97% | **+1.08%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.25% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$450.42** / 初期 $100.00 (+350.42%)
- 確定: 3411件 (Win 1081 / Loss 1112 / Flat 1218) / skip 2769件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $450.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1807件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0057 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.08** / 初期 $100.00 (+8.08%)
- 確定: 643件 (Win 213 / Loss 245 / Flat 185) / pending 2件 / skip 443件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000221 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $108.08

## 6. Latest Market Context

- 更新: 2026-07-27T08:06:16.982194+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65182.9
- Funnel: target 901 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DIA/USDT:USDT | +40.88% | $8,768,119.14 |
| BTW/USDT:USDT | +31.50% | $2,264,713.39 |
| AKE/USDT:USDT | +28.08% | $34,001,191.32 |
| ON/USDT:USDT | +24.62% | $3,408,116.06 |
| NIL/USDT:USDT | +22.70% | $1,809,220.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DIA/USDT:USDT | below_1h_threshold | +2.87% | +2.89% |
| KAS/USDT:USDT | below_1h_threshold | +1.31% | +1.33% |
| KAITO/USDT:USDT | below_1h_threshold | +0.47% | +0.49% |
| ZRO/USDT:USDT | below_1h_threshold | +0.45% | +0.47% |
| OPENAI/USDT:USDT | below_1h_threshold | +0.28% | +0.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
