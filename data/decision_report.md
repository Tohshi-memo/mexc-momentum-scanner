# Decision Report

- generated_at: 2026-06-05T07:16:09.175069+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5700**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=5700, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.39% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.41% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1009件 (Win 239 / Loss 312 / Flat 458) / skip 1252件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T07:16:06.731096+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.53% price=61585.7
- Funnel: target 772 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +55.56% | $19,855,936.69 |
| OPN/USDT:USDT | +28.07% | $35,512,145.00 |
| BEAT/USDT:USDT | +11.68% | $26,281,569.28 |
| HEI/USDT:USDT | +11.12% | $4,405,370.54 |
| HOME/USDT:USDT | +10.01% | $8,474,478.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPN/USDT:USDT | below_1h_threshold | +3.84% | +4.37% |
| AIA/USDT:USDT | below_1h_threshold | +2.98% | +3.52% |
| UB/USDT:USDT | below_1h_threshold | +0.82% | +1.35% |
| APPSTOCK/USDT:USDT | below_1h_threshold | +0.68% | +1.22% |
| XAU/USDT:USDT | below_1h_threshold | +0.17% | +0.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
