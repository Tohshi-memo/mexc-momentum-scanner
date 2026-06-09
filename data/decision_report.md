# Decision Report

- generated_at: 2026-06-09T16:01:46.560517+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6146**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=6146, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.65% | **+1.32%** |
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.96%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.94% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.98% | **+0.30%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.21% | **+0.13%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.17% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.50** / 初期 $100.00 (+49.50%)
- 確定: 1186件 (Win 297 / Loss 372 / Flat 517) / skip 1521件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $149.50

## 4. Latest Market Context

- 更新: 2026-06-09T16:01:43.977624+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=61139.4
- Funnel: target 778 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +1.83% | $75,613,641.20 |
| BTW/USDT:USDT | +1.04% | $3,626,943.16 |
| POWER/USDT:USDT | +0.83% | $4,953,409.34 |
| HOME/USDT:USDT | +0.79% | $3,638,687.86 |
| FOLKS/USDT:USDT | +0.68% | $2,329,074.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +1.65% | +1.59% |
| BTW/USDT:USDT | below_1h_threshold | +1.20% | +1.14% |
| POWER/USDT:USDT | below_1h_threshold | +0.83% | +0.77% |
| HOME/USDT:USDT | below_1h_threshold | +0.80% | +0.74% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.79% | +0.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
