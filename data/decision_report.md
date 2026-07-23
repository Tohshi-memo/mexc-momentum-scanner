# Decision Report

- generated_at: 2026-07-23T08:16:09.785536+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9363**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=9363, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.82% | **+1.36%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.06% | **+0.90%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.33% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.03% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.42% | **+0.71%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.50% | **+0.35%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.35% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.05** / 初期 $100.00 (+326.05%)
- 確定: 3320件 (Win 1048 / Loss 1075 / Flat 1197) / skip 2604件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $426.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1162件 (Win 312 / Loss 254 / Flat 596) / skip 1612件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0466 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BROCCOLIF3B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 430件 (Win 143 / Loss 180 / Flat 107) / pending 0件 / skip 401件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000115 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: O/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-23T08:16:03.111682+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=65503.5
- Funnel: target 892 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +39.32% | $5,875,186.25 |
| BANK/USDT:USDT | +36.98% | $98,973,019.86 |
| RIF/USDT:USDT | +28.19% | $5,751,405.11 |
| ON/USDT:USDT | +21.01% | $4,417,699.87 |
| ZAMA/USDT:USDT | +18.42% | $5,031,652.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +1.92% | +1.77% |
| BANK/USDT:USDT | below_1h_threshold | +1.85% | +1.70% |
| WLFI/USDT:USDT | below_1h_threshold | +1.38% | +1.23% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.34% | +1.19% |
| UB/USDT:USDT | below_1h_threshold | +1.11% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
