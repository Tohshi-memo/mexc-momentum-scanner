# Decision Report

- generated_at: 2026-05-08T07:03:00.504359+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3749**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=3749, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.57% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| ASK_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 25件 (TP 6 / SL 17 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 120件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T07:02:57.237429+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=79411.1
- Funnel: target 772 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +37.02% | $4,100,144.91 |
| SATO/USDT:USDT | +25.74% | $8,913,758.43 |
| BSB/USDT:USDT | +24.08% | $4,788,683.22 |
| NOT/USDT:USDT | +23.21% | $10,034,542.24 |
| LAB/USDT:USDT | +18.86% | $203,360,791.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +3.40% | +3.49% |
| CHZ/USDT:USDT | below_1h_threshold | +3.10% | +3.20% |
| PLAY/USDT:USDT | below_1h_threshold | +1.84% | +1.94% |
| TAC/USDT:USDT | below_1h_threshold | +1.29% | +1.38% |
| BSB/USDT:USDT | below_1h_threshold | +1.00% | +1.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
