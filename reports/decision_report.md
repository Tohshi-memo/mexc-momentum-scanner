# Decision Report

- generated_at: 2026-06-24T14:42:26.959199+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7481**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7481, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.45% | **+1.45%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.18% | **+0.18%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.07% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.68** / 初期 $100.00 (+131.68%)
- 確定: 2112件 (Win 626 / Loss 701 / Flat 785) / skip 1930件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $231.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.13** / 初期 $100.00 (+7.13%)
- 確定: 344件 (Win 98 / Loss 94 / Flat 152) / skip 548件
- 成長率目線: 平均log +0.000200 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0468 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $107.13

## 5. Latest Market Context

- 更新: 2026-06-24T14:33:12.124254+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=61309.3
- Funnel: target 808 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +38.50% | $18,612,379.05 |
| BAS/USDT:USDT | +35.22% | $3,818,420.97 |
| SLX/USDT:USDT | +30.06% | $7,365,071.58 |
| SYN/USDT:USDT | +23.58% | $15,178,496.45 |
| SAHARA/USDT:USDT | +19.69% | $3,207,002.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| G/USDT:USDT | below_1h_threshold | +2.35% | +2.35% |
| JUP/USDT:USDT | below_1h_threshold | +1.92% | +1.92% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.88% | +1.88% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.80% | +1.80% |
| RAVE/USDT:USDT | below_1h_threshold | +1.72% | +1.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
