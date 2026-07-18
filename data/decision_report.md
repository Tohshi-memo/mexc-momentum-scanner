# Decision Report

- generated_at: 2026-07-18T00:16:11.604723+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8900**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.78% / filled 20/20。**
- 全期間 MARKET基準: n=8900, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_BB3S | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.92% | **+0.65%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.39% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.49% | **+0.74%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.72% | **+0.47%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.44% | **+0.28%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$365.74** / 初期 $100.00 (+265.74%)
- 確定: 3015件 (Win 937 / Loss 958 / Flat 1120) / skip 2446件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $365.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$112.09** / 初期 $100.00 (+12.09%)
- 確定: 862件 (Win 203 / Loss 174 / Flat 485) / skip 1449件
- 成長率目線: 平均log +0.000132 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $112.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.45** / 初期 $100.00 (-0.55%)
- 確定: 158件 (Win 50 / Loss 85 / Flat 23) / pending 4件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.13% 残高後 $99.45

## 6. Latest Market Context

- 更新: 2026-07-18T00:16:05.151325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63945.5
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +52.41% | $10,145,713.70 |
| AKE/USDT:USDT | +23.00% | $48,832,800.00 |
| CASHCAT/USDT:USDT | +19.74% | $1,197,776.57 |
| CRO/USDT:USDT | +8.25% | $2,220,441.72 |
| VVV/USDT:USDT | +7.41% | $2,634,238.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.29% | +4.22% |
| PI/USDT:USDT | below_1h_threshold | +3.65% | +3.58% |
| TAG/USDT:USDT | below_1h_threshold | +0.90% | +0.84% |
| 0G/USDT:USDT | below_1h_threshold | +0.64% | +0.58% |
| ADA/USDT:USDT | below_1h_threshold | +0.60% | +0.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
