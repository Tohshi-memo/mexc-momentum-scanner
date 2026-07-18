# Decision Report

- generated_at: 2026-07-18T09:11:13.003180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8926**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.77% / filled 20/20。**
- 全期間 MARKET基準: n=8926, expectancy=+0.01%
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
| LIMIT_1PCT | 17/20 | 85.0% | +0.97% | **+0.82%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.52% | **+0.50%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.54% | **+0.33%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.47% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.34% | **+0.61%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.63% | **+0.28%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.26% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$111.25** / 初期 $100.00 (+11.25%)
- 確定トレード: 115件 (TP 43 / SL 68 / EXP 4)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $111.25
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$365.92** / 初期 $100.00 (+265.92%)
- 確定: 3041件 (Win 944 / Loss 967 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XEC/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $365.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.42** / 初期 $100.00 (+10.42%)
- 確定: 888件 (Win 209 / Loss 181 / Flat 498) / skip 1449件
- 成長率目線: 平均log +0.000112 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0135 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $110.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.08** / 初期 $100.00 (+0.08%)
- 確定: 181件 (Win 58 / Loss 96 / Flat 27) / pending 4件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000423 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $100.08

## 6. Latest Market Context

- 更新: 2026-07-18T09:11:06.453665+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63950.7
- Funnel: target 885 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +57.18% | $59,176,755.00 |
| TRADOOR/USDT:USDT | +33.47% | $3,323,376.26 |
| ESPORTS/USDT:USDT | +28.05% | $14,220,999.60 |
| XEC/USDT:USDT | +16.23% | $3,658,692.17 |
| BSB/USDT:USDT | +13.33% | $1,382,225.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.47% | +4.51% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.98% | +2.02% |
| XEC/USDT:USDT | below_1h_threshold | +0.97% | +1.01% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +0.81% | +0.86% |
| CASHCAT/USDT:USDT | below_1h_threshold | +0.40% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
