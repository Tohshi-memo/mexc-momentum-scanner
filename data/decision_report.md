# Decision Report

- generated_at: 2026-07-03T01:59:36.044141+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8124**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=8124, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +2.21% | **+1.66%** |
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| ASK | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.97% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.26% | **+0.49%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.52% | **+0.28%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.18% | **+0.11%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.24% | **-0.06%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.11% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$285.42** / 初期 $100.00 (+185.42%)
- 確定: 2447件 (Win 755 / Loss 817 / Flat 875) / skip 2238件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $285.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.09** / 初期 $100.00 (+5.09%)
- 確定: 579件 (Win 140 / Loss 138 / Flat 301) / skip 956件
- 成長率目線: 平均log +0.000086 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GUA/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.35% 残高後 $105.09

## 5. Latest Market Context

- 更新: 2026-07-03T01:59:24.510151+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=61599.8
- Funnel: target 834 → liquid 170 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=2, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +24.20% | $1,977,875.67 |
| PIPPIN/USDT:USDT | +19.94% | $7,113,012.73 |
| LAB/USDT:USDT | +14.23% | $18,040,527.22 |
| MAGMA/USDT:USDT | +13.82% | $5,265,529.98 |
| WLD/USDT:USDT | +13.74% | $63,640,389.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_relative_strength | +5.48% | +4.96% |
| RAVE/USDT:USDT | below_relative_strength | +5.00% | +4.49% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.64% | +3.12% |
| VVV/USDT:USDT | below_1h_threshold | +3.57% | +3.05% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +3.49% | +2.97% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
