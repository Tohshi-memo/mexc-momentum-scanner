# Decision Report

- generated_at: 2026-06-17T12:52:03.002920+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6938**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=6938, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.05% | **+1.05%** |
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +1.71% | **+0.93%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.63% | **+0.81%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.03** / 初期 $100.00 (+97.03%)
- 確定: 1810件 (Win 493 / Loss 571 / Flat 746) / skip 1689件
- 成長率目線: 平均log +0.000375 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $197.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.46** / 初期 $100.00 (+1.46%)
- 確定: 211件 (Win 51 / Loss 48 / Flat 112) / skip 138件
- 成長率目線: 平均log +0.000069 / 幾何平均 +0.007% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1002 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $101.46

## 5. Latest Market Context

- 更新: 2026-06-17T12:51:58.278493+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=64970.6
- Funnel: target 790 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.3 >= 65=1, 4h RSI 81.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +62.55% | $1,493,553.45 |
| ESPORTS/USDT:USDT | +61.23% | $10,719,251.17 |
| BP/USDT:USDT | +26.83% | $1,079,837.12 |
| HIGH/USDT:USDT | +25.55% | $3,543,890.42 |
| PLAY/USDT:USDT | +21.11% | $2,958,847.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BP/USDT:USDT | below_relative_strength | +5.19% | +4.88% |
| AGT/USDT:USDT | below_relative_strength | +5.04% | +4.74% |
| BLESS/USDT:USDT | below_1h_threshold | +4.37% | +4.07% |
| UNI/USDT:USDT | below_1h_threshold | +2.48% | +2.17% |
| GRASS/USDT:USDT | below_1h_threshold | +2.28% | +1.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
