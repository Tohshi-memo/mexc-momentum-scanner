# Decision Report

- generated_at: 2026-05-19T07:33:34.890049+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4464**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4464, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.25% | **+0.87%** |
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.36%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.51% | **+1.21%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +1.55% | **+0.78%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.01% | **+0.50%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.26% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.06** / 初期 $100.00 (+23.06%)
- 確定: 461件 (Win 122 / Loss 158 / Flat 181) / skip 564件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $123.06

## 4. Latest Market Context

- 更新: 2026-05-19T07:33:32.384114+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=77139.8
- Funnel: target 768 → liquid 140 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.7 >= 65=1, 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +27.87% | $8,777,481.82 |
| EDEN/USDT:USDT | +23.21% | $2,053,029.47 |
| PLAY/USDT:USDT | +20.43% | $1,992,835.66 |
| SPACE/USDT:USDT | +13.55% | $1,007,840.25 |
| ONDO/USDT:USDT | +13.45% | $53,292,076.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +1.99% | +1.79% |
| HYPE/USDT:USDT | below_1h_threshold | +1.33% | +1.13% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.98% | +0.78% |
| NEAR/USDT:USDT | below_1h_threshold | +0.73% | +0.53% |
| ONT/USDT:USDT | below_1h_threshold | +0.64% | +0.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
