# Decision Report

- generated_at: 2026-09-24T11:36:20.825955+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15474**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=15474, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.23% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +3.87% | **+2.58%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.57%** |
| MARKET_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.89% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5898件 (Win 1739 / Loss 1890 / Flat 2269) / skip 6137件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.81** / 初期 $100.00 (+153.81%)
- 確定: 3421件 (Win 946 / Loss 791 / Flat 1684) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0497 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $253.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.27** / 初期 $100.00 (+21.27%)
- 確定: 3159件 (Win 932 / Loss 1246 / Flat 981) / pending 0件 / skip 3784件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000186 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.27

## 6. Latest Market Context

- 更新: 2026-09-24T11:36:01.077284+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=83410.1
- Funnel: target 1070 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +42.95% | $4,874,090.11 |
| NIL/USDT:USDT | +33.07% | $22,405,212.67 |
| LSK/USDT:USDT | +27.18% | $12,493,895.31 |
| TUT/USDT:USDT | +20.69% | $2,247,604.13 |
| CYS/USDT:USDT | +15.79% | $1,062,766.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +2.23% | +2.30% |
| NEAR/USDT:USDT | below_1h_threshold | +1.72% | +1.79% |
| CYS/USDT:USDT | below_1h_threshold | +1.63% | +1.70% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.39% | +1.47% |
| VET/USDT:USDT | below_1h_threshold | +1.24% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
