# Decision Report

- generated_at: 2026-08-01T16:26:18.745721+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10101**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=10101, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.15% | **+1.03%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.33% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.58% | **+1.93%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.86% | **+0.73%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.21% | **+0.72%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.74% | **+0.35%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$570.82** / 初期 $100.00 (+470.82%)
- 確定: 3638件 (Win 1158 / Loss 1191 / Flat 1289) / skip 3024件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $570.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2233件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.96** / 初期 $100.00 (+10.96%)
- 確定: 912件 (Win 288 / Loss 357 / Flat 267) / pending 2件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.96

## 6. Latest Market Context

- 更新: 2026-08-01T16:26:11.399666+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=62926.6
- Funnel: target 922 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIGHT/USDT:USDT | +4.08% | $2,245,345.71 |
| IDOL/USDT:USDT | +3.83% | $1,492,438.87 |
| 1000RATS/USDT:USDT | +3.20% | $22,648,825.34 |
| ESPORTS/USDT:USDT | +3.15% | $1,550,798.57 |
| UAI/USDT:USDT | +3.01% | $6,486,064.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +4.13% | +4.21% |
| FIGHT/USDT:USDT | below_1h_threshold | +4.09% | +4.17% |
| 1000RATS/USDT:USDT | below_1h_threshold | +3.20% | +3.28% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.16% | +3.24% |
| UAI/USDT:USDT | below_1h_threshold | +3.02% | +3.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
