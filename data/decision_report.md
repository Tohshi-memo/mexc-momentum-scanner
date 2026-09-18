# Decision Report

- generated_at: 2026-09-18T03:11:25.927251+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14858**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=14858, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_BB3S | 8/17 | 47.1% | +1.32% | **+0.62%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.31% | **+1.38%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.20% | **+0.66%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.22% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5604件 (Win 1679 / Loss 1814 / Flat 2111) / skip 5815件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.85** / 初期 $100.00 (+143.85%)
- 確定: 3147件 (Win 876 / Loss 751 / Flat 1520) / skip 5122件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1241 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $243.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.32** / 初期 $100.00 (+23.32%)
- 確定: 2960件 (Win 878 / Loss 1166 / Flat 916) / pending 0件 / skip 3367件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000352 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.32

## 6. Latest Market Context

- 更新: 2026-09-18T03:11:14.959399+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=77046.7
- Funnel: target 1052 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +34.17% | $3,394,341.60 |
| ARB/USDT:USDT | +26.48% | $79,096,348.83 |
| COTI/USDT:USDT | +20.44% | $6,823,573.37 |
| NEAR/USDT:USDT | +19.62% | $122,989,410.76 |
| APT/USDT:USDT | +15.04% | $6,058,906.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OP/USDT:USDT | below_1h_threshold | +2.89% | +2.76% |
| NEAR/USDT:USDT | below_1h_threshold | +2.23% | +2.10% |
| COTI/USDT:USDT | below_1h_threshold | +1.86% | +1.73% |
| UNI/USDT:USDT | below_1h_threshold | +1.72% | +1.59% |
| RAY/USDT:USDT | below_1h_threshold | +1.56% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
