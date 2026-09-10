# Decision Report

- generated_at: 2026-09-10T17:46:35.546014+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14174**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=14174, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/16 | 18.8% | +6.33% | **+1.19%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.66% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +4.98% | **+4.98%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.86% | **+0.47%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 207件 (TP 78 / SL 124 / EXP 5)
- 最新: HEMI/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,074.20** / 初期 $100.00 (+974.20%)
- 確定: 5354件 (Win 1611 / Loss 1729 / Flat 2014) / skip 5381件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ETHFI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,074.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.18** / 初期 $100.00 (+108.18%)
- 確定: 2768件 (Win 765 / Loss 649 / Flat 1354) / skip 4817件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0978 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.69** / 初期 $100.00 (+22.69%)
- 確定: 2679件 (Win 791 / Loss 1023 / Flat 865) / pending 4件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000454 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.69

## 6. Latest Market Context

- 更新: 2026-09-10T17:46:22.099438+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=77333.7
- Funnel: target 1067 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +9.54% | $8,808,497.71 |
| SAGA/USDT:USDT | +8.99% | $2,920,451.97 |
| 4STOCK/USDT:USDT | +8.66% | $2,463,160.09 |
| BTW/USDT:USDT | +6.82% | $1,665,252.20 |
| NIULAI/USDT:USDT | +6.35% | $1,402,817.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +3.78% | +3.57% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.72% | +3.51% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.65% | +3.44% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.27% | +3.06% |
| SOPH/USDT:USDT | below_1h_threshold | +2.55% | +2.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
