# Decision Report

- generated_at: 2026-10-16T04:56:25.507792+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16783**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16783, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.57% | **+1.49%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_BB3S | 4/12 | 33.3% | +1.89% | **+0.63%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.08% | **+1.70%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.06% | **+0.72%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.30% | **+0.45%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.54% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 241件 (TP 89 / SL 145 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,260.96** / 初期 $100.00 (+1160.96%)
- 確定: 6314件 (Win 1849 / Loss 2026 / Flat 2439) / skip 7030件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STBL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,260.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.98** / 初期 $100.00 (+175.98%)
- 確定: 3675件 (Win 1024 / Loss 871 / Flat 1780) / skip 6519件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0385 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STBL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $275.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4943件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000239 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-16T04:56:13.706438+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=82081.1
- Funnel: target 1090 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +63.55% | $7,187,073.11 |
| STBL/USDT:USDT | +18.89% | $1,412,175.38 |
| SIREN/USDT:USDT | +16.91% | $1,249,266.76 |
| INJ/USDT:USDT | +15.18% | $64,136,218.56 |
| SI/USDT:USDT | +11.92% | $2,162,329.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.74% | +3.76% |
| SOXL/USDT:USDT | below_1h_threshold | +2.75% | +2.76% |
| KORU/USDT:USDT | below_1h_threshold | +2.53% | +2.55% |
| MVLL/USDT:USDT | below_1h_threshold | +2.33% | +2.34% |
| INTW/USDT:USDT | below_1h_threshold | +2.23% | +2.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
