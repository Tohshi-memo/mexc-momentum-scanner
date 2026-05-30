# Decision Report

- generated_at: 2026-05-30T15:05:27.809612+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5134**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=5134, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.74% | **+1.65%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.78% | **+1.25%** |
| LIMIT_BB3S | 9/17 | 52.9% | +2.31% | **+1.22%** |
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.98% | **+0.79%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.39% | **+0.26%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.12% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 76件 (TP 22 / SL 51 / EXP 3)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.38** / 初期 $100.00 (+23.38%)
- 確定: 789件 (Win 183 / Loss 241 / Flat 365) / skip 906件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +5.96%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $123.38

## 4. Latest Market Context

- 更新: 2026-05-30T15:05:25.380842+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=73872.1
- Funnel: target 773 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +57.21% | $4,064,837.45 |
| LAB/USDT:USDT | +38.16% | $143,933,574.05 |
| STG/USDT:USDT | +37.84% | $2,370,610.25 |
| NFP/USDT:USDT | +28.79% | $3,759,924.33 |
| H/USDT:USDT | +28.64% | $7,504,159.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +0.86% | +0.90% |
| VTHO/USDT:USDT | below_1h_threshold | +0.86% | +0.90% |
| RENDER/USDT:USDT | below_1h_threshold | +0.43% | +0.47% |
| XMR/USDT:USDT | below_1h_threshold | +0.38% | +0.42% |
| LAB/USDT:USDT | below_1h_threshold | +0.33% | +0.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
