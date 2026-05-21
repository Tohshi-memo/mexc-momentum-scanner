# Decision Report

- generated_at: 2026-05-21T11:33:55.070054+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4619**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=4619, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.65% | **+1.41%** |
| ASK | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_BB3S | 7/19 | 36.8% | +2.03% | **+0.75%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.01% | **+0.80%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.08% | **+0.54%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.21% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 634件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T11:33:53.054786+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=77280.0
- Funnel: target 766 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROVE/USDT:USDT | +50.02% | $4,264,913.13 |
| EDEN/USDT:USDT | +37.62% | $30,761,677.01 |
| ROAM/USDT:USDT | +34.62% | $2,234,204.47 |
| MITO/USDT:USDT | +33.22% | $1,115,643.01 |
| PEAQ/USDT:USDT | +30.88% | $1,012,118.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +2.24% | +2.09% |
| LIT/USDT:USDT | below_1h_threshold | +2.17% | +2.03% |
| FIDA/USDT:USDT | below_1h_threshold | +2.16% | +2.02% |
| BEAT/USDT:USDT | below_1h_threshold | +1.68% | +1.54% |
| MONAD/USDT:USDT | below_1h_threshold | +1.57% | +1.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
