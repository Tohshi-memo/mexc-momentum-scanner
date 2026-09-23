# Decision Report

- generated_at: 2026-09-23T23:36:16.388703+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15447**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=15447, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.63% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_5PCT | 5/20 | 25.0% | +5.18% | **+1.30%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.60% | **+1.28%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.47% | **+1.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.89% | **+1.13%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.39% | **+0.23%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.04% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5897件 (Win 1739 / Loss 1890 / Flat 2268) / skip 6111件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.74** / 初期 $100.00 (+152.74%)
- 確定: 3394件 (Win 935 / Loss 790 / Flat 1669) / skip 5464件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0654 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $252.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.18** / 初期 $100.00 (+21.18%)
- 確定: 3139件 (Win 924 / Loss 1236 / Flat 979) / pending 2件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000232 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $121.18

## 6. Latest Market Context

- 更新: 2026-09-23T23:36:07.899889+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=84458.8
- Funnel: target 1061 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +30.25% | $11,417,982.72 |
| LSK/USDT:USDT | +17.20% | $4,155,232.63 |
| BTW/USDT:USDT | +9.35% | $3,767,174.37 |
| MARSCOIN/USDT:USDT | +8.13% | $3,407,774.58 |
| UAI/USDT:USDT | +7.02% | $2,548,970.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +2.25% | +2.33% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.50% | +1.58% |
| CHR/USDT:USDT | below_1h_threshold | +1.46% | +1.54% |
| COTI/USDT:USDT | below_1h_threshold | +1.34% | +1.42% |
| UAI/USDT:USDT | below_1h_threshold | +0.84% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
