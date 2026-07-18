# Decision Report

- generated_at: 2026-07-18T08:46:16.281952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8925**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.77% / filled 20/20。**
- 全期間 MARKET基準: n=8925, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.77% | **+1.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.03% | **+0.87%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.28% | **+0.46%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.61% | **+0.43%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.54% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.34% | **+0.61%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.63% | **+0.28%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.15% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$111.25** / 初期 $100.00 (+11.25%)
- 確定トレード: 115件 (TP 43 / SL 68 / EXP 4)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $111.25
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$365.49** / 初期 $100.00 (+265.49%)
- 確定: 3040件 (Win 943 / Loss 967 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $365.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.34** / 初期 $100.00 (+10.34%)
- 確定: 887件 (Win 208 / Loss 181 / Flat 498) / skip 1449件
- 成長率目線: 平均log +0.000111 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0109 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $110.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.25** / 初期 $100.00 (+0.25%)
- 確定: 180件 (Win 58 / Loss 95 / Flat 27) / pending 5件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000423 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $100.25

## 6. Latest Market Context

- 更新: 2026-07-18T08:46:08.476611+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63957.0
- Funnel: target 885 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +44.24% | $59,349,377.04 |
| ESPORTS/USDT:USDT | +34.70% | $14,134,738.80 |
| TRADOOR/USDT:USDT | +30.11% | $3,091,627.65 |
| BSB/USDT:USDT | +12.47% | $1,365,364.76 |
| VVV/USDT:USDT | +10.56% | $3,054,018.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STAR/USDT:USDT | below_1h_threshold | +4.03% | +4.06% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.73% | +3.77% |
| BULLA/USDT:USDT | below_1h_threshold | +3.20% | +3.23% |
| ALLO/USDT:USDT | below_1h_threshold | +3.09% | +3.13% |
| LAB/USDT:USDT | below_1h_threshold | +0.46% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
