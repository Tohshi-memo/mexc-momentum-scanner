# Decision Report

- generated_at: 2026-06-24T10:57:04.231527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7472**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7472, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.71% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.50** / 初期 $100.00 (+130.50%)
- 確定: 2103件 (Win 622 / Loss 697 / Flat 784) / skip 1930件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $230.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.80** / 初期 $100.00 (+6.80%)
- 確定: 335件 (Win 94 / Loss 90 / Flat 151) / skip 548件
- 成長率目線: 平均log +0.000196 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0327 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: O/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.80

## 5. Latest Market Context

- 更新: 2026-06-24T10:56:58.416085+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=62427.7
- Funnel: target 808 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +45.41% | $16,423,120.22 |
| SLX/USDT:USDT | +43.82% | $3,983,754.22 |
| O/USDT:USDT | +26.28% | $1,569,792.53 |
| SAHARA/USDT:USDT | +22.26% | $2,580,396.04 |
| ID/USDT:USDT | +19.22% | $1,751,646.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +4.48% | +4.83% |
| SLX/USDT:USDT | below_1h_threshold | +4.04% | +4.40% |
| LIGHT/USDT:USDT | below_1h_threshold | +3.24% | +3.60% |
| AAVE/USDT:USDT | below_1h_threshold | +2.47% | +2.83% |
| UNI/USDT:USDT | below_1h_threshold | +1.83% | +2.19% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
