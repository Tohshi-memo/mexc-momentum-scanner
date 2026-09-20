# Decision Report

- generated_at: 2026-09-20T09:31:29.495469+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15161**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=15161, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +2.44% | **+1.71%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.60% | **+1.52%** |
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_BB3S | 4/16 | 25.0% | +3.78% | **+0.94%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.93% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.10% | **+0.88%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.93% | **+0.59%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.55% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,192.84** / 初期 $100.00 (+1092.84%)
- 確定: 5687件 (Win 1702 / Loss 1836 / Flat 2149) / skip 6035件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,192.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.85** / 初期 $100.00 (+147.85%)
- 確定: 3274件 (Win 907 / Loss 763 / Flat 1604) / skip 5298件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0516 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $247.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T09:31:16.266474+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=80368.3
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +66.16% | $6,494,990.85 |
| AKE/USDT:USDT | +34.00% | $60,678,437.03 |
| OFC/USDT:USDT | +28.11% | $2,417,317.22 |
| ONE/USDT:USDT | +26.99% | $52,399,004.34 |
| EVAA/USDT:USDT | +20.32% | $2,044,932.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_relative_strength | +5.07% | +4.90% |
| CATE/USDT:USDT | below_1h_threshold | +4.22% | +4.05% |
| CELR/USDT:USDT | below_1h_threshold | +3.55% | +3.38% |
| S/USDT:USDT | below_1h_threshold | +2.99% | +2.83% |
| BANK/USDT:USDT | below_1h_threshold | +2.66% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
