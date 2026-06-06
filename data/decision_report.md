# Decision Report

- generated_at: 2026-06-06T15:35:35.249562+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5856**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=5856, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| ASK | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.15% | **+0.69%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1403件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T15:35:32.147987+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=60684.1
- Funnel: target 771 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +119.41% | $76,000,301.05 |
| HEI/USDT:USDT | +70.26% | $4,867,969.70 |
| VELVET/USDT:USDT | +51.88% | $4,017,033.42 |
| BLUAI/USDT:USDT | +32.95% | $6,568,453.75 |
| SKYAI/USDT:USDT | +32.81% | $5,159,540.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLUAI/USDT:USDT | below_1h_threshold | +3.65% | +3.77% |
| VELVET/USDT:USDT | below_1h_threshold | +3.06% | +3.19% |
| ALLO/USDT:USDT | below_1h_threshold | +3.06% | +3.19% |
| BEAT/USDT:USDT | below_1h_threshold | +2.20% | +2.33% |
| LIT/USDT:USDT | below_1h_threshold | +1.83% | +1.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
