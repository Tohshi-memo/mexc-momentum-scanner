# Decision Report

- generated_at: 2026-08-26T10:11:22.071360+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12695**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12695, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.22% | **+0.49%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.45% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.55% | **+1.39%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.54% | **+1.16%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.41% | **+0.77%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$699.64** / 初期 $100.00 (+599.64%)
- 確定: 4596件 (Win 1398 / Loss 1510 / Flat 1688) / skip 4660件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $699.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.92** / 初期 $100.00 (+57.92%)
- 確定: 1991件 (Win 542 / Loss 477 / Flat 972) / skip 4115件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1732 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $157.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.52** / 初期 $100.00 (+16.52%)
- 確定: 1969件 (Win 578 / Loss 750 / Flat 641) / pending 4件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000392 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.52

## 6. Latest Market Context

- 更新: 2026-08-26T10:11:12.451813+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=78311.4
- Funnel: target 1023 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +173.19% | $13,119,417.08 |
| BMT/USDT:USDT | +55.23% | $14,219,264.47 |
| TAC/USDT:USDT | +33.46% | $6,327,319.44 |
| LONGXIA/USDT:USDT | +28.62% | $1,971,582.14 |
| PORTAL/USDT:USDT | +20.69% | $3,931,932.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +1.35% | +1.49% |
| BEAT/USDT:USDT | below_1h_threshold | +1.00% | +1.14% |
| BICO/USDT:USDT | below_1h_threshold | +0.79% | +0.93% |
| CYS/USDT:USDT | below_1h_threshold | +0.69% | +0.83% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.45% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
