# Decision Report

- generated_at: 2026-05-04T03:02:36.805753+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3133**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3133, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_BB3S | 5/17 | 29.4% | +0.50% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.59% | **+1.81%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.39% | **+1.20%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.57% | **+0.87%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.02% | **+0.86%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.46% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T03:02:35.001564+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=79994.1
- Funnel: target 757 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +43.45% | $4,693,108.54 |
| SKYAI/USDT:USDT | +41.26% | $35,592,954.19 |
| LAB/USDT:USDT | +39.85% | $231,544,264.66 |
| GIGA/USDT:USDT | +28.97% | $1,103,725.39 |
| BSB/USDT:USDT | +27.55% | $14,789,964.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.17% | +2.34% |
| TST/USDT:USDT | below_1h_threshold | +1.69% | +1.86% |
| SIREN/USDT:USDT | below_1h_threshold | +0.99% | +1.16% |
| BSB/USDT:USDT | below_1h_threshold | +0.91% | +1.08% |
| LUNC/USDT:USDT | below_1h_threshold | +0.86% | +1.03% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
