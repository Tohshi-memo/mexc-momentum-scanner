# Decision Report

- generated_at: 2026-06-09T16:26:09.668051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6148**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=6148, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.65% | **+1.32%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.85% | **+0.81%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.94% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.03% | **+0.72%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.06% | **+0.69%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.06% | **+0.59%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.93% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.01** / 初期 $100.00 (+48.01%)
- 確定: 1188件 (Win 297 / Loss 374 / Flat 517) / skip 1521件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $148.01

## 4. Latest Market Context

- 更新: 2026-06-09T16:26:04.022320+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=61068.2
- Funnel: target 778 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SIREN/USDT:USDT | +12.71% | $9,202,610.11 |
| H/USDT:USDT | +4.32% | $76,121,691.29 |
| CHZ/USDT:USDT | +2.83% | $10,366,936.02 |
| NEAR/USDT:USDT | +1.34% | $60,880,947.83 |
| POL/USDT:USDT | +0.99% | $1,334,024.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.32% | +4.38% |
| CHZ/USDT:USDT | below_1h_threshold | +2.91% | +2.97% |
| NEAR/USDT:USDT | below_1h_threshold | +1.35% | +1.41% |
| POL/USDT:USDT | below_1h_threshold | +1.00% | +1.06% |
| SAHARA/USDT:USDT | below_1h_threshold | +0.89% | +0.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
