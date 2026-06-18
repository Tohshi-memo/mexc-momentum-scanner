# Decision Report

- generated_at: 2026-06-18T16:48:42.351862+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7061**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.22% / filled 20/20。**
- 全期間 MARKET基準: n=7061, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |
| ASK | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.01% | **+1.61%** |
| LIMIT_BB3S | 6/20 | 30.0% | +5.11% | **+1.53%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.57% | **+1.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.70% | **+0.53%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.90% | **+0.45%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.11% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$100.46** / 初期 $100.00 (+0.46%)
- 確定トレード: 14件 (TP 5 / SL 9 / EXP 0)
- 最新: ALLO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$217.87** / 初期 $100.00 (+117.87%)
- 確定: 1883件 (Win 531 / Loss 601 / Flat 751) / skip 1739件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $217.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 164件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T16:48:28.123016+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.55% price=62681.9
- Funnel: target 795 → liquid 171 → pre 50 → checked 50 → surge 6 → strict 5
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +15.20% | $18,384,122.21 |
| BEAT/USDT:USDT | +8.89% | $55,685,034.25 |
| EVAA/USDT:USDT | +7.78% | $1,855,472.66 |
| ESPORTS/USDT:USDT | +7.10% | $50,990,211.28 |
| TAC/USDT:USDT | +5.87% | $2,266,590.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.47% | +3.92% |
| GRASS/USDT:USDT | below_1h_threshold | +4.37% | +3.83% |
| RE/USDT:USDT | below_1h_threshold | +4.24% | +3.69% |
| H/USDT:USDT | below_1h_threshold | +3.13% | +2.59% |
| USELESS/USDT:USDT | below_1h_threshold | +2.80% | +2.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
