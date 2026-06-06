# Decision Report

- generated_at: 2026-06-06T16:04:44.233617+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5860**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5860, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +5.14% | **+1.54%** |
| LIMIT_9PCT | 5/20 | 25.0% | +5.95% | **+1.49%** |
| ASK | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1407件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T16:04:40.786332+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=60844.1
- Funnel: target 771 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +10.67% | $1,561,089.14 |
| BSB/USDT:USDT | +4.29% | $4,172,246.50 |
| BEAT/USDT:USDT | +2.42% | $32,603,202.21 |
| MBOX/USDT:USDT | +1.47% | $1,069,326.56 |
| HOME/USDT:USDT | +1.44% | $10,332,141.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.89% | +3.74% |
| BEAT/USDT:USDT | below_1h_threshold | +2.36% | +2.21% |
| HOME/USDT:USDT | below_1h_threshold | +1.63% | +1.48% |
| MBOX/USDT:USDT | below_1h_threshold | +1.48% | +1.33% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.47% | +1.32% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
