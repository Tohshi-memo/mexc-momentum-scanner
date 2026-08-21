# Decision Report

- generated_at: 2026-08-21T16:01:29.373488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12210**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=12210, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.29% | **+0.26%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | -0.05% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 189件 (TP 72 / SL 112 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4362件 (Win 1337 / Loss 1434 / Flat 1591) / skip 4409件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.28** / 初期 $100.00 (+54.28%)
- 確定: 1826件 (Win 503 / Loss 430 / Flat 893) / skip 3795件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1866件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000236 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T16:01:19.058187+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77275.3
- Funnel: target 1018 → liquid 209 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +3.55% | $46,678,938.40 |
| ALIGN/USDT:USDT | +1.29% | $1,002,012.98 |
| PROM/USDT:USDT | +0.85% | $2,050,386.88 |
| ENA/USDT:USDT | +0.83% | $185,716,639.01 |
| USELESS/USDT:USDT | +0.74% | $3,167,454.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.80% | +3.73% |
| ALIGN/USDT:USDT | below_1h_threshold | +1.02% | +0.95% |
| SCRT/USDT:USDT | below_1h_threshold | +0.93% | +0.86% |
| ENA/USDT:USDT | below_1h_threshold | +0.90% | +0.83% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.89% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
