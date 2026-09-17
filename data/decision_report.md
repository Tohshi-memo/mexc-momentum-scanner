# Decision Report

- generated_at: 2026-09-17T20:11:17.152959+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14834**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=14834, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +2.98% | **+1.34%** |
| LIMIT_6PCT | 7/20 | 35.0% | +3.67% | **+1.28%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.56% | **+0.86%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +2.26% | **+1.92%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.61% | **+1.37%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.50% | **+1.20%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.90% | **+0.86%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.81% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5603件 (Win 1679 / Loss 1814 / Flat 2110) / skip 5792件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.90** / 初期 $100.00 (+141.90%)
- 確定: 3132件 (Win 872 / Loss 747 / Flat 1513) / skip 5113件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0882 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $241.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2958件 (Win 878 / Loss 1165 / Flat 915) / pending 0件 / skip 3353件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T20:11:06.830261+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=76591.3
- Funnel: target 1052 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +51.85% | $1,842,848.66 |
| ONE/USDT:USDT | +18.67% | $32,529,445.73 |
| COTI/USDT:USDT | +13.99% | $2,870,692.69 |
| PIEVERSE/USDT:USDT | +10.87% | $1,337,866.71 |
| UNI/USDT:USDT | +7.02% | $47,842,542.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.84% | +3.80% |
| ONE/USDT:USDT | below_1h_threshold | +2.38% | +2.35% |
| AKE/USDT:USDT | below_1h_threshold | +2.24% | +2.20% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.84% | +1.80% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.20% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
