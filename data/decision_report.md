# Decision Report

- generated_at: 2026-09-22T03:51:33.897462+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15293**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.27% / filled 20/20。**
- 全期間 MARKET基準: n=15293, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.90% | **+1.71%** |
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_BB3S | 7/18 | 38.9% | +2.35% | **+0.91%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.65% | **+0.45%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.51% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.73% | **+0.33%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.33% | **+0.30%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.55% | **+0.25%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.22% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,183.34** / 初期 $100.00 (+1083.34%)
- 確定: 5784件 (Win 1721 / Loss 1861 / Flat 2202) / skip 6070件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,183.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.59** / 初期 $100.00 (+149.59%)
- 確定: 3332件 (Win 921 / Loss 772 / Flat 1639) / skip 5372件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $249.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.98** / 初期 $100.00 (+22.98%)
- 確定: 3065件 (Win 902 / Loss 1199 / Flat 964) / pending 3件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000238 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.98

## 6. Latest Market Context

- 更新: 2026-09-22T03:51:18.763426+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=85489.5
- Funnel: target 1055 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +34.02% | $2,739,158.30 |
| ALCH/USDT:USDT | +18.78% | $2,434,083.36 |
| GRASS/USDT:USDT | +13.51% | $2,507,708.35 |
| FORM/USDT:USDT | +12.74% | $9,479,926.51 |
| TAO/USDT:USDT | +8.97% | $144,247,355.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.84% | +5.07% |
| SYN/USDT:USDT | below_1h_threshold | +4.00% | +4.22% |
| PEPE/USDT:USDT | below_1h_threshold | +2.77% | +3.00% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.72% | +2.95% |
| PHA/USDT:USDT | below_1h_threshold | +2.71% | +2.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
