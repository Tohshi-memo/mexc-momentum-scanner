# Decision Report

- generated_at: 2026-09-15T01:11:21.223707+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14543**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=14543, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.64% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.33% | **+1.75%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,052.44** / 初期 $100.00 (+952.44%)
- 確定: 5446件 (Win 1637 / Loss 1770 / Flat 2039) / skip 5658件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,052.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2992件 (Win 830 / Loss 716 / Flat 1446) / skip 4962件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0011 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.54** / 初期 $100.00 (+25.54%)
- 確定: 2890件 (Win 859 / Loss 1120 / Flat 911) / pending 4件 / skip 3121件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000482 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $125.54

## 6. Latest Market Context

- 更新: 2026-09-15T01:11:08.200152+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=77756.9
- Funnel: target 1073 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +42.80% | $1,228,688.67 |
| CNPY/USDT:USDT | +18.38% | $1,696,791.74 |
| AIN/USDT:USDT | +17.99% | $6,481,819.97 |
| CYS/USDT:USDT | +14.13% | $1,493,675.01 |
| POWER/USDT:USDT | +10.52% | $6,393,877.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +2.70% | +2.92% |
| CYS/USDT:USDT | below_1h_threshold | +2.01% | +2.23% |
| USELESS/USDT:USDT | below_1h_threshold | +1.98% | +2.21% |
| KORU/USDT:USDT | below_1h_threshold | +1.65% | +1.87% |
| CATE/USDT:USDT | below_1h_threshold | +1.56% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
