# Decision Report

- generated_at: 2026-05-29T20:00:24.753680+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5071**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=5071, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/17 | 58.8% | +1.92% | **+1.13%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.38% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.09% | **+0.98%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.87% | **+0.61%** |
| ASK_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 892件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T20:00:22.234751+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=73511.7
- Funnel: target 774 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GUA/USDT:USDT | +18.71% | $6,404,996.07 |
| XLM/USDT:USDT | +11.40% | $354,519,393.47 |
| GRASS/USDT:USDT | +10.21% | $3,922,841.09 |
| LIT/USDT:USDT | +9.61% | $3,816,435.45 |
| ZBCN/USDT:USDT | +8.36% | $1,169,898.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +0.77% | +0.73% |
| IBMSTOCK/USDT:USDT | below_1h_threshold | +0.41% | +0.38% |
| LAB/USDT:USDT | below_1h_threshold | +0.40% | +0.37% |
| GRASS/USDT:USDT | below_1h_threshold | +0.22% | +0.19% |
| VVV/USDT:USDT | below_1h_threshold | +0.17% | +0.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
