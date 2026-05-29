# Decision Report

- generated_at: 2026-05-29T12:14:44.237312+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5046**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=5046, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.48% | **+0.41%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.31% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.92% | **+0.74%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.61% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$99.09** / 初期 $100.00 (-0.91%)
- 確定トレード: 73件 (TP 22 / SL 48 / EXP 3)
- 最新: NIL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 867件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T12:14:41.624286+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=73321.2
- Funnel: target 777 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +130.46% | $99,639,767.80 |
| ID/USDT:USDT | +39.36% | $1,714,467.08 |
| DELLSTOCK/USDT:USDT | +30.28% | $9,882,128.61 |
| LAB/USDT:USDT | +26.73% | $83,467,888.28 |
| CTR/USDT:USDT | +25.30% | $1,498,620.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CTR/USDT:USDT | below_1h_threshold | +4.45% | +4.62% |
| GUA/USDT:USDT | below_1h_threshold | +2.66% | +2.83% |
| JCT/USDT:USDT | below_1h_threshold | +2.11% | +2.28% |
| ID/USDT:USDT | below_1h_threshold | +1.73% | +1.90% |
| PHA/USDT:USDT | below_1h_threshold | +0.84% | +1.01% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
