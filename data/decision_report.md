# Decision Report

- generated_at: 2026-09-13T00:51:27.468382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14334**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=14334, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.80% | **+1.68%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.78% | **+0.98%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.20% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.66% | **+1.32%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.56% | **+1.17%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.81%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.05% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5465件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$215.98** / 初期 $100.00 (+115.98%)
- 確定: 2852件 (Win 788 / Loss 662 / Flat 1402) / skip 4893件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1405 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $215.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.12** / 初期 $100.00 (+25.12%)
- 確定: 2785件 (Win 826 / Loss 1070 / Flat 889) / pending 4件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000447 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $125.12

## 6. Latest Market Context

- 更新: 2026-09-13T00:51:13.386895+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77219.3
- Funnel: target 1068 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +46.44% | $58,188,982.68 |
| ZCAT/USDT:USDT | +26.98% | $1,045,732.37 |
| STORJ/USDT:USDT | +20.62% | $20,557,470.50 |
| REZ/USDT:USDT | +16.54% | $2,395,495.44 |
| ALCH/USDT:USDT | +14.39% | $2,473,580.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| REZ/USDT:USDT | below_1h_threshold | +1.95% | +1.98% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.39% | +1.42% |
| UAI/USDT:USDT | below_1h_threshold | +1.38% | +1.41% |
| INJ/USDT:USDT | below_1h_threshold | +1.17% | +1.20% |
| CHZ/USDT:USDT | below_1h_threshold | +1.12% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
