# Decision Report

- generated_at: 2026-05-27T05:09:28.569564+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4918**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=4918, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.70% | **+0.70%** |
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.29% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.41% | **+1.27%** |
| MARKET_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.18% | **+0.65%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.01% | **+0.55%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.76% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.07** / 初期 $100.00 (+28.07%)
- 確定: 681件 (Win 172 / Loss 218 / Flat 291) / skip 798件
- 成長率目線: 平均log +0.000363 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $128.07

## 4. Latest Market Context

- 更新: 2026-05-27T05:09:26.435915+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=75593.9
- Funnel: target 772 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| REQ/USDT:USDT | +26.49% | $1,363,646.43 |
| RON/USDT:USDT | +14.95% | $1,041,388.77 |
| LUNC/USDT:USDT | +14.56% | $9,751,687.88 |
| PLAY/USDT:USDT | +11.50% | $8,344,408.56 |
| GUA/USDT:USDT | +9.89% | $3,682,452.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RON/USDT:USDT | below_1h_threshold | +1.82% | +1.75% |
| UB/USDT:USDT | below_1h_threshold | +1.47% | +1.40% |
| LUNC/USDT:USDT | below_1h_threshold | +0.83% | +0.76% |
| USELESS/USDT:USDT | below_1h_threshold | +0.80% | +0.73% |
| AKT/USDT:USDT | below_1h_threshold | +0.75% | +0.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
