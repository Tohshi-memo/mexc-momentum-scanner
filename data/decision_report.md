# Decision Report

- generated_at: 2026-05-04T10:07:21.997033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3183**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3183, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/18 | 27.8% | +2.22% | **+0.62%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.43% | **+0.30%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.48% | **+0.99%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T10:07:19.957613+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.30% price=78759.5
- Funnel: target 761 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +58.98% | $51,686,099.47 |
| TST/USDT:USDT | +58.52% | $8,001,494.71 |
| TAG/USDT:USDT | +53.25% | $14,024,667.52 |
| GIGA/USDT:USDT | +45.96% | $1,394,570.91 |
| BSB/USDT:USDT | +32.64% | $26,213,652.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UKOIL/USDT:USDT | below_1h_threshold | +2.27% | +3.58% |
| USOIL/USDT:USDT | below_1h_threshold | +2.09% | +3.39% |
| BSB/USDT:USDT | below_1h_threshold | +1.45% | +2.75% |
| UB/USDT:USDT | below_1h_threshold | +1.44% | +2.75% |
| TAG/USDT:USDT | below_1h_threshold | +1.31% | +2.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
