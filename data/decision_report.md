# Decision Report

- generated_at: 2026-05-04T04:17:11.136109+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3146**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3146, expectancy=-0.17%
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
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.33% | **+0.53%** |
| LIMIT_BB3S | 5/15 | 33.3% | +1.17% | **+0.39%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.37% | **+1.17%** |
| ASK_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.03% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T04:17:08.690638+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=80393.6
- Funnel: target 756 → liquid 170 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1, 4h RSI 84.1 >= 65=1, 4h RSI 89.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +65.34% | $17,473,749.69 |
| LAB/USDT:USDT | +49.72% | $221,385,513.34 |
| TAG/USDT:USDT | +38.68% | $6,816,494.79 |
| SKYAI/USDT:USDT | +37.77% | $41,401,450.53 |
| TST/USDT:USDT | +36.29% | $6,150,159.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.16% | +4.01% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.62% | +2.48% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.61% | +2.47% |
| LAB/USDT:USDT | below_1h_threshold | +2.50% | +2.36% |
| UB/USDT:USDT | below_1h_threshold | +2.38% | +2.24% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
