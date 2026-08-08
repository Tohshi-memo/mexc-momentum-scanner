# Decision Report

- generated_at: 2026-08-08T05:21:16.795959+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10811**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10811, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_8PCT | 10/20 | 50.0% | +0.37% | **+0.19%** |
| LIMIT_9PCT | 8/20 | 40.0% | +0.07% | **+0.03%** |
| LIMIT_BB3S | 5/13 | 38.5% | -0.65% | **-0.25%** |
| LIMIT_6PCT | 11/20 | 55.0% | -0.73% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 10/20 | 50.0% | +4.73% | **+2.36%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +6.35% | **+2.22%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +3.60% | **+1.80%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +2.97% | **+1.78%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$615.31** / 初期 $100.00 (+515.31%)
- 確定: 3812件 (Win 1208 / Loss 1252 / Flat 1352) / skip 3560件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $615.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2712件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0974 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1097件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000273 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T05:21:08.893906+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64978.4
- Funnel: target 961 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +256.66% | $6,562,913.16 |
| BLESS/USDT:USDT | +20.61% | $93,000,285.34 |
| MMT/USDT:USDT | +18.33% | $1,624,797.21 |
| TUT/USDT:USDT | +17.73% | $2,506,759.77 |
| SLX/USDT:USDT | +16.47% | $2,757,764.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +2.57% | +2.57% |
| GWEI/USDT:USDT | below_1h_threshold | +1.83% | +1.83% |
| UAI/USDT:USDT | below_1h_threshold | +1.38% | +1.37% |
| CYS/USDT:USDT | below_1h_threshold | +0.56% | +0.56% |
| WIF/USDT:USDT | below_1h_threshold | +0.43% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
