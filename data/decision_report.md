# Decision Report

- generated_at: 2026-05-29T18:55:22.827460+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5067**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=5067, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/13 | 61.5% | +3.06% | **+1.89%** |
| ASK | 20/20 | 100.0% | +0.89% | **+0.89%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.63% | **+1.18%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.82% | **+0.78%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.89% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 888件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T18:55:20.442517+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.90% price=73286.2
- Funnel: target 774 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +21.22% | $7,560,933.76 |
| GUA/USDT:USDT | +8.26% | $6,137,591.35 |
| GRASS/USDT:USDT | +8.06% | $3,616,262.44 |
| LAB/USDT:USDT | +5.91% | $104,504,212.15 |
| FET/USDT:USDT | +3.76% | $31,062,930.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +2.50% | +3.40% |
| ZBCN/USDT:USDT | below_1h_threshold | +2.17% | +3.08% |
| HEI/USDT:USDT | below_1h_threshold | +1.95% | +2.86% |
| IBMSTOCK/USDT:USDT | below_1h_threshold | +1.65% | +2.56% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.63% | +2.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
