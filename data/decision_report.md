# Decision Report

- generated_at: 2026-07-30T12:26:14.650985+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9882**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.35% / filled 20/20。**
- 全期間 MARKET基準: n=9882, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.33% | **+1.40%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.82% | **+1.18%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.18% | **+0.83%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.08% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.05% | **+0.58%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 171件 (TP 67 / SL 99 / EXP 5)
- 最新: AMZU/USDT:USDT SL_HIT PnL -2.81% 残高後 $121.53
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2923件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2051件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.82** / 初期 $100.00 (+11.82%)
- 確定: 787件 (Win 258 / Loss 306 / Flat 223) / pending 4件 / skip 562件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000788 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESP/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $111.82

## 6. Latest Market Context

- 更新: 2026-07-30T12:26:07.429077+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=64914.9
- Funnel: target 917 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +60.27% | $1,993,674.43 |
| ESP/USDT:USDT | +24.88% | $4,446,977.97 |
| MMT/USDT:USDT | +23.37% | $1,514,433.21 |
| ROBO/USDT:USDT | +16.87% | $1,046,757.10 |
| MSFU/USDT:USDT | +16.47% | $3,013,082.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARMSTOCK/USDT:USDT | below_relative_strength | +5.09% | +4.86% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.37% | +4.14% |
| KORU/USDT:USDT | below_1h_threshold | +3.99% | +3.76% |
| SOXL/USDT:USDT | below_1h_threshold | +3.35% | +3.12% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.32% | +3.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
