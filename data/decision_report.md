# Decision Report

- generated_at: 2026-05-15T03:38:15.599639+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4321**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.65% / filled 20/20。**
- 全期間 MARKET基準: n=4321, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+2.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.65% | **+2.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.69% | **+2.69%** |
| MARKET | 20/20 | 100.0% | +2.65% | **+2.65%** |
| LIMIT_BB3S | 4/14 | 28.6% | +5.64% | **+1.61%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.76% | **+1.32%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.99% | **+1.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +2.72% | **+2.72%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.82% | **+0.49%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 44件 (TP 11 / SL 30 / EXP 3)
- 最新: SKYAI/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.02** / 初期 $100.00 (+21.02%)
- 確定: 373件 (Win 97 / Loss 130 / Flat 146) / skip 509件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $121.02

## 4. Latest Market Context

- 更新: 2026-05-15T03:38:11.936841+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=80962.6
- Funnel: target 764 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +32.02% | $2,665,853.45 |
| GWEI/USDT:USDT | +19.46% | $1,063,827.58 |
| FIGSTOCK/USDT:USDT | +14.45% | $3,091,833.11 |
| UP/USDT:USDT | +13.96% | $3,984,124.53 |
| TAC/USDT:USDT | +12.56% | $2,069,193.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEAQ/USDT:USDT | below_1h_threshold | +2.92% | +3.29% |
| RIVER/USDT:USDT | below_1h_threshold | +2.73% | +3.10% |
| H/USDT:USDT | below_1h_threshold | +1.60% | +1.97% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +1.46% | +1.82% |
| GUA/USDT:USDT | below_1h_threshold | +1.22% | +1.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
