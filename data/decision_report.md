# Decision Report

- generated_at: 2026-05-22T12:08:13.204570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4691**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4691, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.01% | **+0.01%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.12% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +1.02% | **+0.87%** |
| ASK_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.67% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.99** / 初期 $100.00 (+21.99%)
- 確定: 561件 (Win 142 / Loss 185 / Flat 234) / skip 691件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.99

## 4. Latest Market Context

- 更新: 2026-05-22T12:08:11.562691+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77408.2
- Funnel: target 768 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +46.56% | $3,900,548.61 |
| ALT/USDT:USDT | +41.42% | $2,525,172.02 |
| BEAT/USDT:USDT | +35.91% | $14,977,600.36 |
| GENIUS/USDT:USDT | +34.00% | $1,949,369.28 |
| GRASS/USDT:USDT | +24.17% | $6,895,484.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +2.79% | +2.77% |
| EDEN/USDT:USDT | below_1h_threshold | +1.82% | +1.81% |
| TIA/USDT:USDT | below_1h_threshold | +1.75% | +1.73% |
| INJ/USDT:USDT | below_1h_threshold | +1.71% | +1.69% |
| FET/USDT:USDT | below_1h_threshold | +0.86% | +0.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
