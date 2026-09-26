# Decision Report

- generated_at: 2026-09-26T22:41:25.816989+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15623**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=15623, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.71% | **+0.61%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.62% | **+0.59%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.43% | **+0.57%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.88% | **+0.53%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.79% | **+0.48%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.25% | **+0.37%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.16% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5978件 (Win 1766 / Loss 1923 / Flat 2289) / skip 6206件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5501件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0294 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.36** / 初期 $100.00 (+19.36%)
- 確定: 3206件 (Win 944 / Loss 1272 / Flat 990) / pending 5件 / skip 3885件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $119.36

## 6. Latest Market Context

- 更新: 2026-09-26T22:41:12.464182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=84236.3
- Funnel: target 1070 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +17.95% | $23,474,016.56 |
| GRASS/USDT:USDT | +11.56% | $4,713,895.37 |
| MARSCOIN/USDT:USDT | +9.71% | $1,907,022.40 |
| ZEC/USDT:USDT | +7.28% | $789,554,017.64 |
| GRAM/USDT:USDT | +6.19% | $5,085,240.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAKE/USDT:USDT | below_1h_threshold | +2.02% | +1.88% |
| PHA/USDT:USDT | below_1h_threshold | +1.69% | +1.55% |
| LSK/USDT:USDT | below_1h_threshold | +1.03% | +0.89% |
| 2Z/USDT:USDT | below_1h_threshold | +0.97% | +0.84% |
| SOXL/USDT:USDT | below_1h_threshold | +0.60% | +0.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
