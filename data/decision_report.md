# Decision Report

- generated_at: 2026-09-12T17:41:25.575759+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14317**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=14317, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.47% | **+1.39%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.97% | **+0.77%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.17% | **+0.70%** |
| LIMIT_BB3S | 3/19 | 15.8% | +3.98% | **+0.63%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.74% | **+1.48%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.01% | **+0.96%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.28% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5449件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2835件 (Win 780 / Loss 656 / Flat 1399) / skip 4893件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0967 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.33** / 初期 $100.00 (+23.33%)
- 確定: 2768件 (Win 818 / Loss 1064 / Flat 886) / pending 5件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000342 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $123.33

## 6. Latest Market Context

- 更新: 2026-09-12T17:41:13.421028+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=77192.7
- Funnel: target 1068 → liquid 127 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +15.32% | $28,507,656.27 |
| REZ/USDT:USDT | +12.33% | $1,032,778.18 |
| RIVER/USDT:USDT | +10.63% | $9,863,819.47 |
| PUMPFUN/USDT:USDT | +6.14% | $13,283,874.08 |
| LONGXIA/USDT:USDT | +5.90% | $8,312,608.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +4.21% | +4.38% |
| CYS/USDT:USDT | below_1h_threshold | +2.63% | +2.80% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.86% | +2.03% |
| ALCH/USDT:USDT | below_1h_threshold | +1.56% | +1.73% |
| INJ/USDT:USDT | below_1h_threshold | +1.28% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
