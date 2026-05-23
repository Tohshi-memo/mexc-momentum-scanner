# Decision Report

- generated_at: 2026-05-23T05:39:06.288321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4756**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=4756, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| ASK | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.48% | **+0.34%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.21% | **+0.14%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 602件 (Win 149 / Loss 191 / Flat 262) / skip 715件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-23T05:39:04.154675+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=75463.9
- Funnel: target 764 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +125.10% | $60,508,575.79 |
| IN/USDT:USDT | +28.08% | $1,602,969.43 |
| BILL/USDT:USDT | +17.31% | $18,665,535.54 |
| BEAT/USDT:USDT | +17.22% | $59,694,749.51 |
| MYX/USDT:USDT | +11.06% | $1,102,927.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.22% | +3.28% |
| BSB/USDT:USDT | below_1h_threshold | +2.87% | +2.92% |
| MYX/USDT:USDT | below_1h_threshold | +2.04% | +2.10% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.47% | +1.53% |
| CHIP/USDT:USDT | below_1h_threshold | +1.29% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
