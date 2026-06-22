# Decision Report

- generated_at: 2026-06-22T12:51:01.532762+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7365**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=7365, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| ASK | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_BB3S | 5/18 | 27.8% | +2.57% | **+0.71%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.00% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.26% | **+0.17%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.17% | **+0.12%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.18% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$102.97** / 初期 $100.00 (+2.97%)
- 確定トレード: 27件 (TP 11 / SL 16 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.97
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$229.45** / 初期 $100.00 (+129.45%)
- 確定: 2033件 (Win 599 / Loss 669 / Flat 765) / skip 1893件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $229.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 464件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0429 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T12:50:55.585875+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.81% price=65149.9
- Funnel: target 808 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +77.72% | $17,222,683.97 |
| CLO/USDT:USDT | +27.76% | $3,230,829.95 |
| BEL/USDT:USDT | +25.25% | $1,410,683.06 |
| BTW/USDT:USDT | +22.39% | $41,719,598.01 |
| LAYER/USDT:USDT | +21.99% | $3,179,708.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.82% | +3.00% |
| ZRO/USDT:USDT | below_1h_threshold | +1.77% | +0.95% |
| W/USDT:USDT | below_1h_threshold | +1.74% | +0.93% |
| BILL/USDT:USDT | below_1h_threshold | +1.73% | +0.92% |
| SOXL/USDT:USDT | below_1h_threshold | +1.71% | +0.90% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
