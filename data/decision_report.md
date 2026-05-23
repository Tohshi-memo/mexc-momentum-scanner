# Decision Report

- generated_at: 2026-05-23T11:29:35.881744+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4773**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.22% / filled 20/20。**
- 全期間 MARKET基準: n=4773, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.22% | **+1.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.34% | **+1.34%** |
| MARKET | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.20% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.26% | **+0.22%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.47% | **+0.21%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 718件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T11:29:33.013018+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=74822.3
- Funnel: target 764 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +153.78% | $79,664,465.07 |
| BEAT/USDT:USDT | +27.80% | $68,502,682.68 |
| IN/USDT:USDT | +21.57% | $2,089,434.49 |
| GMTTOKEN/USDT:USDT | +18.19% | $2,804,776.58 |
| SKYAI/USDT:USDT | +12.21% | $2,236,151.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.00% | +1.81% |
| GMTTOKEN/USDT:USDT | below_1h_threshold | +1.63% | +1.44% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.29% | +1.10% |
| RIVER/USDT:USDT | below_1h_threshold | +1.25% | +1.06% |
| IN/USDT:USDT | below_1h_threshold | +1.10% | +0.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
