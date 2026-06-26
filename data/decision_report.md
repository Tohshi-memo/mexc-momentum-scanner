# Decision Report

- generated_at: 2026-06-26T12:27:59.338105+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7625**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=7625, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.94% | **+0.71%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.85% | **-0.08%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.46% | **-0.23%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -1.30% | **-0.65%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.44** / 初期 $100.00 (+123.44%)
- 確定: 2151件 (Win 633 / Loss 715 / Flat 803) / skip 2035件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +1.00% 残高後 $223.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 382件 (Win 103 / Loss 100 / Flat 179) / skip 654件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T12:27:54.756142+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=59624.5
- Funnel: target 809 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ICNT/USDT:USDT | +44.84% | $2,292,102.40 |
| MAGMA/USDT:USDT | +44.57% | $2,812,581.00 |
| AIN/USDT:USDT | +22.32% | $6,598,591.35 |
| IDOL/USDT:USDT | +17.44% | $1,540,999.31 |
| BEAT/USDT:USDT | +17.06% | $47,288,733.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.94% | +3.55% |
| VELVET/USDT:USDT | below_1h_threshold | +3.17% | +2.78% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.52% | +2.13% |
| LAB/USDT:USDT | below_1h_threshold | +2.40% | +2.01% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.39% | +2.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
