# Decision Report

- generated_at: 2026-06-02T01:40:34.529438+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5387**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.25% / filled 20/20。**
- 全期間 MARKET基準: n=5387, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.25% | **+2.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.77% | **+2.77%** |
| MARKET | 20/20 | 100.0% | +2.25% | **+2.25%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.22% | **+1.11%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.21% | **-0.03%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.23% | **-0.12%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -1.12% | **-1.01%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.85** / 初期 $100.00 (+31.85%)
- 確定: 902件 (Win 209 / Loss 271 / Flat 422) / skip 1046件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $131.85

## 4. Latest Market Context

- 更新: 2026-06-02T01:40:32.200499+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.64% price=70807.3
- Funnel: target 776 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +66.90% | $9,447,817.09 |
| UB/USDT:USDT | +14.35% | $2,409,633.68 |
| SLX/USDT:USDT | +13.71% | $12,837,861.47 |
| WLD/USDT:USDT | +11.22% | $138,339,203.42 |
| NEAR/USDT:USDT | +7.98% | $134,970,739.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.96% | +4.61% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.23% | +3.88% |
| BILL/USDT:USDT | below_1h_threshold | +2.76% | +3.41% |
| UB/USDT:USDT | below_1h_threshold | +1.39% | +2.03% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.54% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
