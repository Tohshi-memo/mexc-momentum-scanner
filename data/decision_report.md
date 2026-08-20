# Decision Report

- generated_at: 2026-08-20T08:21:24.724088+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12019**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12019, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.35% | **+0.41%** |
| LIMIT_BB3S | 6/14 | 42.9% | +0.81% | **+0.35%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.48% | **+0.22%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.35% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.86% | **+1.39%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.12% | **+1.17%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.93% | **+0.97%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.20** / 初期 $100.00 (+506.20%)
- 確定: 4243件 (Win 1303 / Loss 1388 / Flat 1552) / skip 4337件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BOME/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $606.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3609件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.76** / 初期 $100.00 (+16.76%)
- 確定: 1754件 (Win 520 / Loss 670 / Flat 564) / pending 3件 / skip 1736件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000489 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MINIMAXSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.76

## 6. Latest Market Context

- 更新: 2026-08-20T08:21:16.251636+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.06% price=71256.5
- Funnel: target 1004 → liquid 197 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BOME/USDT:USDT | +32.63% | $4,258,563.73 |
| MAGMA/USDT:USDT | +28.77% | $7,681,787.84 |
| BASECAT/USDT:USDT | +23.68% | $1,229,852.37 |
| RED/USDT:USDT | +19.89% | $2,138,073.28 |
| LIT/USDT:USDT | +19.36% | $10,169,248.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEPE/USDT:USDT | below_1h_threshold | +3.02% | +0.95% |
| ENA/USDT:USDT | below_1h_threshold | +2.76% | +0.69% |
| FLOKI/USDT:USDT | below_1h_threshold | +2.57% | +0.51% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.30% | +0.24% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.11% | +0.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
