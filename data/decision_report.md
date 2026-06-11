# Decision Report

- generated_at: 2026-06-11T17:05:40.026458+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6379**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=6379, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.50% | **+0.45%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.63% | **+0.44%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.57% | **+0.43%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.31% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.37** / 初期 $100.00 (+50.37%)
- 確定: 1296件 (Win 332 / Loss 412 / Flat 552) / skip 1644件
- 成長率目線: 平均log +0.000315 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $150.37

## 4. Latest Market Context

- 更新: 2026-06-11T17:05:37.267802+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=62435.5
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +8.47% | $9,701,896.04 |
| SIREN/USDT:USDT | +5.65% | $5,520,972.47 |
| UB/USDT:USDT | +5.38% | $1,393,304.41 |
| ESPORTS/USDT:USDT | +5.15% | $8,793,827.93 |
| VELVET/USDT:USDT | +3.80% | $92,501,445.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +2.08% | +2.26% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.32% | +1.50% |
| UB/USDT:USDT | below_1h_threshold | +1.14% | +1.31% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.08% | +1.26% |
| ID/USDT:USDT | below_1h_threshold | +0.93% | +1.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
