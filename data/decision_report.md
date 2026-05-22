# Decision Report

- generated_at: 2026-05-22T10:13:54.103344+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4683**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4683, expectancy=-0.09%
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
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.57% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/9 | 66.7% | +3.63% | **+2.42%** |
| ASK_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.47% | **+1.18%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.70** / 初期 $100.00 (+21.70%)
- 確定: 554件 (Win 140 / Loss 185 / Flat 229) / skip 690件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.70

## 4. Latest Market Context

- 更新: 2026-05-22T10:13:52.009644+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77296.4
- Funnel: target 768 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +46.59% | $3,490,364.05 |
| GENIUS/USDT:USDT | +34.32% | $1,379,739.15 |
| ALT/USDT:USDT | +31.63% | $1,571,437.59 |
| BEAT/USDT:USDT | +26.74% | $11,229,457.63 |
| NEAR/USDT:USDT | +22.20% | $107,316,985.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +4.85% | +4.81% |
| GENIUS/USDT:USDT | below_1h_threshold | +3.25% | +3.22% |
| EDEN/USDT:USDT | below_1h_threshold | +2.79% | +2.75% |
| GRASS/USDT:USDT | below_1h_threshold | +2.07% | +2.03% |
| AVNT/USDT:USDT | below_1h_threshold | +1.26% | +1.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
