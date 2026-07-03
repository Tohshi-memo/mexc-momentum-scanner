# Decision Report

- generated_at: 2026-07-03T18:41:17.288655+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8184**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=8184, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.11% | **+0.95%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.52% | **+0.26%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.72% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.98% | **+0.15%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.14% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$289.07** / 初期 $100.00 (+189.07%)
- 確定: 2503件 (Win 769 / Loss 833 / Flat 901) / skip 2242件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NEX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $289.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 984件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T18:41:11.916685+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=62199.6
- Funnel: target 834 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TA/USDT:USDT | +30.04% | $1,534,362.88 |
| MAGMA/USDT:USDT | +28.56% | $9,581,168.69 |
| TLM/USDT:USDT | +11.41% | $16,708,160.60 |
| VELVET/USDT:USDT | +10.55% | $29,055,390.23 |
| BASED/USDT:USDT | +7.11% | $8,455,807.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.63% | +4.58% |
| NOM/USDT:USDT | below_1h_threshold | +4.18% | +4.14% |
| TLM/USDT:USDT | below_1h_threshold | +2.58% | +2.53% |
| GPS/USDT:USDT | below_1h_threshold | +2.57% | +2.53% |
| ADA/USDT:USDT | below_1h_threshold | +2.39% | +2.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
