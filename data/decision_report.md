# Decision Report

- generated_at: 2026-05-22T16:43:57.314210+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4717**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=4717, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.24% | **+1.06%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.02% | **+0.82%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.81% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +2.07% | **+0.62%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.61% | **+0.56%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | -0.06% | **-0.03%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.31% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.06** / 初期 $100.00 (+21.06%)
- 確定: 565件 (Win 144 / Loss 187 / Flat 234) / skip 713件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $121.06

## 4. Latest Market Context

- 更新: 2026-05-22T16:43:55.016354+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=76857.0
- Funnel: target 768 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +7.38% | $26,531,033.87 |
| GENIUS/USDT:USDT | +4.41% | $5,090,376.16 |
| BUILDONBOB/USDT:USDT | +3.61% | $5,621,471.92 |
| PEAQ/USDT:USDT | +2.86% | $1,309,298.70 |
| UB/USDT:USDT | +2.56% | $2,316,991.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +4.54% | +4.41% |
| BUILDONBOB/USDT:USDT | below_1h_threshold | +3.62% | +3.48% |
| PEAQ/USDT:USDT | below_1h_threshold | +2.87% | +2.74% |
| UB/USDT:USDT | below_1h_threshold | +2.50% | +2.37% |
| USELESS/USDT:USDT | below_1h_threshold | +2.06% | +1.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
