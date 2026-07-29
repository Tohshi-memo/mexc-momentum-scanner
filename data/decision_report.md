# Decision Report

- generated_at: 2026-07-29T00:52:05.497847+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9743**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=9743, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.96%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.51% | **+0.30%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.39% | **+0.25%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.01% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.63% | **+0.50%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.10% | **+0.07%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.04% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$108.52** / 初期 $100.00 (+8.52%)
- 確定トレード: 151件 (TP 53 / SL 93 / EXP 5)
- 最新: SNXX/USDT:USDT TP_HIT PnL +8.00% 残高後 $108.52
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$509.13** / 初期 $100.00 (+409.13%)
- 確定: 3513件 (Win 1113 / Loss 1141 / Flat 1259) / skip 2791件
- 成長率目線: 平均log +0.000463 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KAITO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $509.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1928件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0997 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.55** / 初期 $100.00 (+10.55%)
- 確定: 758件 (Win 246 / Loss 289 / Flat 223) / pending 2件 / skip 463件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000386 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KAITO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $110.55

## 6. Latest Market Context

- 更新: 2026-07-29T00:51:43.648056+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=64020.0
- Funnel: target 904 → liquid 169 → pre 50 → checked 50 → surge 6 → strict 6
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +21.46% | $1,320,883.40 |
| ZIL/USDT:USDT | +19.52% | $8,388,138.21 |
| BTW/USDT:USDT | +17.07% | $6,456,128.89 |
| ON/USDT:USDT | +14.27% | $49,978,863.02 |
| BEAT/USDT:USDT | +12.80% | $48,943,560.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +4.14% | +3.96% |
| AKE/USDT:USDT | below_1h_threshold | +3.77% | +3.58% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +3.41% | +3.23% |
| BTW/USDT:USDT | below_1h_threshold | +3.40% | +3.21% |
| ZIL/USDT:USDT | below_1h_threshold | +3.34% | +3.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
