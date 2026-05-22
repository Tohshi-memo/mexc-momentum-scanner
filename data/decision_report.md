# Decision Report

- generated_at: 2026-05-22T10:58:59.392553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4688**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4688, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.46% | **+0.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +3.02% | **+2.26%** |
| ASK_LONG | 20/20 | 100.0% | +1.90% | **+1.90%** |
| MARKET_LONG | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.04% | **+1.43%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +1.40% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.99** / 初期 $100.00 (+21.99%)
- 確定: 558件 (Win 142 / Loss 185 / Flat 231) / skip 691件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $121.99

## 4. Latest Market Context

- 更新: 2026-05-22T10:58:56.521448+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77279.4
- Funnel: target 768 → liquid 142 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.8 >= 65=1, 4h RSI 83.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +53.54% | $3,681,840.52 |
| ALT/USDT:USDT | +35.77% | $1,851,477.24 |
| EDEN/USDT:USDT | +33.65% | $22,130,743.07 |
| GENIUS/USDT:USDT | +32.81% | $1,565,651.85 |
| BEAT/USDT:USDT | +30.11% | $12,827,389.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.76% | +3.75% |
| ALT/USDT:USDT | below_1h_threshold | +3.61% | +3.60% |
| PLAY/USDT:USDT | below_1h_threshold | +3.36% | +3.34% |
| GRASS/USDT:USDT | below_1h_threshold | +3.34% | +3.32% |
| BEAT/USDT:USDT | below_1h_threshold | +3.07% | +3.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
