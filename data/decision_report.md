# Decision Report

- generated_at: 2026-09-24T10:51:26.339380+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15473**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.85% / filled 20/20。**
- 全期間 MARKET基準: n=15473, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.84% | **+0.75%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.79% | **+0.67%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +5.24% | **+5.24%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.17% | **+0.97%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.89% | **+0.31%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5898件 (Win 1739 / Loss 1890 / Flat 2269) / skip 6136件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.81** / 初期 $100.00 (+153.81%)
- 確定: 3420件 (Win 946 / Loss 791 / Flat 1683) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0644 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $253.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.27** / 初期 $100.00 (+21.27%)
- 確定: 3159件 (Win 932 / Loss 1246 / Flat 981) / pending 0件 / skip 3783件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.27

## 6. Latest Market Context

- 更新: 2026-09-24T10:51:12.742060+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=83490.2
- Funnel: target 1070 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +44.02% | $4,689,985.04 |
| NIL/USDT:USDT | +36.42% | $21,885,660.97 |
| LSK/USDT:USDT | +27.78% | $12,245,279.34 |
| TUT/USDT:USDT | +20.12% | $1,853,908.96 |
| CYS/USDT:USDT | +14.18% | $1,061,541.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +3.26% | +2.95% |
| AERO/USDT:USDT | below_1h_threshold | +2.51% | +2.20% |
| JASMY/USDT:USDT | below_1h_threshold | +2.09% | +1.78% |
| ICP/USDT:USDT | below_1h_threshold | +1.96% | +1.65% |
| TRB/USDT:USDT | below_1h_threshold | +1.58% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
