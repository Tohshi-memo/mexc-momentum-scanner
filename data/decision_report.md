# Decision Report

- generated_at: 2026-06-09T11:57:47.950041+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6133**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=6133, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.67% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.64% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.84% | **+0.43%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.75% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.12% | **+0.79%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.26% | **+0.76%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.89% | **+0.49%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.19% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.90** / 初期 $100.00 (+51.90%)
- 確定: 1173件 (Win 294 / Loss 365 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $151.90

## 4. Latest Market Context

- 更新: 2026-06-09T11:57:41.618112+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=62590.5
- Funnel: target 774 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +51.71% | $21,903,126.88 |
| SLX/USDT:USDT | +31.05% | $5,272,925.15 |
| POWER/USDT:USDT | +24.00% | $2,645,100.77 |
| PLAY/USDT:USDT | +17.56% | $1,974,975.80 |
| SKHYNIXSTOCK/USDT:USDT | +11.95% | $4,544,133.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWER/USDT:USDT | below_1h_threshold | +4.53% | +4.79% |
| BSB/USDT:USDT | below_1h_threshold | +3.64% | +3.90% |
| CHZ/USDT:USDT | below_1h_threshold | +3.53% | +3.78% |
| PLAY/USDT:USDT | below_1h_threshold | +3.39% | +3.64% |
| SLX/USDT:USDT | below_1h_threshold | +3.23% | +3.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
