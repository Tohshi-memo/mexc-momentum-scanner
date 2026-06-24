# Decision Report

- generated_at: 2026-06-24T13:07:17.076300+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7476**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7476, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.43% | **+1.43%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.07% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.09** / 初期 $100.00 (+131.09%)
- 確定: 2107件 (Win 624 / Loss 699 / Flat 784) / skip 1930件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $231.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.96** / 初期 $100.00 (+6.96%)
- 確定: 339件 (Win 96 / Loss 92 / Flat 151) / skip 548件
- 成長率目線: 平均log +0.000199 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0384 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.96

## 5. Latest Market Context

- 更新: 2026-06-24T13:07:11.565452+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.63% price=62194.2
- Funnel: target 808 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +43.29% | $6,433,071.91 |
| HEI/USDT:USDT | +42.01% | $17,984,997.24 |
| BAS/USDT:USDT | +36.47% | $2,365,016.97 |
| O/USDT:USDT | +28.98% | $5,091,548.25 |
| ID/USDT:USDT | +15.84% | $1,727,456.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.85% |
| O/USDT:USDT | below_1h_threshold | +1.63% | +2.26% |
| SYN/USDT:USDT | below_1h_threshold | +0.98% | +1.61% |
| SLX/USDT:USDT | below_1h_threshold | +0.79% | +1.42% |
| ID/USDT:USDT | below_1h_threshold | +0.37% | +1.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
