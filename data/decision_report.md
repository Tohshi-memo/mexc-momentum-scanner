# Decision Report

- generated_at: 2026-07-18T06:51:20.427609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8917**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=8917, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.88% | **+1.69%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.28% | **+1.14%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.21% | **+0.84%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.42% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.72% | **+0.78%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.45% | **+0.38%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.26% | **+0.24%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$361.89** / 初期 $100.00 (+261.89%)
- 確定: 3032件 (Win 941 / Loss 965 / Flat 1126) / skip 2446件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $361.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.96** / 初期 $100.00 (+10.96%)
- 確定: 879件 (Win 206 / Loss 179 / Flat 494) / skip 1449件
- 成長率目線: 平均log +0.000118 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0121 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $110.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.58** / 初期 $100.00 (-0.42%)
- 確定: 175件 (Win 55 / Loss 93 / Flat 27) / pending 6件 / skip 211件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.58

## 6. Latest Market Context

- 更新: 2026-07-18T06:51:12.409380+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63950.5
- Funnel: target 885 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.5 >= 65=1, 4h RSI 86.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +53.13% | $53,166,483.28 |
| ESPORTS/USDT:USDT | +42.85% | $13,663,503.36 |
| TRADOOR/USDT:USDT | +25.71% | $1,765,962.01 |
| BSB/USDT:USDT | +11.99% | $1,281,739.57 |
| VVV/USDT:USDT | +9.54% | $2,846,997.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.87% | +4.85% |
| STAR/USDT:USDT | below_1h_threshold | +4.63% | +4.61% |
| SYN/USDT:USDT | below_1h_threshold | +4.34% | +4.32% |
| GALA/USDT:USDT | below_1h_threshold | +3.15% | +3.13% |
| ZRO/USDT:USDT | below_1h_threshold | +1.20% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
