# Decision Report

- generated_at: 2026-08-07T23:56:15.366465+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10775**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10775, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +2.61% | **+1.44%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.96% | **+1.19%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.93% | **+0.77%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.15% | **+0.69%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.79% | **+0.43%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.51% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3800件 (Win 1203 / Loss 1250 / Flat 1347) / skip 3536件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.83** / 初期 $100.00 (+44.83%)
- 確定: 1492件 (Win 421 / Loss 351 / Flat 720) / skip 2694件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0827 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $144.83

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.23** / 初期 $100.00 (+18.23%)
- 確定: 1181件 (Win 381 / Loss 467 / Flat 333) / pending 1件 / skip 1064件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MMT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.23

## 6. Latest Market Context

- 更新: 2026-08-07T23:56:07.469321+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64882.7
- Funnel: target 961 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +95.64% | $3,500,846.09 |
| BLESS/USDT:USDT | +30.35% | $76,740,242.47 |
| GWEI/USDT:USDT | +21.35% | $1,802,695.52 |
| EPIC/USDT:USDT | +19.37% | $2,269,380.12 |
| SLX/USDT:USDT | +13.79% | $1,456,834.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.60% | +3.56% |
| BLESS/USDT:USDT | below_1h_threshold | +3.36% | +3.32% |
| HEI/USDT:USDT | below_1h_threshold | +2.80% | +2.76% |
| RE/USDT:USDT | below_1h_threshold | +1.85% | +1.81% |
| FET/USDT:USDT | below_1h_threshold | +1.25% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
