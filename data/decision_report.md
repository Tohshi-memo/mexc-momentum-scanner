# Decision Report

- generated_at: 2026-05-11T16:07:46.035335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4053**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4053, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.31% | **+0.30%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.80% | **+0.63%** |
| ASK_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.38% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 396件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T16:07:43.006587+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=81486.4
- Funnel: target 762 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +4.25% | $1,118,873.51 |
| PENGUIN/USDT:USDT | +3.94% | $2,019,100.53 |
| BILL/USDT:USDT | +3.01% | $19,819,189.12 |
| BSB/USDT:USDT | +2.56% | $3,621,688.42 |
| B/USDT:USDT | +2.38% | $24,375,622.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LYN/USDT:USDT | below_1h_threshold | +4.39% | +4.29% |
| PENGUIN/USDT:USDT | below_1h_threshold | +3.94% | +3.84% |
| BILL/USDT:USDT | below_1h_threshold | +2.90% | +2.80% |
| BSB/USDT:USDT | below_1h_threshold | +2.56% | +2.46% |
| B/USDT:USDT | below_1h_threshold | +2.47% | +2.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
