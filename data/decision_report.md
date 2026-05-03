# Decision Report

- generated_at: 2026-05-03T08:36:59.739755+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3053**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3053, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.98% | **+0.40%** |
| LIMIT_BB3S | 10/13 | 76.9% | +0.39% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.80% | **+1.96%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +3.07% | **+1.84%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.55% | **+1.78%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.43% | **+1.09%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T08:36:57.754689+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=78374.6
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 98.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +73.26% | $11,059,131.62 |
| BR/USDT:USDT | +21.84% | $3,806,487.50 |
| TAC/USDT:USDT | +20.61% | $2,741,419.59 |
| AIGENSYN/USDT:USDT | +19.56% | $3,363,830.27 |
| FHE/USDT:USDT | +17.46% | $2,855,436.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.55% | +4.47% |
| TAC/USDT:USDT | below_1h_threshold | +3.74% | +3.66% |
| B/USDT:USDT | below_1h_threshold | +3.58% | +3.50% |
| ALCH/USDT:USDT | below_1h_threshold | +3.11% | +3.04% |
| BSB/USDT:USDT | below_1h_threshold | +2.75% | +2.67% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
