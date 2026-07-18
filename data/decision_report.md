# Decision Report

- generated_at: 2026-07-18T07:31:10.174581+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8919**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.13% / filled 20/20。**
- 全期間 MARKET基準: n=8919, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.13% | **+1.07%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.61% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.16% | **+0.98%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.91% | **+0.68%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.94% | **+0.38%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$111.81** / 初期 $100.00 (+11.81%)
- 確定トレード: 114件 (TP 43 / SL 67 / EXP 4)
- 最新: ALLO/USDT:USDT SL_HIT PnL -3.65% 残高後 $111.81
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$365.51** / 初期 $100.00 (+265.51%)
- 確定: 3034件 (Win 942 / Loss 965 / Flat 1127) / skip 2446件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $365.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.04** / 初期 $100.00 (+11.04%)
- 確定: 881件 (Win 207 / Loss 179 / Flat 495) / skip 1449件
- 成長率目線: 平均log +0.000119 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0103 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $111.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.40** / 初期 $100.00 (-0.60%)
- 確定: 176件 (Win 55 / Loss 94 / Flat 27) / pending 5件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.40

## 6. Latest Market Context

- 更新: 2026-07-18T07:31:03.694527+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63981.3
- Funnel: target 885 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +55.42% | $54,383,402.59 |
| ESPORTS/USDT:USDT | +36.67% | $13,864,813.43 |
| TRADOOR/USDT:USDT | +32.10% | $2,255,188.26 |
| BSB/USDT:USDT | +12.07% | $1,301,169.89 |
| VVV/USDT:USDT | +11.08% | $2,922,898.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STAR/USDT:USDT | below_1h_threshold | +4.46% | +4.42% |
| TRADOOR/USDT:USDT | below_1h_threshold | +4.30% | +4.26% |
| AKE/USDT:USDT | below_1h_threshold | +1.66% | +1.62% |
| EGLD/USDT:USDT | below_1h_threshold | +1.07% | +1.03% |
| ALLO/USDT:USDT | below_1h_threshold | +0.78% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
