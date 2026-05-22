# Decision Report

- generated_at: 2026-05-22T13:54:16.638151+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4700**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4700, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.01% | **+0.00%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +0.33% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.13** / 初期 $100.00 (+22.13%)
- 確定: 562件 (Win 143 / Loss 185 / Flat 234) / skip 699件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $122.13

## 4. Latest Market Context

- 更新: 2026-05-22T13:54:10.500270+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=77222.3
- Funnel: target 768 → liquid 138 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.3 >= 65=1, 4h RSI 82.5 >= 65=1, 4h RSI 89.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +54.66% | $4,220,245.96 |
| BEAT/USDT:USDT | +51.52% | $19,361,017.02 |
| GENIUS/USDT:USDT | +41.62% | $3,263,777.82 |
| UB/USDT:USDT | +33.19% | $2,117,824.39 |
| ALT/USDT:USDT | +32.17% | $3,207,324.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.33% | +4.67% |
| AGT/USDT:USDT | below_1h_threshold | +4.15% | +4.49% |
| SPOTSTOCK/USDT:USDT | below_1h_threshold | +4.14% | +4.49% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +2.31% | +2.65% |
| BUILDONBOB/USDT:USDT | below_1h_threshold | +1.91% | +2.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
