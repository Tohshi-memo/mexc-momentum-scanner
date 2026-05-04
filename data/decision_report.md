# Decision Report

- generated_at: 2026-05-04T10:17:33.237209+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3187**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3187, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/19 | 31.6% | +2.97% | **+0.94%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.50% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.56% | **+0.78%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.11% | **+0.55%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.36% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T10:17:28.774866+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.39% price=78692.1
- Funnel: target 761 → liquid 183 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.6 >= 65=1, 4h RSI 91.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +69.88% | $8,249,529.18 |
| SKYAI/USDT:USDT | +63.48% | $53,176,906.82 |
| TAG/USDT:USDT | +53.64% | $14,210,527.93 |
| GIGA/USDT:USDT | +52.25% | $1,449,007.29 |
| BSB/USDT:USDT | +30.48% | $26,371,703.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UKOIL/USDT:USDT | below_1h_threshold | +3.80% | +5.19% |
| USOIL/USDT:USDT | below_1h_threshold | +3.68% | +5.07% |
| TRIA/USDT:USDT | below_1h_threshold | +2.28% | +3.67% |
| TAG/USDT:USDT | below_1h_threshold | +1.82% | +3.21% |
| LUNC/USDT:USDT | below_1h_threshold | +1.58% | +2.97% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
