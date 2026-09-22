# Decision Report

- generated_at: 2026-09-22T01:16:16.231194+00:00
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
- 確定: 3058件 (Win 899 / Loss 1196 / Flat 963) / pending 3件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.56

## 6. Latest Market Context

- 更新: 2026-09-22T01:16:07.369558+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=85819.1
- Funnel: target 1055 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +27.47% | $8,862,520.59 |
| ALCH/USDT:USDT | +25.24% | $2,271,035.23 |
| EVAA/USDT:USDT | +12.42% | $2,310,218.92 |
| GRASS/USDT:USDT | +12.29% | $2,244,973.63 |
| 4STOCK/USDT:USDT | +9.22% | $1,093,725.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +4.92% | +4.97% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.65% | +1.70% |
| NIL/USDT:USDT | below_1h_threshold | +1.55% | +1.60% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.53% | +1.58% |
| S/USDT:USDT | below_1h_threshold | +1.38% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
