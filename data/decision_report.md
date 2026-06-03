# Decision Report

- generated_at: 2026-06-03T06:02:17.823910+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5525**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5525, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.69% | **+0.41%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +4.09% | **+0.82%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.61% | **+0.42%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.64% | **+0.39%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.66% | **+0.33%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.56% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.38** / 初期 $100.00 (+31.38%)
- 確定: 980件 (Win 231 / Loss 301 / Flat 448) / skip 1106件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $131.38

## 4. Latest Market Context

- 更新: 2026-06-03T06:02:15.482526+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=67266.7
- Funnel: target 773 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +35.22% | $2,647,552.40 |
| PORTAL/USDT:USDT | +28.63% | $13,960,348.23 |
| GENIUS/USDT:USDT | +27.99% | $1,659,392.56 |
| LIT/USDT:USDT | +20.47% | $7,546,071.10 |
| APR/USDT:USDT | +20.23% | $1,267,427.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +1.89% | +1.93% |
| CLO/USDT:USDT | below_1h_threshold | +1.87% | +1.91% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.67% | +1.70% |
| MYX/USDT:USDT | below_1h_threshold | +0.94% | +0.97% |
| DYDX/USDT:USDT | below_1h_threshold | +0.63% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
