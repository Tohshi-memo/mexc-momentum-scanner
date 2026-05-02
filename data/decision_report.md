# Decision Report

- generated_at: 2026-05-02T16:02:26.389538+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2942**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2942, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_5PCT | 12/20 | 60.0% | +2.13% | **+1.28%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.70% | **+0.85%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +6.78% | **+3.88%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.35% | **+2.51%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.90% | **+2.03%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.94% | **+1.76%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.93% | **+1.74%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T16:02:24.302222+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78439.9
- Funnel: target 755 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +5.32% | $10,809,320.57 |
| ORDI/USDT:USDT | +3.30% | $18,655,649.51 |
| NAORIS/USDT:USDT | +2.15% | $4,449,165.85 |
| ASTEROID/USDT:USDT | +1.78% | $2,476,144.65 |
| ORCA/USDT:USDT | +1.59% | $5,614,577.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +3.46% | +3.48% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.15% | +2.17% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.79% | +1.80% |
| BIO/USDT:USDT | below_1h_threshold | +1.76% | +1.77% |
| BRETT/USDT:USDT | below_1h_threshold | +1.62% | +1.63% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
