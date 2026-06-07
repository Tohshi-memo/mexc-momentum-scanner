# Decision Report

- generated_at: 2026-06-07T00:17:06.826565+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5913**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=5913, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| ASK | 20/20 | 100.0% | +0.42% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +6.66% | **+4.44%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.35% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.98% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.94** / 初期 $100.00 (+37.94%)
- 確定: 1040件 (Win 250 / Loss 319 / Flat 471) / skip 1434件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $137.94

## 4. Latest Market Context

- 更新: 2026-06-07T00:17:01.368341+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=60823.0
- Funnel: target 771 → liquid 128 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +38.69% | $64,541,441.90 |
| SKYAI/USDT:USDT | +30.26% | $29,428,095.21 |
| BLESS/USDT:USDT | +27.52% | $1,958,999.71 |
| FIDA/USDT:USDT | +26.92% | $3,367,779.26 |
| BTW/USDT:USDT | +24.82% | $12,623,181.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.91% | +1.95% |
| BTW/USDT:USDT | below_1h_threshold | +1.82% | +1.86% |
| BLESS/USDT:USDT | below_1h_threshold | +1.13% | +1.17% |
| WLD/USDT:USDT | below_1h_threshold | +1.04% | +1.08% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.01% | +1.05% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
