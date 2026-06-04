# Decision Report

- generated_at: 2026-06-04T21:35:18.740548+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5672**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5672, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 3/15 | 20.0% | +2.12% | **+0.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.25% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.12% | **+1.65%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.87% | **+1.35%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.90% | **+1.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1225件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T21:35:15.990314+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=63399.9
- Funnel: target 770 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +37.26% | $6,104,814.46 |
| OPN/USDT:USDT | +32.04% | $38,198,479.37 |
| AAOISTOCK/USDT:USDT | +11.16% | $1,167,402.65 |
| XMR/USDT:USDT | +9.12% | $7,974,503.61 |
| HOME/USDT:USDT | +8.20% | $5,172,835.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.45% | +4.76% |
| XMR/USDT:USDT | below_1h_threshold | +3.69% | +4.00% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.55% | +0.87% |
| USOIL/USDT:USDT | below_1h_threshold | +0.25% | +0.56% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.20% | +0.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
