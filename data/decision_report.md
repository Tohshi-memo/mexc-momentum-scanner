# Decision Report

- generated_at: 2026-06-17T12:24:37.341776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6934**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=6934, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.02% | **+1.02%** |
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.61% | **+0.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.35% | **+0.26%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/12 | 50.0% | +2.21% | **+1.11%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.75% | **+0.88%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$196.78** / 初期 $100.00 (+96.78%)
- 確定: 1806件 (Win 491 / Loss 569 / Flat 746) / skip 1689件
- 成長率目線: 平均log +0.000375 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTER/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $196.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.31** / 初期 $100.00 (+1.31%)
- 確定: 207件 (Win 49 / Loss 46 / Flat 112) / skip 138件
- 成長率目線: 平均log +0.000063 / 幾何平均 +0.006% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0930 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTER/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.46% 残高後 $101.31

## 5. Latest Market Context

- 更新: 2026-06-17T12:24:30.216317+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=64644.5
- Funnel: target 788 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +60.96% | $9,744,970.71 |
| AGT/USDT:USDT | +59.91% | $1,264,521.92 |
| HIGH/USDT:USDT | +28.09% | $3,441,825.48 |
| BP/USDT:USDT | +24.18% | $1,048,771.23 |
| ID/USDT:USDT | +21.15% | $1,558,726.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.05% | +4.25% |
| AGT/USDT:USDT | below_1h_threshold | +3.11% | +3.31% |
| BP/USDT:USDT | below_1h_threshold | +2.87% | +3.07% |
| XPL/USDT:USDT | below_1h_threshold | +2.43% | +2.63% |
| GRASS/USDT:USDT | below_1h_threshold | +2.32% | +2.52% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
