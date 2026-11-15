# Decision Report

- generated_at: 2026-11-15T14:06:16.450865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18968**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18968, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.33% | **+0.27%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.45% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +1.57% | **+1.35%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.87% | **+0.52%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,711.71** / 初期 $100.00 (+1611.71%)
- 確定: 7335件 (Win 2106 / Loss 2348 / Flat 2881) / skip 8194件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,711.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.50** / 初期 $100.00 (+329.50%)
- 確定: 4970件 (Win 1330 / Loss 1081 / Flat 2559) / skip 7409件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0019 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $429.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7128件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000180 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T14:06:03.036924+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.48% price=65090.7
- Funnel: target 1066 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARIA/USDT:USDT | +33.34% | $3,935,024.61 |
| EVAA/USDT:USDT | +30.43% | $16,776,435.77 |
| INIT/USDT:USDT | +21.87% | $7,871,073.54 |
| JCT/USDT:USDT | +17.93% | $6,589,149.28 |
| IDOL/USDT:USDT | +11.37% | $1,775,747.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +1.92% | +2.41% |
| EVAA/USDT:USDT | below_1h_threshold | +0.77% | +1.26% |
| JCT/USDT:USDT | below_1h_threshold | +0.62% | +1.11% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.30% | +0.79% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.26% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
