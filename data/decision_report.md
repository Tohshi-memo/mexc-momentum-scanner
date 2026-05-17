# Decision Report

- generated_at: 2026-05-17T17:13:31.698781+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4413**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4413, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_BB3S | 5/11 | 45.5% | +1.22% | **+0.55%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.04% | **+0.02%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.68% | **+1.88%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.29% | **+1.26%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.62% | **+1.21%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.77% | **+1.06%** |
| ASK_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.26** / 初期 $100.00 (+19.26%)
- 確定: 410件 (Win 106 / Loss 139 / Flat 165) / skip 564件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $119.26

## 4. Latest Market Context

- 更新: 2026-05-17T17:13:29.731139+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=77849.2
- Funnel: target 760 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +4.51% | $5,096,656.39 |
| UB/USDT:USDT | +3.14% | $11,809,507.69 |
| KAIA/USDT:USDT | +2.25% | $4,417,089.61 |
| RAVE/USDT:USDT | +2.14% | $5,987,088.31 |
| BEAT/USDT:USDT | +1.79% | $3,387,081.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +0.84% | +1.03% |
| B/USDT:USDT | below_1h_threshold | +0.82% | +1.01% |
| IONQSTOCK/USDT:USDT | below_1h_threshold | +0.77% | +0.95% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.52% | +0.70% |
| PLAY/USDT:USDT | below_1h_threshold | +0.46% | +0.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
