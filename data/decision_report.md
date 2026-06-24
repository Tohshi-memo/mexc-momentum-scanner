# Decision Report

- generated_at: 2026-06-24T13:46:11.652771+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7478**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7478, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.55** / 初期 $100.00 (+132.55%)
- 確定: 2109件 (Win 625 / Loss 699 / Flat 785) / skip 1930件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $232.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.42** / 初期 $100.00 (+7.42%)
- 確定: 341件 (Win 97 / Loss 92 / Flat 152) / skip 548件
- 成長率目線: 平均log +0.000210 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0467 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $107.42

## 5. Latest Market Context

- 更新: 2026-06-24T13:46:06.898924+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.78% price=61476.6
- Funnel: target 808 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAS/USDT:USDT | +39.82% | $2,882,737.44 |
| HEI/USDT:USDT | +37.93% | $18,350,264.26 |
| SLX/USDT:USDT | +35.55% | $6,769,645.54 |
| SYN/USDT:USDT | +21.72% | $14,137,759.60 |
| O/USDT:USDT | +19.93% | $5,563,538.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +1.91% | +3.69% |
| CCLSTOCK/USDT:USDT | below_1h_threshold | +1.83% | +3.61% |
| LAB/USDT:USDT | below_1h_threshold | +1.64% | +3.42% |
| EVAA/USDT:USDT | below_1h_threshold | +1.42% | +3.19% |
| ALLO/USDT:USDT | below_1h_threshold | +1.18% | +2.96% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
