# Decision Report

- generated_at: 2026-05-04T02:47:07.315258+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3130**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3130, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.56% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.33% | **+1.40%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.75% | **+1.37%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.58% | **+1.03%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.35% | **+1.01%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.21% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T02:47:02.593855+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=80031.1
- Funnel: target 757 → liquid 166 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1, 4h RSI 78.4 >= 65=1, 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +44.95% | $35,833,243.61 |
| TAG/USDT:USDT | +39.14% | $4,495,279.75 |
| LAB/USDT:USDT | +38.96% | $241,631,863.47 |
| GIGA/USDT:USDT | +25.59% | $1,103,369.70 |
| BSB/USDT:USDT | +21.81% | $14,961,529.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +2.57% | +2.21% |
| MONAD/USDT:USDT | below_1h_threshold | +2.49% | +2.13% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.11% | +1.76% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.00% | +1.64% |
| ENA/USDT:USDT | below_1h_threshold | +1.96% | +1.60% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
