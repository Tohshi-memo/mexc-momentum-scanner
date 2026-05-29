# Decision Report

- generated_at: 2026-05-29T23:24:46.898927+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5075**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=5075, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/19 | 47.4% | +1.43% | **+0.68%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.21% | **+1.03%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 896件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T23:24:44.392883+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=73331.1
- Funnel: target 773 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +25.79% | $1,279,851.50 |
| XLM/USDT:USDT | +22.61% | $381,797,061.87 |
| BASED/USDT:USDT | +14.91% | $2,287,047.55 |
| LAB/USDT:USDT | +14.08% | $126,519,362.69 |
| XMR/USDT:USDT | +7.29% | $7,377,597.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +2.68% | +2.84% |
| H/USDT:USDT | below_1h_threshold | +2.28% | +2.44% |
| HBAR/USDT:USDT | below_1h_threshold | +2.13% | +2.28% |
| APE/USDT:USDT | below_1h_threshold | +1.95% | +2.10% |
| ALGO/USDT:USDT | below_1h_threshold | +1.49% | +1.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
