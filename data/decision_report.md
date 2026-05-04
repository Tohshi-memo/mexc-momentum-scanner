# Decision Report

- generated_at: 2026-05-04T04:42:30.752255+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3150**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3150, expectancy=-0.18%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.65% | **+0.26%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +2.04% | **+1.70%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.12%** |
| ASK_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.25% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T04:42:22.943881+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80308.1
- Funnel: target 756 → liquid 173 → pre 50 → checked 50 → surge 7 → strict 2
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1, 4h RSI 65.4 >= 65=1, 4h RSI 84.0 >= 65=1, 4h RSI 87.2 >= 65=1, 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +70.19% | $19,369,877.00 |
| LAB/USDT:USDT | +56.78% | $222,741,598.58 |
| SKYAI/USDT:USDT | +46.21% | $43,784,389.73 |
| TAG/USDT:USDT | +38.35% | $7,197,905.33 |
| TST/USDT:USDT | +35.93% | $6,244,171.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANANAS31/USDT:USDT | below_1h_threshold | +3.25% | +3.22% |
| MERL/USDT:USDT | below_1h_threshold | +3.15% | +3.11% |
| GONGJIAN/USDT:USDT | below_1h_threshold | +3.12% | +3.09% |
| EDGE/USDT:USDT | below_1h_threshold | +2.36% | +2.33% |
| AIOT/USDT:USDT | below_1h_threshold | +1.96% | +1.93% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
