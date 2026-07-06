# Decision Report

- generated_at: 2026-07-06T19:03:35.333135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8406**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8406, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.66% | **+0.33%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |
| ASK | 20/20 | 100.0% | +0.00% | **+0.00%** |
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |
| LIMIT_8PCT | 4/20 | 20.0% | -0.15% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +1.76% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.32% | **+0.99%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.32% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.13** / 初期 $100.00 (+217.13%)
- 確定: 2624件 (Win 832 / Loss 887 / Flat 905) / skip 2343件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $317.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1178件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T19:03:30.187195+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63659.7
- Funnel: target 841 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUR/USDT:USDT | +20.54% | $2,932,065.32 |
| ANSEM/USDT:USDT | +14.41% | $4,155,622.70 |
| ALLO/USDT:USDT | +10.37% | $14,827,138.68 |
| HMSTR/USDT:USDT | +10.10% | $4,630,249.24 |
| CAP/USDT:USDT | +6.80% | $5,886,321.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LDO/USDT:USDT | below_1h_threshold | +1.07% | +1.09% |
| ALLO/USDT:USDT | below_1h_threshold | +0.76% | +0.78% |
| VVV/USDT:USDT | below_1h_threshold | +0.75% | +0.77% |
| ANSEM/USDT:USDT | below_1h_threshold | +0.73% | +0.75% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.55% | +0.57% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
