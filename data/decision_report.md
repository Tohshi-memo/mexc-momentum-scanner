# Decision Report

- generated_at: 2026-09-05T22:01:16.435978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13778**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=13778, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.39% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.09% | **+0.06%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.74** / 初期 $100.00 (+755.74%)
- 確定: 5084件 (Win 1524 / Loss 1658 / Flat 1902) / skip 5255件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $855.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.47** / 初期 $100.00 (+87.47%)
- 確定: 2523件 (Win 702 / Loss 597 / Flat 1224) / skip 4666件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0327 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $187.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.52** / 初期 $100.00 (+19.52%)
- 確定: 2395件 (Win 710 / Loss 909 / Flat 776) / pending 6件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000180 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.52

## 6. Latest Market Context

- 更新: 2026-09-05T22:01:06.546472+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=79872.9
- Funnel: target 1050 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +29.47% | $53,191,173.39 |
| UAI/USDT:USDT | +25.44% | $5,320,111.67 |
| 4/USDT:USDT | +23.04% | $23,445,133.75 |
| SUSHI/USDT:USDT | +22.61% | $3,416,610.28 |
| MAGMA/USDT:USDT | +12.34% | $2,461,517.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTUSTOCK/USDT:USDT | below_1h_threshold | +2.31% | +2.31% |
| 4/USDT:USDT | below_1h_threshold | +0.81% | +0.81% |
| LIT/USDT:USDT | below_1h_threshold | +0.47% | +0.47% |
| BULLA/USDT:USDT | below_1h_threshold | +0.28% | +0.27% |
| OP/USDT:USDT | below_1h_threshold | +0.18% | +0.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
