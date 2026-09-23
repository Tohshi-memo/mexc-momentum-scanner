# Decision Report

- generated_at: 2026-09-23T10:56:29.545214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15428**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=15428, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +2.60% | **+1.95%** |
| LIMIT_5PCT | 7/20 | 35.0% | +5.28% | **+1.85%** |
| LIMIT_ATR | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_BB3S | 5/12 | 41.7% | +3.66% | **+1.52%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.88% | **+1.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.71% | **+1.54%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.58% | **+1.42%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.18% | **+0.77%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.72% | **+0.47%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.75% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5895件 (Win 1739 / Loss 1890 / Flat 2266) / skip 6094件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.06** / 初期 $100.00 (+149.06%)
- 確定: 3376件 (Win 931 / Loss 789 / Flat 1656) / skip 5463件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $249.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3765件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T10:56:17.625837+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=85798.7
- Funnel: target 1061 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMISTOCK/USDT:USDT | +777.95% | $1,259,478.08 |
| TAKE/USDT:USDT | +222.42% | $5,610,348.94 |
| SHROOM/USDT:USDT | +68.17% | $1,380,002.50 |
| MET/USDT:USDT | +34.63% | $1,416,119.01 |
| ALLO/USDT:USDT | +22.20% | $4,211,599.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.86% | +3.88% |
| MYX/USDT:USDT | below_1h_threshold | +2.71% | +2.74% |
| CHR/USDT:USDT | below_1h_threshold | +2.69% | +2.72% |
| MET/USDT:USDT | below_1h_threshold | +2.67% | +2.70% |
| RAY/USDT:USDT | below_1h_threshold | +2.23% | +2.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
