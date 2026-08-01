# Decision Report

- generated_at: 2026-08-01T09:11:21.691534+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10077**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.46% / filled 20/20。**
- 全期間 MARKET基準: n=10077, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.51% | **+1.21%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.84% | **+1.10%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.77% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.08% | **+0.16%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.77% | **-0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$570.87** / 初期 $100.00 (+470.87%)
- 確定: 3627件 (Win 1157 / Loss 1189 / Flat 1281) / skip 3011件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $570.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2209件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.50** / 初期 $100.00 (+11.50%)
- 確定: 888件 (Win 285 / Loss 351 / Flat 252) / pending 3件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000087 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $111.50

## 6. Latest Market Context

- 更新: 2026-08-01T09:11:13.099476+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63096.1
- Funnel: target 921 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +44.62% | $1,366,061.51 |
| KOMA/USDT:USDT | +32.61% | $16,089,209.92 |
| BTW/USDT:USDT | +29.53% | $5,187,973.51 |
| TAKE/USDT:USDT | +27.50% | $1,009,400.16 |
| GIGGLE/USDT:USDT | +22.78% | $27,791,882.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KOMA/USDT:USDT | below_1h_threshold | +4.80% | +4.80% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.49% | +2.49% |
| AKE/USDT:USDT | below_1h_threshold | +2.24% | +2.24% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.55% | +1.55% |
| EVAA/USDT:USDT | below_1h_threshold | +1.15% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
