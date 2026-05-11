# Decision Report

- generated_at: 2026-05-11T06:37:52.118892+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4010**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=4010, expectancy=-0.12%
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
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.93% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.16% | **+0.99%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.31% | **+0.92%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.34% | **+0.27%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +0.14% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$99.20** / 初期 $100.00 (-0.80%)
- 確定トレード: 31件 (TP 8 / SL 20 / EXP 3)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.40** / 初期 $100.00 (+8.40%)
- 確定: 216件 (Win 54 / Loss 75 / Flat 87) / skip 355件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.40

## 4. Latest Market Context

- 更新: 2026-05-11T06:37:48.049863+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=80888.0
- Funnel: target 777 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.4 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +36.44% | $3,577,478.14 |
| US/USDT:USDT | +34.72% | $10,806,393.40 |
| TROLLSOL/USDT:USDT | +18.12% | $5,200,410.83 |
| ALCH/USDT:USDT | +18.09% | $4,502,244.94 |
| SAGA/USDT:USDT | +15.60% | $1,270,853.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +4.68% | +4.57% |
| UB/USDT:USDT | below_1h_threshold | +4.40% | +4.30% |
| US/USDT:USDT | below_1h_threshold | +1.87% | +1.77% |
| TRUTH/USDT:USDT | below_1h_threshold | +1.36% | +1.25% |
| DEEP/USDT:USDT | below_1h_threshold | +1.27% | +1.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
