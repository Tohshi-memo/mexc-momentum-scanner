# Decision Report

- generated_at: 2026-06-18T05:32:41.478604+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7007**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7007, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.42% | **+0.11%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.38% | **+0.10%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.22% | **+0.17%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$212.98** / 初期 $100.00 (+112.98%)
- 確定: 1853件 (Win 516 / Loss 586 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $212.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.74** / 初期 $100.00 (+4.74%)
- 確定: 280件 (Win 77 / Loss 74 / Flat 129) / skip 138件
- 成長率目線: 平均log +0.000165 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $104.74

## 5. Latest Market Context

- 更新: 2026-06-18T05:32:35.885798+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63906.6
- Funnel: target 793 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.4 >= 65=1, 4h RSI 83.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +97.42% | $36,391,842.91 |
| O/USDT:USDT | +56.84% | $2,229,980.81 |
| SYN/USDT:USDT | +55.68% | $4,771,718.88 |
| H/USDT:USDT | +34.79% | $32,422,527.98 |
| HOME/USDT:USDT | +31.91% | $1,790,366.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +3.97% | +3.88% |
| CLO/USDT:USDT | below_1h_threshold | +3.66% | +3.57% |
| RE/USDT:USDT | below_1h_threshold | +1.63% | +1.55% |
| UP/USDT:USDT | below_1h_threshold | +0.91% | +0.82% |
| MITO/USDT:USDT | below_1h_threshold | +0.76% | +0.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
