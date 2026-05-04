# Decision Report

- generated_at: 2026-05-04T04:32:28.418481+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3148**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3148, expectancy=-0.17%
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
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.17% | **+0.45%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +2.04% | **+1.70%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.37% | **+1.17%** |
| ASK_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.03% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T04:32:23.123930+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=80325.0
- Funnel: target 756 → liquid 171 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1, 4h RSI 66.4 >= 65=1, 4h RSI 86.6 >= 65=1, 4h RSI 83.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +63.16% | $18,373,520.29 |
| LAB/USDT:USDT | +53.80% | $222,028,902.32 |
| TAG/USDT:USDT | +43.30% | $7,071,015.59 |
| SKYAI/USDT:USDT | +42.13% | $42,884,180.66 |
| GIGA/USDT:USDT | +34.32% | $1,140,692.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANANAS31/USDT:USDT | below_1h_threshold | +4.56% | +4.51% |
| GIGGLE/USDT:USDT | below_1h_threshold | +3.93% | +3.88% |
| UB/USDT:USDT | below_1h_threshold | +3.73% | +3.68% |
| BR/USDT:USDT | below_1h_threshold | +2.14% | +2.08% |
| TURBO/USDT:USDT | below_1h_threshold | +1.70% | +1.65% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
