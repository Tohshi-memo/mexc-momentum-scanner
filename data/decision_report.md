# Decision Report

- generated_at: 2026-08-01T08:16:15.841941+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10074**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.14% / filled 20/20。**
- 全期間 MARKET基準: n=10074, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.14% | **+2.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.19% | **+0.89%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.00% | **+0.55%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.82% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.08% | **+0.16%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.16% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$565.22** / 初期 $100.00 (+465.22%)
- 確定: 3626件 (Win 1156 / Loss 1189 / Flat 1281) / skip 3009件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.48% 残高後 $565.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2206件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.50** / 初期 $100.00 (+11.50%)
- 確定: 886件 (Win 285 / Loss 351 / Flat 250) / pending 3件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000103 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $111.50

## 6. Latest Market Context

- 更新: 2026-08-01T08:16:08.653032+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=63072.1
- Funnel: target 921 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +36.36% | $1,286,417.78 |
| KOMA/USDT:USDT | +26.83% | $16,396,767.97 |
| BTW/USDT:USDT | +26.21% | $4,663,635.15 |
| TLM/USDT:USDT | +22.33% | $2,543,637.69 |
| GIGGLE/USDT:USDT | +20.05% | $28,673,307.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KOMA/USDT:USDT | below_1h_threshold | +3.57% | +3.49% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.52% | +2.44% |
| BEAT/USDT:USDT | below_1h_threshold | +2.14% | +2.06% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.39% | +1.30% |
| BANK/USDT:USDT | below_1h_threshold | +1.14% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
