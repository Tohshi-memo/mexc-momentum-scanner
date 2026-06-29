# Decision Report

- generated_at: 2026-06-29T14:37:04.030751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7821**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=7821, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.35% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.83% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.97% | **+0.79%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +0.53% | **+0.41%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.14** / 初期 $100.00 (+2.14%)
- 確定トレード: 42件 (TP 15 / SL 26 / EXP 1)
- 最新: G/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$263.87** / 初期 $100.00 (+163.87%)
- 確定: 2325件 (Win 708 / Loss 774 / Flat 843) / skip 2057件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $263.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 775件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T14:36:56.953651+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=59541.2
- Funnel: target 810 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +166.96% | $33,060,933.56 |
| RAVE/USDT:USDT | +38.36% | $45,087,657.73 |
| GWEI/USDT:USDT | +36.11% | $2,870,120.12 |
| G/USDT:USDT | +26.89% | $2,825,066.82 |
| UB/USDT:USDT | +26.00% | $2,621,480.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +3.41% | +3.44% |
| RAVE/USDT:USDT | below_1h_threshold | +3.23% | +3.26% |
| AGLD/USDT:USDT | below_1h_threshold | +3.10% | +3.13% |
| BEAT/USDT:USDT | below_1h_threshold | +3.01% | +3.04% |
| ORDI/USDT:USDT | below_1h_threshold | +2.37% | +2.40% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
