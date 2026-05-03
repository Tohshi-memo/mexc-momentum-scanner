# Decision Report

- generated_at: 2026-05-03T16:52:05.287534+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3089**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3089, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.45% | **+0.87%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.92% | **+0.74%** |
| LIMIT_BB3S | 6/15 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.03% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.52% | **+0.99%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.67% | **+0.92%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.01% | **+0.91%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.06% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T16:51:57.509782+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78687.3
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +16.98% | $332,826,255.50 |
| SKYAI/USDT:USDT | +8.90% | $24,599,512.55 |
| AIOT/USDT:USDT | +7.16% | $2,321,729.06 |
| TST/USDT:USDT | +4.40% | $5,089,191.13 |
| ZEREBRO/USDT:USDT | +3.08% | $1,021,236.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +4.40% | +4.33% |
| BR/USDT:USDT | below_1h_threshold | +3.75% | +3.67% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.08% | +3.01% |
| BB/USDT:USDT | below_1h_threshold | +2.26% | +2.19% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.88% | +1.80% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
