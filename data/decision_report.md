# Decision Report

- generated_at: 2026-09-26T21:06:26.036524+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15616**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=15616, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.03% | **+0.81%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.53% | **+0.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.16% | **+0.32%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.40% | **+0.30%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.40% | **+0.16%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.21% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,245.84** / 初期 $100.00 (+1145.84%)
- 確定: 5977件 (Win 1766 / Loss 1922 / Flat 2289) / skip 6200件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PAID/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,245.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5494件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0229 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.73** / 初期 $100.00 (+19.73%)
- 確定: 3199件 (Win 942 / Loss 1268 / Flat 989) / pending 6件 / skip 3884件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PAID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.73

## 6. Latest Market Context

- 更新: 2026-09-26T21:06:13.024799+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=84066.8
- Funnel: target 1070 → liquid 144 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +9.93% | $1,729,979.60 |
| GRASS/USDT:USDT | +9.69% | $4,206,705.75 |
| TRIA/USDT:USDT | +7.43% | $6,511,997.69 |
| GRAM/USDT:USDT | +6.86% | $4,271,096.45 |
| LSK/USDT:USDT | +5.20% | $3,129,689.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PAID/USDT:USDT | below_1h_threshold | +1.78% | +1.69% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.69% | +1.60% |
| GRAM/USDT:USDT | below_1h_threshold | +1.60% | +1.51% |
| PYTH/USDT:USDT | below_1h_threshold | +0.96% | +0.87% |
| LSK/USDT:USDT | below_1h_threshold | +0.87% | +0.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
