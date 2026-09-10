# Decision Report

- generated_at: 2026-09-10T13:36:23.203292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14166**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14166, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +2.59% | **+1.29%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,051.11** / 初期 $100.00 (+951.11%)
- 確定: 5346件 (Win 1607 / Loss 1726 / Flat 2013) / skip 5381件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,051.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.42** / 初期 $100.00 (+107.42%)
- 確定: 2760件 (Win 762 / Loss 647 / Flat 1351) / skip 4817件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0985 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $207.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.81** / 初期 $100.00 (+21.81%)
- 確定: 2671件 (Win 787 / Loss 1020 / Flat 864) / pending 3件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000308 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $121.81

## 6. Latest Market Context

- 更新: 2026-09-10T13:36:12.300246+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=76883.7
- Funnel: target 1065 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +44.31% | $8,494,959.22 |
| CATE/USDT:USDT | +26.04% | $2,793,489.17 |
| NES/USDT:USDT | +18.69% | $1,517,878.28 |
| SOXS/USDT:USDT | +7.93% | $15,532,724.12 |
| KAS/USDT:USDT | +6.81% | $9,300,243.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.70% | +3.67% |
| MINA/USDT:USDT | below_1h_threshold | +2.58% | +2.55% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.44% | +2.41% |
| ARX/USDT:USDT | below_1h_threshold | +1.43% | +1.40% |
| USOIL/USDT:USDT | below_1h_threshold | +1.39% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
