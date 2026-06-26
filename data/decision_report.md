# Decision Report

- generated_at: 2026-06-26T10:00:44.481088+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7622**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=7622, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.59% | **+0.38%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.42% | **+0.36%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| ASK_LONG | 20/20 | 100.0% | +0.10% | **+0.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.31% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.93** / 初期 $100.00 (+120.93%)
- 確定: 2148件 (Win 631 / Loss 715 / Flat 802) / skip 2035件
- 成長率目線: 平均log +0.000369 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $220.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 382件 (Win 103 / Loss 100 / Flat 179) / skip 651件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T10:00:39.194234+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=59670.0
- Funnel: target 809 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ICNT/USDT:USDT | +40.20% | $1,558,036.38 |
| MAGMA/USDT:USDT | +36.92% | $1,425,157.69 |
| UB/USDT:USDT | +36.86% | $2,102,499.69 |
| AIN/USDT:USDT | +34.21% | $6,028,926.52 |
| G/USDT:USDT | +32.37% | $10,126,407.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| W/USDT:USDT | below_1h_threshold | +0.21% | +0.28% |
| VELVET/USDT:USDT | below_1h_threshold | +0.18% | +0.24% |
| ALLO/USDT:USDT | below_1h_threshold | +0.15% | +0.22% |
| BEAT/USDT:USDT | below_1h_threshold | +0.12% | +0.19% |
| G/USDT:USDT | below_1h_threshold | +0.12% | +0.18% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
