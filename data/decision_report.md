# Decision Report

- generated_at: 2026-05-20T14:03:48.117136+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4545**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=4545, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.56% | **+1.56%** |
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.67% | **+1.50%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.85% | **+0.55%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.55% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.54% | **-0.24%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.46% | **-0.25%** |

## 2. $100 Live Portfolio

- 残高: **$97.18** / 初期 $100.00 (-2.82%)
- 確定トレード: 56件 (TP 15 / SL 38 / EXP 3)
- 最新: SATO/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.91** / 初期 $100.00 (+23.91%)
- 確定: 507件 (Win 132 / Loss 174 / Flat 201) / skip 599件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROMPT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $123.91

## 4. Latest Market Context

- 更新: 2026-05-20T14:03:46.097235+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=77145.2
- Funnel: target 763 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +75.35% | $2,552,630.34 |
| FIDA/USDT:USDT | +48.72% | $4,849,120.14 |
| BANANAS31/USDT:USDT | +28.66% | $2,754,341.12 |
| PROMPT/USDT:USDT | +27.73% | $12,852,264.86 |
| EDEN/USDT:USDT | +25.13% | $22,702,637.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.52% | +1.56% |
| SATO/USDT:USDT | below_1h_threshold | +1.50% | +1.54% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.08% | +1.12% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.97% | +1.01% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.69% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
