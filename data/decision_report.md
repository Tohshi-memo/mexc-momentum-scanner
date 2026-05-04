# Decision Report

- generated_at: 2026-05-04T13:52:23.735539+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3209**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3209, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.57% | **-1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.38% | **+0.41%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.73% | **+2.61%** |
| ASK_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| MARKET_LONG | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.85% | **+1.99%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.91% | **+1.46%** |

## 2. $100 Live Portfolio

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定トレード: 13件 (TP 5 / SL 6 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.88
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T13:52:20.564849+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78802.4
- Funnel: target 761 → liquid 190 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=2, 4h RSI 93.9 >= 65=1, 4h RSI 87.6 >= 65=1, 4h RSI 78.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +136.43% | $14,749,044.64 |
| SKYAI/USDT:USDT | +93.48% | $75,835,658.14 |
| GIGA/USDT:USDT | +48.81% | $2,167,704.78 |
| 4/USDT:USDT | +39.37% | $1,757,565.49 |
| TAG/USDT:USDT | +31.10% | $16,543,797.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +4.43% | +4.46% |
| 4/USDT:USDT | below_1h_threshold | +3.91% | +3.93% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.89% | +3.91% |
| BR/USDT:USDT | below_1h_threshold | +3.52% | +3.54% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.49% | +3.51% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
