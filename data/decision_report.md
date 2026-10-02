# Decision Report

- generated_at: 2026-10-02T15:26:30.087681+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16009**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=16009, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.26% | **+0.85%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.93% | **+0.77%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.79% | **+0.47%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.50% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.65% | **+0.59%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.41% | **+0.29%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.33% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.32** / 初期 $100.00 (+1242.32%)
- 確定: 6114件 (Win 1807 / Loss 1960 / Flat 2347) / skip 6456件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,342.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5815件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0172 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4171件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T15:26:18.538489+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=85319.1
- Funnel: target 1099 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +72.86% | $4,266,295.97 |
| MAGMA/USDT:USDT | +62.22% | $3,254,393.78 |
| SAND/USDT:USDT | +42.10% | $55,347,408.78 |
| SI/USDT:USDT | +39.45% | $3,864,150.65 |
| NIGHT/USDT:USDT | +19.62% | $7,339,686.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CT/USDT:USDT | below_1h_threshold | +3.60% | +3.97% |
| SI/USDT:USDT | below_1h_threshold | +2.66% | +3.04% |
| MONAD/USDT:USDT | below_1h_threshold | +1.80% | +2.18% |
| LTC/USDT:USDT | below_1h_threshold | +1.45% | +1.83% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.34% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
