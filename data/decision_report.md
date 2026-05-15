# Decision Report

- generated_at: 2026-05-15T07:28:11.924770+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4326**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.44% / filled 20/20。**
- 全期間 MARKET基準: n=4326, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+3.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.44% | **+3.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.50% | **+3.50%** |
| MARKET | 20/20 | 100.0% | +3.44% | **+3.44%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.62% | **+2.89%** |
| LIMIT_2PCT | 13/20 | 65.0% | +3.71% | **+2.41%** |
| LIMIT_ATR | 11/20 | 55.0% | +3.02% | **+1.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.36% | **+0.75%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.33% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 378件 (Win 97 / Loss 131 / Flat 150) / skip 509件
- 成長率目線: 平均log +0.000491 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNDKSTOCK/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T07:28:08.761616+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.49% price=80940.1
- Funnel: target 761 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +28.04% | $3,631,112.87 |
| GWEI/USDT:USDT | +27.89% | $1,313,236.74 |
| UP/USDT:USDT | +22.64% | $4,215,437.78 |
| FIGSTOCK/USDT:USDT | +14.45% | $3,188,677.64 |
| BILL/USDT:USDT | +13.09% | $20,039,633.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.34% | +3.85% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.69% | +2.20% |
| UB/USDT:USDT | below_1h_threshold | +2.30% | +1.81% |
| UP/USDT:USDT | below_1h_threshold | +2.23% | +1.73% |
| CHIP/USDT:USDT | below_1h_threshold | +2.14% | +1.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
