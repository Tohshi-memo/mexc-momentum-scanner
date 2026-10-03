# Decision Report

- generated_at: 2026-10-03T00:06:08.755804+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16023**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16023, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.81% | **+0.56%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.16% | **+0.13%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.17% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.10% | **+1.16%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.98% | **+0.84%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +1.18% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,335.42** / 初期 $100.00 (+1235.42%)
- 確定: 6128件 (Win 1807 / Loss 1963 / Flat 2358) / skip 6456件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,335.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5829件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0370 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4182件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T00:06:00.969982+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=84432.8
- Funnel: target 1099 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +40.96% | $6,065,611.68 |
| SAND/USDT:USDT | +9.02% | $75,814,947.67 |
| LONGXIA/USDT:USDT | +6.02% | $16,689,884.52 |
| NIGHT/USDT:USDT | +4.64% | $8,282,901.25 |
| SUPER/USDT:USDT | +3.63% | $1,210,725.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXS/USDT:USDT | below_1h_threshold | +1.37% | +1.43% |
| GRASS/USDT:USDT | below_1h_threshold | +1.00% | +1.06% |
| VELVET/USDT:USDT | below_1h_threshold | +0.90% | +0.96% |
| ICP/USDT:USDT | below_1h_threshold | +0.70% | +0.76% |
| RENDER/USDT:USDT | below_1h_threshold | +0.61% | +0.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
