# Decision Report

- generated_at: 2026-06-11T09:35:38.329712+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6333**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6333, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| ASK | 20/20 | 100.0% | +0.10% | **+0.10%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.96% | **+0.29%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1271件 (Win 319 / Loss 401 / Flat 551) / skip 1623件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T09:35:34.783717+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62933.7
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIO/USDT:USDT | +77.74% | $6,167,178.66 |
| VELVET/USDT:USDT | +74.08% | $74,101,197.33 |
| H/USDT:USDT | +49.36% | $13,099,795.08 |
| BEAT/USDT:USDT | +46.84% | $217,471,666.07 |
| COLLECT/USDT:USDT | +43.17% | $1,771,322.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIO/USDT:USDT | below_1h_threshold | +4.47% | +4.46% |
| HOME/USDT:USDT | below_1h_threshold | +2.83% | +2.81% |
| PYTH/USDT:USDT | below_1h_threshold | +2.12% | +2.11% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.40% | +1.39% |
| BSB/USDT:USDT | below_1h_threshold | +1.26% | +1.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
