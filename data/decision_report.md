# Decision Report

- generated_at: 2026-05-23T21:04:06.816523+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4800**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4800, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.30% | **-1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.15% | **-0.07%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.12% | **+2.34%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.59% | **+2.15%** |
| ASK_LONG | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 745件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T21:04:04.387793+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=76922.0
- Funnel: target 764 → liquid 114 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +19.53% | $1,403,133.78 |
| GRASS/USDT:USDT | +17.44% | $4,628,970.44 |
| NIL/USDT:USDT | +13.24% | $1,207,789.43 |
| FIDA/USDT:USDT | +9.52% | $2,704,166.95 |
| ZEC/USDT:USDT | +9.02% | $520,108,647.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +0.44% | +0.87% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.30% | +0.72% |
| NEAR/USDT:USDT | below_1h_threshold | +0.29% | +0.71% |
| ZEC/USDT:USDT | below_1h_threshold | +0.01% | +0.43% |
| DOT/USDT:USDT | below_1h_threshold | -0.23% | +0.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
