# Decision Report

- generated_at: 2026-07-31T08:01:21.550595+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9976**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9976, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.44% | **+0.97%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.14% | **+0.92%** |
| LIMIT_10PCT | 2/20 | 10.0% | +7.36% | **+0.74%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.80% | **+0.72%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.08% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.45% | **+1.38%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_BB3S_LONG | 10/12 | 83.3% | +0.93% | **+0.78%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +1.65% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$562.74** / 初期 $100.00 (+462.74%)
- 確定: 3567件 (Win 1141 / Loss 1162 / Flat 1264) / skip 2970件
- 成長率目線: 平均log +0.000484 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $562.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.30** / 初期 $100.00 (+43.30%)
- 確定: 1270件 (Win 359 / Loss 292 / Flat 619) / skip 2117件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1652 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $143.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.65** / 初期 $100.00 (+10.65%)
- 確定: 813件 (Win 264 / Loss 323 / Flat 226) / pending 4件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000344 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $110.65

## 6. Latest Market Context

- 更新: 2026-07-31T08:01:11.590869+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63909.0
- Funnel: target 920 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +65.12% | $10,710,274.16 |
| GIGGLE/USDT:USDT | +45.60% | $3,926,931.56 |
| MMT/USDT:USDT | +32.81% | $12,290,178.10 |
| AXTISTOCK/USDT:USDT | +31.77% | $4,632,871.38 |
| BULLA/USDT:USDT | +28.77% | $1,302,040.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +3.25% | +3.25% |
| SOXL/USDT:USDT | below_1h_threshold | +2.93% | +2.93% |
| KORU/USDT:USDT | below_1h_threshold | +2.93% | +2.93% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.50% | +2.50% |
| MVLL/USDT:USDT | below_1h_threshold | +1.92% | +1.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
