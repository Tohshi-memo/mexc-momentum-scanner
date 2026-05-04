# Decision Report

- generated_at: 2026-05-04T11:12:28.196957+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3196**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3196, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.56% | **+0.31%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.91% | **+0.25%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.47% | **+1.33%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.23% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T11:12:26.158030+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78925.5
- Funnel: target 761 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +94.74% | $9,525,454.18 |
| SKYAI/USDT:USDT | +67.02% | $58,693,007.41 |
| GIGA/USDT:USDT | +58.43% | $1,717,359.94 |
| TAG/USDT:USDT | +49.64% | $14,982,920.50 |
| 4/USDT:USDT | +41.15% | $1,479,858.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.44% | +4.40% |
| LAB/USDT:USDT | below_1h_threshold | +3.60% | +3.56% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.54% | +3.50% |
| 4/USDT:USDT | below_1h_threshold | +2.78% | +2.74% |
| TRIA/USDT:USDT | below_1h_threshold | +1.68% | +1.64% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
