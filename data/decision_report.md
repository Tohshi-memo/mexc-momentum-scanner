# Decision Report

- generated_at: 2026-05-15T12:13:15.380654+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4335**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=4335, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.41% | **+2.41%** |
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.20% | **+1.87%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.90% | **+1.43%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.84% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +1.59% | **+1.04%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.10% | **+0.60%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.22** / 初期 $100.00 (+19.22%)
- 確定: 385件 (Win 97 / Loss 133 / Flat 155) / skip 511件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_6PCT_LONG` SL_HIT account -0.50% 残高後 $119.22

## 4. Latest Market Context

- 更新: 2026-05-15T12:13:09.263546+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80462.5
- Funnel: target 764 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +28.47% | $5,444,329.17 |
| UP/USDT:USDT | +28.37% | $5,188,561.90 |
| GWEI/USDT:USDT | +26.34% | $1,660,064.20 |
| PEAQ/USDT:USDT | +24.67% | $4,407,140.19 |
| GUA/USDT:USDT | +18.85% | $1,305,536.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.35% | +1.50% |
| BEAT/USDT:USDT | below_1h_threshold | +0.80% | +0.95% |
| AIO/USDT:USDT | below_1h_threshold | +0.63% | +0.78% |
| RIVER/USDT:USDT | below_1h_threshold | +0.50% | +0.65% |
| POLYX/USDT:USDT | below_1h_threshold | +0.45% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
