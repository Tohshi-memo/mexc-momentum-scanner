# Decision Report

- generated_at: 2026-05-31T10:25:08.188877+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5186**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=5186, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.26% | **+0.38%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.38% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.59% | **+1.43%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.57% | **+1.33%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.48% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.08** / 初期 $100.00 (+25.08%)
- 確定: 821件 (Win 188 / Loss 245 / Flat 388) / skip 926件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIA/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $125.08

## 4. Latest Market Context

- 更新: 2026-05-31T10:25:05.671398+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=73724.5
- Funnel: target 773 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +55.46% | $2,355,199.63 |
| PLAY/USDT:USDT | +42.29% | $4,987,805.29 |
| PORTAL/USDT:USDT | +26.25% | $12,369,818.56 |
| TA/USDT:USDT | +22.94% | $2,492,043.86 |
| MYX/USDT:USDT | +15.81% | $3,625,995.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +3.34% | +3.46% |
| HIVE/USDT:USDT | below_1h_threshold | +2.69% | +2.81% |
| PLAY/USDT:USDT | below_1h_threshold | +1.24% | +1.36% |
| TA/USDT:USDT | below_1h_threshold | +1.22% | +1.34% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.11% | +1.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
