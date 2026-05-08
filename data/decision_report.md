# Decision Report

- generated_at: 2026-05-08T17:32:48.178981+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3811**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=3811, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| ASK | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.64% | **+0.55%** |
| LIMIT_BB3S | 3/14 | 21.4% | +0.68% | **+0.14%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.86% | **+0.43%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.15% | **+0.06%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.01% | **+0.01%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.44% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 180件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T17:32:45.016701+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.46% price=80133.2
- Funnel: target 768 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INTCSTOCK/USDT:USDT | +7.39% | $8,204,064.29 |
| JUP/USDT:USDT | +7.32% | $4,339,609.14 |
| CHIP/USDT:USDT | +7.22% | $49,436,590.12 |
| COLLECT/USDT:USDT | +7.04% | $1,468,269.87 |
| SPORTFUN/USDT:USDT | +6.61% | $1,455,978.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OP/USDT:USDT | below_1h_threshold | +4.56% | +4.10% |
| SATO/USDT:USDT | below_1h_threshold | +3.90% | +3.44% |
| LINEA/USDT:USDT | below_1h_threshold | +3.62% | +3.17% |
| IO/USDT:USDT | below_1h_threshold | +3.33% | +2.88% |
| ARB/USDT:USDT | below_1h_threshold | +3.11% | +2.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
