# Decision Report

- generated_at: 2026-06-12T21:06:16.616233+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6543**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.22% / filled 20/20。**
- 全期間 MARKET基準: n=6543, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+4.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.22% | **+4.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.22% | **+4.22%** |
| ASK | 20/20 | 100.0% | +3.66% | **+3.66%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.56% | **+2.85%** |
| LIMIT_2PCT | 13/20 | 65.0% | +4.01% | **+2.61%** |
| LIMIT_ATR | 9/20 | 45.0% | +4.80% | **+2.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.95% | **+0.49%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | -1.98% | **-1.28%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$163.82** / 初期 $100.00 (+63.82%)
- 確定: 1416件 (Win 388 / Loss 462 / Flat 566) / skip 1688件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $163.82

## 4. Latest Market Context

- 更新: 2026-06-12T21:06:13.855272+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=63446.6
- Funnel: target 774 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +16.04% | $1,224,998.29 |
| PLAY/USDT:USDT | +15.93% | $10,206,126.23 |
| AIN/USDT:USDT | +10.63% | $1,697,582.87 |
| H/USDT:USDT | +8.64% | $29,668,567.76 |
| ESPORTS/USDT:USDT | +6.02% | $68,993,695.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.84% | +2.79% |
| AIN/USDT:USDT | below_1h_threshold | +0.25% | +0.20% |
| SITMSTOCK/USDT:USDT | below_1h_threshold | +0.23% | +0.19% |
| PLSTOCK/USDT:USDT | below_1h_threshold | +0.19% | +0.15% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.14% | +0.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
