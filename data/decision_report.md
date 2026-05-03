# Decision Report

- generated_at: 2026-05-03T17:47:17.851410+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3093**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3093, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/17 | 23.5% | +3.70% | **+0.87%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.89% | **+0.85%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.79% | **+1.95%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.20% | **+1.76%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.64% | **+1.45%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.09% | **+1.39%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T17:47:11.974719+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=78751.2
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +29.01% | $315,190,155.28 |
| SKYAI/USDT:USDT | +18.74% | $24,085,654.85 |
| TST/USDT:USDT | +9.58% | $5,285,320.23 |
| ASTEROID/USDT:USDT | +4.88% | $2,076,574.42 |
| AIOT/USDT:USDT | +4.46% | $2,264,009.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +3.37% | +3.20% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.19% | +3.02% |
| TST/USDT:USDT | below_1h_threshold | +2.94% | +2.77% |
| SIREN/USDT:USDT | below_1h_threshold | +2.93% | +2.76% |
| AT/USDT:USDT | below_1h_threshold | +2.54% | +2.37% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
