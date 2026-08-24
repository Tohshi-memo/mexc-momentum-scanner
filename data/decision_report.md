# Decision Report

- generated_at: 2026-08-24T07:26:27.768214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12498**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=12498, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.53% | **+1.38%** |
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.21% | **+0.91%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.41% | **+0.55%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.16% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.19% | **-0.09%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.23% | **-0.13%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | -0.67% | **-0.20%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.37% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4509件 (Win 1375 / Loss 1477 / Flat 1657) / skip 4550件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1965件 (Win 536 / Loss 470 / Flat 959) / skip 3944件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GPS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.21** / 初期 $100.00 (+16.21%)
- 確定: 1883件 (Win 554 / Loss 713 / Flat 616) / pending 3件 / skip 2084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000034 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.21

## 6. Latest Market Context

- 更新: 2026-08-24T07:26:18.776658+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=77650.0
- Funnel: target 1019 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +62.02% | $1,088,385.47 |
| TUT/USDT:USDT | +37.02% | $52,124,966.49 |
| PROM/USDT:USDT | +32.07% | $8,904,794.01 |
| BASECAT/USDT:USDT | +19.96% | $3,114,229.62 |
| UAI/USDT:USDT | +16.74% | $10,208,281.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_relative_strength | +5.20% | +4.95% |
| BASECAT/USDT:USDT | below_1h_threshold | +4.11% | +3.86% |
| PROM/USDT:USDT | below_1h_threshold | +4.05% | +3.80% |
| RE/USDT:USDT | below_1h_threshold | +2.99% | +2.74% |
| UAI/USDT:USDT | below_1h_threshold | +2.46% | +2.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
