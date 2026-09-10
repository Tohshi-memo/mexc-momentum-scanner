# Decision Report

- generated_at: 2026-09-10T11:06:19.817560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14159**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14159, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +2.14% | **+1.39%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.97% | **+0.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +8.00% | **+5.33%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.45% | **+1.84%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.02% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.98% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,067.04** / 初期 $100.00 (+967.04%)
- 確定: 5339件 (Win 1607 / Loss 1723 / Flat 2009) / skip 5381件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NES/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,067.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.15** / 初期 $100.00 (+108.15%)
- 確定: 2753件 (Win 762 / Loss 646 / Flat 1345) / skip 4817件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1093 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NES/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.45** / 初期 $100.00 (+22.45%)
- 確定: 2664件 (Win 787 / Loss 1017 / Flat 860) / pending 2件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NES/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.45

## 6. Latest Market Context

- 更新: 2026-09-10T11:06:09.865742+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=77714.9
- Funnel: target 1064 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +42.03% | $2,693,082.10 |
| VTHO/USDT:USDT | +40.30% | $5,982,728.77 |
| NES/USDT:USDT | +16.26% | $1,328,950.29 |
| REZ/USDT:USDT | +13.86% | $1,654,223.11 |
| KAS/USDT:USDT | +8.85% | $7,546,434.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VTHO/USDT:USDT | below_1h_threshold | +2.43% | +2.58% |
| HEMI/USDT:USDT | below_1h_threshold | +1.66% | +1.81% |
| METASTOCK/USDT:USDT | below_1h_threshold | +0.45% | +0.61% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +0.45% | +0.60% |
| SOXS/USDT:USDT | below_1h_threshold | +0.32% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
