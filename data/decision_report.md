# Decision Report

- generated_at: 2026-05-15T10:43:13.849660+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4331**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.39% / filled 20/20。**
- 全期間 MARKET基準: n=4331, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.48% | **+2.48%** |
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.44% | **+2.07%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.79% | **+1.82%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.34% | **+1.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +2.19% | **+1.20%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.96% | **+1.18%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.61% | **+0.39%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.42% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 383件 (Win 97 / Loss 131 / Flat 155) / skip 509件
- 成長率目線: 平均log +0.000485 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T10:43:10.415725+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80428.9
- Funnel: target 763 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +28.97% | $4,185,858.77 |
| GWEI/USDT:USDT | +23.88% | $1,542,151.37 |
| UP/USDT:USDT | +21.44% | $4,754,003.95 |
| IRYS/USDT:USDT | +16.82% | $2,750,735.50 |
| FF/USDT:USDT | +16.38% | $1,553,551.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +3.86% | +3.89% |
| COLLECT/USDT:USDT | below_1h_threshold | +3.09% | +3.12% |
| CHZ/USDT:USDT | below_1h_threshold | +2.87% | +2.90% |
| BEAT/USDT:USDT | below_1h_threshold | +1.95% | +1.98% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +1.72% | +1.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
