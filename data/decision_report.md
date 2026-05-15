# Decision Report

- generated_at: 2026-05-15T12:08:35.360077+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4334**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.90% / filled 20/20。**
- 全期間 MARKET基準: n=4334, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.04% | **+2.04%** |
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.81% | **+1.54%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.85% | **+1.29%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.52% | **+1.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +2.06% | **+1.24%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.97% | **+0.63%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.61% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.81** / 初期 $100.00 (+19.81%)
- 確定: 384件 (Win 97 / Loss 132 / Flat 155) / skip 511件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $119.81

## 4. Latest Market Context

- 更新: 2026-05-15T12:08:32.140216+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=80352.0
- Funnel: target 764 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +29.08% | $5,272,490.23 |
| UP/USDT:USDT | +28.15% | $5,184,857.71 |
| GWEI/USDT:USDT | +26.77% | $1,656,333.14 |
| PEAQ/USDT:USDT | +24.67% | $4,399,894.87 |
| GUA/USDT:USDT | +14.68% | $1,290,052.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +4.97% | +5.25% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.05% | +2.33% |
| AIO/USDT:USDT | below_1h_threshold | +0.64% | +0.93% |
| BEAT/USDT:USDT | below_1h_threshold | +0.42% | +0.71% |
| RIVER/USDT:USDT | below_1h_threshold | +0.35% | +0.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
