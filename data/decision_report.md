# Decision Report

- generated_at: 2026-09-19T01:16:16.262192+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14969**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.52% / filled 20/20。**
- 全期間 MARKET基準: n=14969, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.84% | **+0.59%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.57% | **+0.29%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.40% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +3.11% | **+1.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.40% | **+0.70%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.79% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,189.35** / 初期 $100.00 (+1089.35%)
- 確定: 5624件 (Win 1687 / Loss 1823 / Flat 2114) / skip 5906件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,189.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.98** / 初期 $100.00 (+139.98%)
- 確定: 3175件 (Win 878 / Loss 759 / Flat 1538) / skip 5205件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1291 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 2962件 (Win 879 / Loss 1167 / Flat 916) / pending 0件 / skip 3482件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000390 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.52

## 6. Latest Market Context

- 更新: 2026-09-19T01:16:06.166760+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.47% price=81254.6
- Funnel: target 1050 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +78.69% | $35,787,431.05 |
| SYN/USDT:USDT | +24.33% | $6,841,503.84 |
| MAGMA/USDT:USDT | +23.99% | $1,228,452.62 |
| SAGA/USDT:USDT | +22.81% | $4,207,795.45 |
| USELESS/USDT:USDT | +20.04% | $7,701,255.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| S/USDT:USDT | below_1h_threshold | +1.78% | +2.25% |
| B/USDT:USDT | below_1h_threshold | +1.37% | +1.84% |
| CATE/USDT:USDT | below_1h_threshold | +1.16% | +1.63% |
| APT/USDT:USDT | below_1h_threshold | +1.15% | +1.62% |
| NEAR/USDT:USDT | below_1h_threshold | +1.02% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
