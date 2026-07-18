# Decision Report

- generated_at: 2026-07-18T05:41:11.425369+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8915**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.80% / filled 20/20。**
- 全期間 MARKET基準: n=8915, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.80% | **+1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.76% | **+1.38%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.80% | **+1.35%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.43% | **+1.29%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.90% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.35% | **+1.18%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +0.66% | **+0.59%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.42% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.25% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$362.40** / 初期 $100.00 (+262.40%)
- 確定: 3030件 (Win 941 / Loss 964 / Flat 1125) / skip 2446件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $362.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.96** / 初期 $100.00 (+10.96%)
- 確定: 877件 (Win 206 / Loss 179 / Flat 492) / skip 1449件
- 成長率目線: 平均log +0.000119 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0119 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $110.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.81** / 初期 $100.00 (-0.19%)
- 確定: 173件 (Win 55 / Loss 91 / Flat 27) / pending 4件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.81

## 6. Latest Market Context

- 更新: 2026-07-18T05:41:06.008519+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63932.8
- Funnel: target 885 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +62.43% | $12,548,364.94 |
| AKE/USDT:USDT | +39.48% | $50,550,070.86 |
| TRADOOR/USDT:USDT | +18.31% | $1,495,110.45 |
| BSB/USDT:USDT | +9.23% | $1,162,719.46 |
| VVV/USDT:USDT | +8.70% | $2,815,053.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.31% | +4.33% |
| XEC/USDT:USDT | below_1h_threshold | +3.10% | +3.13% |
| JASMY/USDT:USDT | below_1h_threshold | +2.08% | +2.10% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +2.08% | +2.10% |
| BASED/USDT:USDT | below_1h_threshold | +1.08% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
