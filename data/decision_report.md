# Decision Report

- generated_at: 2026-06-15T04:45:57.242182+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6744**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6744, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.16% | **+1.10%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.14% | **+0.94%** |
| ASK | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.11% | **+0.89%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.16** / 初期 $100.00 (+72.16%)
- 確定: 1617件 (Win 423 / Loss 503 / Flat 691) / skip 1688件
- 成長率目線: 平均log +0.000336 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.50% 残高後 $172.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.84** / 初期 $100.00 (-0.16%)
- 確定: 111件 (Win 24 / Loss 18 / Flat 69) / skip 44件
- 成長率目線: 平均log -0.000014 / 幾何平均 -0.001% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0684 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.35% 残高後 $99.84

## 5. Latest Market Context

- 更新: 2026-06-15T04:45:49.784638+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=65628.5
- Funnel: target 770 → liquid 144 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +124.65% | $2,504,961.11 |
| EVAA/USDT:USDT | +72.24% | $19,255,365.88 |
| CLO/USDT:USDT | +33.18% | $2,099,754.37 |
| WLD/USDT:USDT | +18.91% | $105,829,599.05 |
| GRASS/USDT:USDT | +16.39% | $1,339,602.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +3.81% | +4.21% |
| WLD/USDT:USDT | below_1h_threshold | +2.87% | +3.27% |
| NIL/USDT:USDT | below_1h_threshold | +2.27% | +2.67% |
| JTO/USDT:USDT | below_1h_threshold | +2.08% | +2.48% |
| UAI/USDT:USDT | below_1h_threshold | +1.83% | +2.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
