# Decision Report

- generated_at: 2026-05-23T20:44:19.359269+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4798**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4798, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.08% | **-0.04%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.27% | **+2.78%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.63% | **+2.54%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.28% | **+2.35%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 743件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T20:44:12.962739+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.10% price=76788.4
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +24.48% | $1,299,857.55 |
| GRASS/USDT:USDT | +15.24% | $4,556,245.41 |
| GUA/USDT:USDT | +11.04% | $1,081,067.65 |
| NIL/USDT:USDT | +10.67% | $1,097,280.46 |
| EIGEN/USDT:USDT | +8.89% | $2,037,180.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLUAI/USDT:USDT | below_relative_strength | +5.87% | +4.76% |
| DYDX/USDT:USDT | below_relative_strength | +5.81% | +4.71% |
| NIL/USDT:USDT | below_1h_threshold | +4.92% | +3.82% |
| DOT/USDT:USDT | below_1h_threshold | +3.70% | +2.60% |
| ENA/USDT:USDT | below_1h_threshold | +3.63% | +2.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
