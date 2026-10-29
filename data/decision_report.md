# Decision Report

- generated_at: 2026-10-29T17:46:49.373708+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17795**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=17795, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.25% | **+0.68%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.92% | **+0.46%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.64% | **+0.32%** |
| LIMIT_BB3S | 5/11 | 45.5% | +0.31% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +1.96% | **+1.37%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6804件 (Win 1975 / Loss 2180 / Flat 2649) / skip 7552件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.70** / 初期 $100.00 (+264.70%)
- 確定: 4316件 (Win 1165 / Loss 978 / Flat 2173) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0067 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PARTI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $364.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5958件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000378 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T17:46:35.461076+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=80890.3
- Funnel: target 1086 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1, 4h RSI 78.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +50.08% | $1,276,691.95 |
| BLESS/USDT:USDT | +11.31% | $10,400,293.72 |
| BULLA/USDT:USDT | +7.20% | $1,565,011.82 |
| UAI/USDT:USDT | +4.46% | $2,755,741.56 |
| SOXS/USDT:USDT | +2.97% | $77,947,295.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +2.74% | +3.16% |
| INIT/USDT:USDT | below_1h_threshold | +1.98% | +2.40% |
| SOXS/USDT:USDT | below_1h_threshold | +1.82% | +2.24% |
| BULLA/USDT:USDT | below_1h_threshold | +1.13% | +1.55% |
| XPIN/USDT:USDT | below_1h_threshold | +0.82% | +1.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
