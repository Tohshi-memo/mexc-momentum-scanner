# Decision Report

- generated_at: 2026-09-22T01:06:14.232046+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15286**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.43% / filled 20/20。**
- 全期間 MARKET基準: n=15286, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.70% | **+1.62%** |
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_BB3S | 10/17 | 58.8% | +1.39% | **+0.82%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.47% | **+0.33%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.33% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.18% | **+0.08%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.01% | **-0.01%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.02% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,171.38** / 初期 $100.00 (+1071.38%)
- 確定: 5777件 (Win 1718 / Loss 1858 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PTB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,171.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.91** / 初期 $100.00 (+147.91%)
- 確定: 3325件 (Win 918 / Loss 769 / Flat 1638) / skip 5372件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0303 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $247.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.56** / 初期 $100.00 (+22.56%)
- 確定: 3058件 (Win 899 / Loss 1196 / Flat 963) / pending 2件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.56

## 6. Latest Market Context

- 更新: 2026-09-22T01:06:04.911982+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=85712.0
- Funnel: target 1055 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +24.69% | $8,833,741.28 |
| ALCH/USDT:USDT | +24.19% | $2,265,195.35 |
| EVAA/USDT:USDT | +13.42% | $2,274,572.79 |
| GRASS/USDT:USDT | +11.70% | $2,221,538.24 |
| PTB/USDT:USDT | +9.88% | $1,206,106.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +2.78% | +2.95% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.65% | +1.82% |
| SNXX/USDT:USDT | below_1h_threshold | +1.30% | +1.47% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.47% |
| SOXL/USDT:USDT | below_1h_threshold | +1.25% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
