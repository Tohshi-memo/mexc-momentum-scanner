# Decision Report

- generated_at: 2026-06-11T04:46:49.058188+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6299**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=6299, expectancy=-0.06%
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
| ASK | 20/20 | 100.0% | +1.42% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +5.21% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.04% | **-0.03%** |
| ASK_LONG | 20/20 | 100.0% | -0.05% | **-0.05%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1270件 (Win 319 / Loss 401 / Flat 550) / skip 1590件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T04:46:46.254656+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62664.7
- Funnel: target 785 → liquid 157 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.5 >= 65=1, 4h RSI 69.2 >= 65=1, 4h RSI 68.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +71.97% | $53,499,228.04 |
| AIO/USDT:USDT | +49.42% | $3,944,250.18 |
| BEAT/USDT:USDT | +35.36% | $199,213,499.89 |
| COLLECT/USDT:USDT | +32.07% | $1,382,324.01 |
| FIGHT/USDT:USDT | +24.84% | $1,196,985.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVNT/USDT:USDT | below_1h_threshold | +3.90% | +3.89% |
| FIGHT/USDT:USDT | below_1h_threshold | +2.54% | +2.52% |
| CRV/USDT:USDT | below_1h_threshold | +2.24% | +2.23% |
| ATOM/USDT:USDT | below_1h_threshold | +1.31% | +1.30% |
| RUNE/USDT:USDT | below_1h_threshold | +1.28% | +1.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
