# Decision Report

- generated_at: 2026-09-24T12:06:49.842056+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15476**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=15476, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.46% | **+0.37%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.27% | **+0.09%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.25% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.19% | **+0.15%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.10% | **+0.08%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.22% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5899件 (Win 1739 / Loss 1890 / Flat 2270) / skip 6138件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.81** / 初期 $100.00 (+153.81%)
- 確定: 3423件 (Win 946 / Loss 791 / Flat 1686) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0495 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $253.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.27** / 初期 $100.00 (+21.27%)
- 確定: 3159件 (Win 932 / Loss 1246 / Flat 981) / pending 0件 / skip 3787件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000278 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.27

## 6. Latest Market Context

- 更新: 2026-09-24T12:06:34.080450+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=83407.7
- Funnel: target 1070 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +45.92% | $4,994,438.93 |
| NIL/USDT:USDT | +33.59% | $22,743,321.95 |
| LSK/USDT:USDT | +31.77% | $12,618,717.77 |
| TUT/USDT:USDT | +13.38% | $2,649,314.66 |
| CYS/USDT:USDT | +13.14% | $1,079,924.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +1.59% | +1.64% |
| BTW/USDT:USDT | below_1h_threshold | +0.77% | +0.82% |
| SOXS/USDT:USDT | below_1h_threshold | +0.45% | +0.50% |
| USOIL/USDT:USDT | below_1h_threshold | +0.39% | +0.44% |
| NEO/USDT:USDT | below_1h_threshold | +0.24% | +0.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
