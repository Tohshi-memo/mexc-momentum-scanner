# Decision Report

- generated_at: 2026-05-04T20:17:24.701043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3256**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3256, expectancy=-0.18%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.96% | **+0.53%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.54% | **+0.51%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.91% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.84% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.80% | **+1.96%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.72% | **+0.94%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.59% | **+0.63%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T20:17:22.462073+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80092.7
- Funnel: target 760 → liquid 199 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +59.46% | $28,692,640.35 |
| TST/USDT:USDT | +12.85% | $22,447,442.86 |
| SKYAI/USDT:USDT | +9.37% | $99,849,239.29 |
| LUNC/USDT:USDT | +6.43% | $70,807,385.97 |
| FHE/USDT:USDT | +6.36% | $2,589,201.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +2.18% | +2.09% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.56% | +1.46% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.03% | +0.94% |
| AIOZ/USDT:USDT | below_1h_threshold | +0.99% | +0.90% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.72% | +0.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
