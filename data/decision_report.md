# Decision Report

- generated_at: 2026-07-21T09:26:16.525344+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9168**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=9168, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_BB3S | 8/17 | 47.1% | +1.13% | **+0.53%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.92% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.43% | **+0.44%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$423.63** / 初期 $100.00 (+323.63%)
- 確定: 3230件 (Win 1015 / Loss 1030 / Flat 1185) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $423.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.71** / 初期 $100.00 (+31.71%)
- 確定: 1129件 (Win 301 / Loss 238 / Flat 590) / skip 1450件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0794 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 300件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T09:26:10.027006+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=66217.8
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +101.62% | $4,442,952.10 |
| ERA/USDT:USDT | +49.16% | $6,821,600.23 |
| ZHIPUSTOCK/USDT:USDT | +35.41% | $3,071,564.50 |
| ESPORTS/USDT:USDT | +14.86% | $5,515,947.70 |
| VVV/USDT:USDT | +11.02% | $1,900,484.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.84% | +3.81% |
| SNXX/USDT:USDT | below_1h_threshold | +2.52% | +2.50% |
| MVLL/USDT:USDT | below_1h_threshold | +2.22% | +2.19% |
| SOXL/USDT:USDT | below_1h_threshold | +2.15% | +2.12% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.10% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
