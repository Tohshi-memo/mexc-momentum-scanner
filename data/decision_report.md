# Decision Report

- generated_at: 2026-06-11T01:42:01.566593+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6290**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=6290, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.76% | **+1.41%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.81% | **+1.40%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.45% | **+0.36%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.93% | **+0.29%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.41% | **+0.28%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1270件 (Win 319 / Loss 401 / Flat 550) / skip 1581件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T01:41:55.064776+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.74% price=62249.4
- Funnel: target 785 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +102.71% | $45,689,958.73 |
| AIO/USDT:USDT | +65.38% | $1,243,555.11 |
| BEAT/USDT:USDT | +29.48% | $189,855,943.50 |
| FIGHT/USDT:USDT | +17.56% | $1,078,552.72 |
| H/USDT:USDT | +11.29% | $11,741,236.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +4.08% | +3.34% |
| BSB/USDT:USDT | below_1h_threshold | +2.75% | +2.01% |
| BEAT/USDT:USDT | below_1h_threshold | +2.74% | +2.00% |
| CRV/USDT:USDT | below_1h_threshold | +2.49% | +1.75% |
| RUNE/USDT:USDT | below_1h_threshold | +2.38% | +1.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
