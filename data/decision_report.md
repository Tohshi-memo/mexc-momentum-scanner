# Decision Report

- generated_at: 2026-06-11T06:12:49.524857+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6314**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6314, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.94% | **+0.14%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 4/20 | 20.0% | -0.84% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.89% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.65% | **+0.99%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.92% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1270件 (Win 319 / Loss 401 / Flat 550) / skip 1605件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T06:12:46.432101+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=62716.1
- Funnel: target 785 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +136.48% | $60,116,287.65 |
| AIO/USDT:USDT | +59.00% | $4,789,598.14 |
| BEAT/USDT:USDT | +44.03% | $211,885,594.16 |
| COLLECT/USDT:USDT | +38.06% | $1,463,414.00 |
| H/USDT:USDT | +22.75% | $10,388,980.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_relative_strength | +5.17% | +4.96% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.58% | +4.37% |
| FOLKS/USDT:USDT | below_1h_threshold | +3.42% | +3.20% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.17% | +1.95% |
| H/USDT:USDT | below_1h_threshold | +2.02% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
