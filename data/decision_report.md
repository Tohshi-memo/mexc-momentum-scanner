# Decision Report

- generated_at: 2026-05-19T23:28:44.354123+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4511**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4511, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +3.60% | **+1.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.35% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.73%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.31** / 初期 $100.00 (+23.31%)
- 確定: 476件 (Win 126 / Loss 165 / Flat 185) / skip 596件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROMPT/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $123.31

## 4. Latest Market Context

- 更新: 2026-05-19T23:28:42.326368+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=76852.0
- Funnel: target 760 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +42.47% | $10,913,847.81 |
| EDEN/USDT:USDT | +29.57% | $16,164,433.82 |
| LIT/USDT:USDT | +17.87% | $3,691,918.20 |
| BANANAS31/USDT:USDT | +13.00% | $1,388,707.98 |
| BSB/USDT:USDT | +11.92% | $35,525,925.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.36% | +4.13% |
| HOME/USDT:USDT | below_1h_threshold | +2.35% | +2.12% |
| FIDA/USDT:USDT | below_1h_threshold | +1.96% | +1.73% |
| PYTH/USDT:USDT | below_1h_threshold | +1.78% | +1.55% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.57% | +1.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
