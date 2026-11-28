# Decision Report

- generated_at: 2026-11-28T22:36:22.677697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19861**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=19861, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/15 | 26.7% | +2.63% | **+0.70%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.36% | **+0.34%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.22% | **+0.17%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.05% | **+0.73%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$122.25** / 初期 $100.00 (+22.25%)
- 確定トレード: 294件 (TP 108 / SL 176 / EXP 10)
- 最新: AKE/USDT:USDT TP_HIT PnL +8.00% 残高後 $122.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,015.21** / 初期 $100.00 (+1915.21%)
- 確定: 7687件 (Win 2216 / Loss 2477 / Flat 2994) / skip 8735件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $2,015.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5298件 (Win 1410 / Loss 1141 / Flat 2747) / skip 7974件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0468 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 8020件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000257 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-28T22:36:08.081145+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=59394.0
- Funnel: target 1101 → liquid 104 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +25.00% | $53,972,634.49 |
| IDOL/USDT:USDT | +7.34% | $1,889,249.11 |
| VELVET/USDT:USDT | +5.87% | $3,390,550.85 |
| LISTA/USDT:USDT | +4.10% | $3,458,960.32 |
| AKE/USDT:USDT | +3.93% | $5,108,243.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +2.58% | +2.37% |
| AKE/USDT:USDT | below_1h_threshold | +2.07% | +1.86% |
| PONS/USDT:USDT | below_1h_threshold | +1.46% | +1.26% |
| VELVET/USDT:USDT | below_1h_threshold | +1.43% | +1.22% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.33% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
