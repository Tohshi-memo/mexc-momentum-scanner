# Decision Report

- generated_at: 2026-07-18T06:26:14.411986+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8916**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=8916, expectancy=+0.01%
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
| LIMIT_ATR | 10/20 | 50.0% | +2.76% | **+1.38%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.90% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.78%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.72% | **+0.78%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.57% | **+0.54%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$361.89** / 初期 $100.00 (+261.89%)
- 確定: 3031件 (Win 941 / Loss 965 / Flat 1125) / skip 2446件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.14% 残高後 $361.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.96** / 初期 $100.00 (+10.96%)
- 確定: 878件 (Win 206 / Loss 179 / Flat 493) / skip 1449件
- 成長率目線: 平均log +0.000118 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0119 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $110.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.75** / 初期 $100.00 (-0.25%)
- 確定: 174件 (Win 55 / Loss 92 / Flat 27) / pending 4件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.06% 残高後 $99.75

## 6. Latest Market Context

- 更新: 2026-07-18T06:26:07.739536+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63960.1
- Funnel: target 885 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +53.61% | $52,023,376.52 |
| ESPORTS/USDT:USDT | +37.79% | $13,192,365.07 |
| TRADOOR/USDT:USDT | +21.35% | $1,612,440.31 |
| BSB/USDT:USDT | +12.23% | $1,231,435.74 |
| VVV/USDT:USDT | +8.82% | $2,786,387.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.78% | +3.74% |
| GALA/USDT:USDT | below_1h_threshold | +2.54% | +2.50% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.44% | +2.40% |
| BASED/USDT:USDT | below_1h_threshold | +0.69% | +0.65% |
| JTO/USDT:USDT | below_1h_threshold | +0.62% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
