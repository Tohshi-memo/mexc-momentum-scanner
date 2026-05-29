# Decision Report

- generated_at: 2026-05-29T21:14:48.674742+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5072**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=5072, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/18 | 55.6% | +1.92% | **+1.07%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.04% | **+0.94%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.42% | **+0.38%** |
| ASK_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 893件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T21:14:46.448121+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=73777.0
- Funnel: target 773 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASED/USDT:USDT | +18.38% | $1,524,621.31 |
| XLM/USDT:USDT | +12.41% | $356,249,109.80 |
| GRASS/USDT:USDT | +10.30% | $4,209,103.47 |
| LAB/USDT:USDT | +9.89% | $114,278,321.13 |
| HEI/USDT:USDT | +5.74% | $8,844,467.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +1.87% | +1.69% |
| BASED/USDT:USDT | below_1h_threshold | +1.75% | +1.57% |
| MEGA/USDT:USDT | below_1h_threshold | +1.64% | +1.46% |
| ZEC/USDT:USDT | below_1h_threshold | +1.30% | +1.12% |
| HBAR/USDT:USDT | below_1h_threshold | +1.20% | +1.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
