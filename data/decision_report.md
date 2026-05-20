# Decision Report

- generated_at: 2026-05-20T14:28:49.210451+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4547**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.35% / filled 20/20。**
- 全期間 MARKET基準: n=4547, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.79% | **+0.75%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.22% | **+0.49%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.61% | **+0.46%** |
| ASK | 20/20 | 100.0% | +0.36% | **+0.36%** |
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |
| ASK_LONG | 20/20 | 100.0% | +0.18% | **+0.18%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.32% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$97.18** / 初期 $100.00 (-2.82%)
- 確定トレード: 56件 (TP 15 / SL 38 / EXP 3)
- 最新: SATO/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.06** / 初期 $100.00 (+24.06%)
- 確定: 509件 (Win 133 / Loss 174 / Flat 202) / skip 599件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIGHT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $124.06

## 4. Latest Market Context

- 更新: 2026-05-20T14:28:44.562482+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=77378.5
- Funnel: target 763 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +85.24% | $2,655,186.45 |
| FIDA/USDT:USDT | +54.29% | $5,330,825.68 |
| PROMPT/USDT:USDT | +25.62% | $12,885,296.63 |
| BANANAS31/USDT:USDT | +24.93% | $2,999,315.52 |
| EDEN/USDT:USDT | +24.31% | $23,116,014.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +3.93% | +3.67% |
| FIDA/USDT:USDT | below_1h_threshold | +3.64% | +3.38% |
| DASH/USDT:USDT | below_1h_threshold | +3.23% | +2.96% |
| H/USDT:USDT | below_1h_threshold | +2.42% | +2.15% |
| BSB/USDT:USDT | below_1h_threshold | +2.32% | +2.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
