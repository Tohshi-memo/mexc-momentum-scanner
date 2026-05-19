# Decision Report

- generated_at: 2026-05-19T13:38:44.106642+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4470**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4470, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.29% | **-1.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.36% | **+0.27%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.33% | **+0.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.45% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +3.17% | **+1.81%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.18% | **+1.63%** |
| MARKET_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.53% | **+0.83%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.85% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.95** / 初期 $100.00 (+23.95%)
- 確定: 467件 (Win 124 / Loss 160 / Flat 183) / skip 564件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $123.95

## 4. Latest Market Context

- 更新: 2026-05-19T13:38:42.101878+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=76877.5
- Funnel: target 764 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +35.88% | $13,371,231.13 |
| PLAY/USDT:USDT | +30.62% | $5,364,375.00 |
| EDEN/USDT:USDT | +24.55% | $3,619,172.56 |
| ONT/USDT:USDT | +13.18% | $2,188,891.48 |
| SIREN/USDT:USDT | +8.23% | $2,616,636.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WDCSTOCK/USDT:USDT | below_1h_threshold | +3.88% | +3.91% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.36% | +3.39% |
| VVV/USDT:USDT | below_1h_threshold | +2.03% | +2.06% |
| PLAY/USDT:USDT | below_1h_threshold | +1.50% | +1.53% |
| ALGO/USDT:USDT | below_1h_threshold | +1.43% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
