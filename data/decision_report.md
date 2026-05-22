# Decision Report

- generated_at: 2026-05-22T09:24:02.704585+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4681**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4681, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.56% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +3.63% | **+2.18%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.87% | **+1.68%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.36% | **+1.66%** |
| ASK_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.55** / 初期 $100.00 (+21.55%)
- 確定: 552件 (Win 139 / Loss 185 / Flat 228) / skip 690件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.55

## 4. Latest Market Context

- 更新: 2026-05-22T09:24:00.283936+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77256.4
- Funnel: target 768 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +48.70% | $3,335,954.54 |
| ALT/USDT:USDT | +34.60% | $1,357,317.03 |
| GENIUS/USDT:USDT | +32.22% | $1,132,561.49 |
| NEAR/USDT:USDT | +27.24% | $95,522,218.59 |
| BEAT/USDT:USDT | +24.86% | $9,554,096.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +2.87% | +2.85% |
| ONDO/USDT:USDT | below_1h_threshold | +2.74% | +2.71% |
| BILL/USDT:USDT | below_1h_threshold | +2.69% | +2.66% |
| PEAQ/USDT:USDT | below_1h_threshold | +2.35% | +2.33% |
| EDEN/USDT:USDT | below_1h_threshold | +2.17% | +2.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
