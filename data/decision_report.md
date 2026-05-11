# Decision Report

- generated_at: 2026-05-11T06:43:03.142725+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4011**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=4011, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |
| ASK | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_BB3S | 6/12 | 50.0% | +1.74% | **+0.87%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.73% | **+0.59%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.80% | **+0.52%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +0.14% | **+0.13%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.57% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$99.20** / 初期 $100.00 (-0.80%)
- 確定トレード: 31件 (TP 8 / SL 20 / EXP 3)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.40** / 初期 $100.00 (+8.40%)
- 確定: 217件 (Win 54 / Loss 75 / Flat 88) / skip 355件
- 成長率目線: 平均log +0.000372 / 幾何平均 +0.037% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.40

## 4. Latest Market Context

- 更新: 2026-05-11T06:42:59.080989+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80766.4
- Funnel: target 777 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1, 4h RSI 71.5 >= 65=1, 4h RSI 73.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +41.03% | $4,211,454.80 |
| US/USDT:USDT | +33.34% | $10,827,864.41 |
| ALCH/USDT:USDT | +18.36% | $4,505,451.12 |
| TROLLSOL/USDT:USDT | +17.30% | $5,205,247.10 |
| SAGA/USDT:USDT | +14.80% | $1,289,791.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.52% | +3.56% |
| ROBO/USDT:USDT | below_1h_threshold | +1.46% | +1.50% |
| BAS/USDT:USDT | below_1h_threshold | +1.35% | +1.39% |
| US/USDT:USDT | below_1h_threshold | +0.83% | +0.87% |
| OPG/USDT:USDT | below_1h_threshold | +0.72% | +0.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
