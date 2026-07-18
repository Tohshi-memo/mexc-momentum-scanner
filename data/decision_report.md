# Decision Report

- generated_at: 2026-07-18T01:21:11.894063+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8906**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=8906, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.73% | **+0.55%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +4.73% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.78% | **+1.25%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.58% | **+0.40%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.47% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$367.56** / 初期 $100.00 (+267.56%)
- 確定: 3021件 (Win 939 / Loss 959 / Flat 1123) / skip 2446件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $367.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$112.45** / 初期 $100.00 (+12.45%)
- 確定: 868件 (Win 205 / Loss 175 / Flat 488) / skip 1449件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.014% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $112.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.65** / 初期 $100.00 (-0.35%)
- 確定: 164件 (Win 52 / Loss 86 / Flat 26) / pending 4件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $99.65

## 6. Latest Market Context

- 更新: 2026-07-18T01:21:05.495899+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63902.1
- Funnel: target 885 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +59.53% | $10,906,415.48 |
| CASHCAT/USDT:USDT | +15.18% | $1,177,306.14 |
| AKE/USDT:USDT | +14.41% | $47,589,932.10 |
| CRO/USDT:USDT | +10.76% | $2,143,295.88 |
| BANK/USDT:USDT | +9.05% | $21,783,303.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.07% | +3.04% |
| SYN/USDT:USDT | below_1h_threshold | +3.06% | +3.02% |
| BILL/USDT:USDT | below_1h_threshold | +2.05% | +2.02% |
| CRO/USDT:USDT | below_1h_threshold | +1.61% | +1.58% |
| UB/USDT:USDT | below_1h_threshold | +1.51% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
