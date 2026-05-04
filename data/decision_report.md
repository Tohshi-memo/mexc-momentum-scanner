# Decision Report

- generated_at: 2026-05-04T04:02:38.307678+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3141**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3141, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.61% | **-0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.29% | **+0.58%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_6PCT | 9/20 | 45.0% | +0.58% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| MARKET_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.37% | **+1.17%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.73% | **+1.13%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.07% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T04:02:36.072392+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80349.2
- Funnel: target 756 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1, 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +71.74% | $39,108,075.47 |
| BSB/USDT:USDT | +56.00% | $16,765,551.75 |
| TAG/USDT:USDT | +48.06% | $6,529,717.13 |
| LAB/USDT:USDT | +46.94% | $220,666,669.07 |
| TST/USDT:USDT | +28.26% | $6,065,288.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +1.74% | +1.66% |
| UB/USDT:USDT | below_1h_threshold | +1.74% | +1.65% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.51% | +1.42% |
| LAB/USDT:USDT | below_1h_threshold | +1.13% | +1.04% |
| RENDER/USDT:USDT | below_1h_threshold | +0.97% | +0.88% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
