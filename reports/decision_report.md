# Decision Report

- generated_at: 2026-06-01T04:21:43.092289+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5269**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.93% / filled 20/20。**
- 全期間 MARKET基準: n=5269, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.99% | **+2.99%** |
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.67% | **+2.13%** |
| LIMIT_ATR | 13/20 | 65.0% | +3.10% | **+2.01%** |
| LIMIT_2PCT | 13/20 | 65.0% | +3.09% | **+2.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.48% | **+0.34%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.19% | **+0.33%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | +0.31% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 936件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T04:17:03.422365+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=73585.8
- Funnel: target 777 → liquid 133 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +165.57% | $28,417,007.89 |
| H/USDT:USDT | +61.06% | $21,663,141.39 |
| STG/USDT:USDT | +34.80% | $22,833,330.64 |
| FHE/USDT:USDT | +28.62% | $1,112,652.71 |
| WLD/USDT:USDT | +21.49% | $60,848,149.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.23% | +4.42% |
| FHE/USDT:USDT | below_1h_threshold | +3.68% | +3.88% |
| CTR/USDT:USDT | below_1h_threshold | +2.99% | +3.19% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.39% | +1.59% |
| XLM/USDT:USDT | below_1h_threshold | +1.39% | +1.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
