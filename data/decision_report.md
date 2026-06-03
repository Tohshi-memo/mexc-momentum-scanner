# Decision Report

- generated_at: 2026-06-03T17:22:18.024862+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5566**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=5566, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.66% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +4.71% | **+2.02%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +3.14% | **+0.78%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.63% | **+0.57%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.81% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1123件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T17:22:15.557068+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=65834.1
- Funnel: target 771 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +23.10% | $4,292,332.18 |
| BP/USDT:USDT | +11.84% | $1,371,944.89 |
| EDEN/USDT:USDT | +11.62% | $1,330,591.31 |
| HEI/USDT:USDT | +7.46% | $1,008,698.14 |
| US/USDT:USDT | +4.27% | $5,609,191.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.80% | +5.10% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.49% | +4.79% |
| UB/USDT:USDT | below_1h_threshold | +2.98% | +3.29% |
| EDEN/USDT:USDT | below_1h_threshold | +1.54% | +1.85% |
| APR/USDT:USDT | below_1h_threshold | +1.43% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
