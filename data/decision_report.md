# Decision Report

- generated_at: 2026-06-24T10:49:06.450355+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7471**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7471, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.21% | **+0.16%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.50** / 初期 $100.00 (+130.50%)
- 確定: 2102件 (Win 622 / Loss 697 / Flat 783) / skip 1930件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $230.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.80** / 初期 $100.00 (+6.80%)
- 確定: 334件 (Win 94 / Loss 90 / Flat 150) / skip 548件
- 成長率目線: 平均log +0.000197 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0280 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: O/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.80

## 5. Latest Market Context

- 更新: 2026-06-24T10:48:58.300741+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=62513.1
- Funnel: target 808 → liquid 157 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +47.56% | $16,316,308.48 |
| SLX/USDT:USDT | +41.62% | $3,891,245.91 |
| SAHARA/USDT:USDT | +21.64% | $2,548,611.90 |
| ID/USDT:USDT | +20.31% | $1,741,176.82 |
| O/USDT:USDT | +19.96% | $1,343,417.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.51% | +3.74% |
| SLX/USDT:USDT | below_1h_threshold | +2.44% | +2.67% |
| AAVE/USDT:USDT | below_1h_threshold | +2.43% | +2.65% |
| LIGHT/USDT:USDT | below_1h_threshold | +2.02% | +2.24% |
| G/USDT:USDT | below_1h_threshold | +1.72% | +1.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
