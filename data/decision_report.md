# Decision Report

- generated_at: 2026-05-22T13:39:04.738460+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4698**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4698, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.46% | **+0.34%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.19% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.07% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.13** / 初期 $100.00 (+22.13%)
- 確定: 562件 (Win 143 / Loss 185 / Flat 234) / skip 697件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $122.13

## 4. Latest Market Context

- 更新: 2026-05-22T13:38:59.781547+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=77221.3
- Funnel: target 768 → liquid 136 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +56.01% | $4,184,427.88 |
| BEAT/USDT:USDT | +46.86% | $18,401,611.61 |
| GENIUS/USDT:USDT | +34.00% | $3,055,784.14 |
| ALT/USDT:USDT | +32.61% | $3,123,375.22 |
| NEAR/USDT:USDT | +28.40% | $147,211,323.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.99% | +4.34% |
| ONDO/USDT:USDT | below_1h_threshold | +2.98% | +3.33% |
| BUILDONBOB/USDT:USDT | below_1h_threshold | +2.80% | +3.15% |
| JTO/USDT:USDT | below_1h_threshold | +2.60% | +2.95% |
| GENIUS/USDT:USDT | below_1h_threshold | +2.49% | +2.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
