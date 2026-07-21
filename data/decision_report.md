# Decision Report

- generated_at: 2026-07-21T02:21:27.204374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9141**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=9141, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.74% | **+1.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.18% | **+1.04%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.14% | **+0.14%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.66% | **+0.13%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.26% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$404.37** / 初期 $100.00 (+304.37%)
- 確定: 3203件 (Win 1002 / Loss 1020 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $404.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.70** / 初期 $100.00 (+27.70%)
- 確定: 1102件 (Win 288 / Loss 228 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0981 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $127.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.10** / 初期 $100.00 (+1.10%)
- 確定: 336件 (Win 118 / Loss 149 / Flat 69) / pending 5件 / skip 273件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.10

## 6. Latest Market Context

- 更新: 2026-07-21T02:21:16.762951+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=65153.4
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +52.37% | $1,368,620.90 |
| JIMOTHY/USDT:USDT | +30.16% | $2,793,739.55 |
| BLESS/USDT:USDT | +15.78% | $1,735,668.27 |
| HEMI/USDT:USDT | +10.59% | $3,172,682.43 |
| AKE/USDT:USDT | +8.74% | $19,699,109.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.16% | +4.24% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.49% |
| BULLA/USDT:USDT | below_1h_threshold | +1.32% | +1.40% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.07% | +1.15% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.01% | +1.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
