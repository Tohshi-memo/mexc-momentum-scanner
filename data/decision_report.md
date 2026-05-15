# Decision Report

- generated_at: 2026-05-15T02:08:11.706629+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4318**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.45% / filled 20/20。**
- 全期間 MARKET基準: n=4318, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.45% | **+1.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.56% | **+1.56%** |
| LIMIT_BB3S | 5/14 | 35.7% | +4.35% | **+1.55%** |
| MARKET | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.85% | **+0.59%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.72% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +2.72% | **+2.72%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.11% | **+0.28%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.50% | **+0.25%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.22% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.02** / 初期 $100.00 (+21.02%)
- 確定: 370件 (Win 97 / Loss 130 / Flat 143) / skip 509件
- 成長率目線: 平均log +0.000516 / 幾何平均 +0.052% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEAQ/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $121.02

## 4. Latest Market Context

- 更新: 2026-05-15T02:08:08.154514+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=80998.9
- Funnel: target 763 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +30.47% | $2,187,143.79 |
| GWEI/USDT:USDT | +21.17% | $1,025,899.31 |
| UP/USDT:USDT | +18.39% | $3,809,898.22 |
| FIGSTOCK/USDT:USDT | +12.40% | $3,051,225.81 |
| TAC/USDT:USDT | +11.56% | $1,990,201.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEAQ/USDT:USDT | below_1h_threshold | +2.35% | +2.47% |
| LAB/USDT:USDT | below_1h_threshold | +1.45% | +1.57% |
| BB/USDT:USDT | below_1h_threshold | +1.08% | +1.19% |
| FF/USDT:USDT | below_1h_threshold | +1.01% | +1.13% |
| AIO/USDT:USDT | below_1h_threshold | +0.77% | +0.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
