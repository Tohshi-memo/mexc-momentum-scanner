# Decision Report

- generated_at: 2026-05-19T13:08:43.388796+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4469**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4469, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.29% | **-1.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.84% | **+0.67%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.33% | **+0.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.45% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +3.17% | **+1.81%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.18% | **+1.63%** |
| MARKET_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.15% | **+0.63%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.97% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.57** / 初期 $100.00 (+24.57%)
- 確定: 466件 (Win 124 / Loss 159 / Flat 183) / skip 564件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $124.57

## 4. Latest Market Context

- 更新: 2026-05-19T13:08:41.429668+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=76762.1
- Funnel: target 764 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +36.46% | $13,098,715.75 |
| PLAY/USDT:USDT | +29.11% | $5,145,883.43 |
| EDEN/USDT:USDT | +27.13% | $3,332,957.55 |
| ONT/USDT:USDT | +13.70% | $2,126,795.55 |
| SIREN/USDT:USDT | +12.71% | $2,119,095.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +1.22% | +1.40% |
| BSB/USDT:USDT | below_1h_threshold | +0.99% | +1.17% |
| NEAR/USDT:USDT | below_1h_threshold | +0.31% | +0.49% |
| PLAY/USDT:USDT | below_1h_threshold | +0.29% | +0.47% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.16% | +0.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
