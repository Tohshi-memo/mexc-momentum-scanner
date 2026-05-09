# Decision Report

- generated_at: 2026-05-09T16:22:34.397301+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3897**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3897, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/16 | 43.8% | +1.38% | **+0.61%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.48% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.13% | **+0.85%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |
| MARKET_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.92% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 263件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T16:22:31.103125+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=80630.3
- Funnel: target 769 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +24.32% | $22,844,367.42 |
| OFC/USDT:USDT | +4.77% | $1,055,971.00 |
| BIO/USDT:USDT | +3.38% | $1,266,133.80 |
| BRETT/USDT:USDT | +3.09% | $2,261,008.05 |
| SIREN/USDT:USDT | +2.50% | $20,567,788.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OFC/USDT:USDT | below_1h_threshold | +4.77% | +4.59% |
| BIO/USDT:USDT | below_1h_threshold | +3.39% | +3.21% |
| BRETT/USDT:USDT | below_1h_threshold | +3.10% | +2.92% |
| SIREN/USDT:USDT | below_1h_threshold | +2.65% | +2.48% |
| RAVE/USDT:USDT | below_1h_threshold | +2.50% | +2.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
