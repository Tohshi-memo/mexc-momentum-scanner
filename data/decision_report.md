# Decision Report

- generated_at: 2026-09-19T01:36:29.387950+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14972**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.12% / filled 20/20。**
- 全期間 MARKET基準: n=14972, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.57% | **+1.33%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.99% | **+0.69%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.50% | **+0.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,189.35** / 初期 $100.00 (+1089.35%)
- 確定: 5625件 (Win 1687 / Loss 1823 / Flat 2115) / skip 5908件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,189.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.98** / 初期 $100.00 (+139.98%)
- 確定: 3176件 (Win 878 / Loss 759 / Flat 1539) / skip 5207件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $239.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 2962件 (Win 879 / Loss 1167 / Flat 916) / pending 0件 / skip 3484件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000385 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.52

## 6. Latest Market Context

- 更新: 2026-09-19T01:36:17.560020+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.72% price=81056.0
- Funnel: target 1050 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +75.03% | $36,289,275.96 |
| ONE/USDT:USDT | +30.69% | $25,401,927.88 |
| SYN/USDT:USDT | +22.26% | $6,958,063.79 |
| SAGA/USDT:USDT | +21.65% | $4,246,484.84 |
| MAGMA/USDT:USDT | +21.45% | $1,255,744.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APT/USDT:USDT | below_1h_threshold | +1.20% | +1.92% |
| CATE/USDT:USDT | below_1h_threshold | +0.96% | +1.68% |
| S/USDT:USDT | below_1h_threshold | +0.95% | +1.67% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +1.60% |
| ZEN/USDT:USDT | below_1h_threshold | +0.85% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
