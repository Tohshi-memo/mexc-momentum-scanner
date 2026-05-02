# Decision Report

- generated_at: 2026-05-02T16:07:07.851672+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2943**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2943, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_5PCT | 11/20 | 55.0% | +2.23% | **+1.23%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.70% | **+0.85%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +6.78% | **+3.88%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.55% | **+1.91%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.44% | **+1.83%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.43% | **+1.29%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.94% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T16:07:03.319964+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78425.7
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1, 4h RSI 96.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +13.47% | $1,093,960.10 |
| TAG/USDT:USDT | +6.74% | $10,943,111.28 |
| LAB/USDT:USDT | +5.62% | $175,262,183.43 |
| ORDI/USDT:USDT | +4.73% | $19,460,119.07 |
| UB/USDT:USDT | +4.41% | $39,679,463.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +4.77% | +4.80% |
| UB/USDT:USDT | below_1h_threshold | +4.36% | +4.39% |
| BASED/USDT:USDT | below_1h_threshold | +3.79% | +3.82% |
| BRETT/USDT:USDT | below_1h_threshold | +2.55% | +2.58% |
| XNY/USDT:USDT | below_1h_threshold | +2.52% | +2.55% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
