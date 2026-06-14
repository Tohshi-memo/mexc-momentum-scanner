# Decision Report

- generated_at: 2026-06-14T16:48:44.481289+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6684**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=6684, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.14% | **+0.96%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.83% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.77** / 初期 $100.00 (+73.77%)
- 確定: 1557件 (Win 415 / Loss 493 / Flat 649) / skip 1688件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $173.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.97** / 初期 $100.00 (-1.03%)
- 確定: 66件 (Win 19 / Loss 13 / Flat 34) / skip 29件
- 成長率目線: 平均log -0.000157 / 幾何平均 -0.016% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.03% 残高後 $98.97

## 5. Latest Market Context

- 更新: 2026-06-14T16:48:38.569954+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64056.0
- Funnel: target 770 → liquid 128 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +6.65% | $1,820,169.43 |
| STG/USDT:USDT | +5.04% | $6,768,611.73 |
| CLO/USDT:USDT | +3.45% | $1,341,403.37 |
| TRADOOR/USDT:USDT | +3.37% | $9,309,920.19 |
| BLUAI/USDT:USDT | +2.91% | $1,341,281.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_relative_strength | +5.04% | +4.95% |
| CLO/USDT:USDT | below_1h_threshold | +3.56% | +3.47% |
| TRADOOR/USDT:USDT | below_1h_threshold | +3.37% | +3.28% |
| BLUAI/USDT:USDT | below_1h_threshold | +2.92% | +2.82% |
| MEGA/USDT:USDT | below_1h_threshold | +2.65% | +2.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
