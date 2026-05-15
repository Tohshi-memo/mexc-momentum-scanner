# Decision Report

- generated_at: 2026-05-15T13:48:14.114871+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4340**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.22% / filled 20/20。**
- 全期間 MARKET基準: n=4340, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.36% | **+2.36%** |
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.40% | **+2.16%** |
| LIMIT_ATR | 15/20 | 75.0% | +2.47% | **+1.85%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.07% | **+1.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.44%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.52% | **+0.16%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.01% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.69** / 初期 $100.00 (-2.31%)
- 確定トレード: 46件 (TP 12 / SL 31 / EXP 3)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 511件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-15T13:48:10.591582+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.52% price=79127.4
- Funnel: target 764 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GWEI/USDT:USDT | +24.95% | $1,811,657.76 |
| IRYS/USDT:USDT | +23.90% | $9,010,571.26 |
| UP/USDT:USDT | +18.30% | $5,618,501.64 |
| PEAQ/USDT:USDT | +16.19% | $4,613,689.47 |
| FF/USDT:USDT | +12.61% | $2,709,432.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDSSTOCK/USDT:USDT | below_1h_threshold | +3.47% | +4.99% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.66% | +4.19% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.65% | +4.17% |
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +2.64% | +4.16% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.04% | +3.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
