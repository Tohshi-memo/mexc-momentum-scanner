# Decision Report

- generated_at: 2026-05-20T15:23:54.209171+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4551**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4551, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.54% | **+0.52%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.81% | **+0.24%** |
| ASK | 20/20 | 100.0% | +0.07% | **+0.07%** |
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| ASK_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.39% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.72** / 初期 $100.00 (+23.72%)
- 確定: 513件 (Win 135 / Loss 175 / Flat 203) / skip 599件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $123.72

## 4. Latest Market Context

- 更新: 2026-05-20T15:23:51.886357+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=77683.4
- Funnel: target 763 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +93.20% | $2,975,478.97 |
| FIDA/USDT:USDT | +52.73% | $6,308,544.35 |
| EDEN/USDT:USDT | +34.47% | $24,201,007.80 |
| LIT/USDT:USDT | +26.87% | $11,235,896.78 |
| BANANAS31/USDT:USDT | +24.19% | $3,342,562.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.79% | +4.45% |
| EDEN/USDT:USDT | below_1h_threshold | +3.11% | +2.76% |
| ZEC/USDT:USDT | below_1h_threshold | +2.32% | +1.97% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.31% | +1.96% |
| FIGHT/USDT:USDT | below_1h_threshold | +2.22% | +1.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
