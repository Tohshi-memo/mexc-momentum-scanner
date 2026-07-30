# Decision Report

- generated_at: 2026-07-30T13:26:23.241815+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9885**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.58% / filled 20/20。**
- 全期間 MARKET基準: n=9885, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.72% | **+1.11%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.16% | **+0.79%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.50% | **+1.05%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.76% | **+0.61%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2926件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2053件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.81** / 初期 $100.00 (+11.81%)
- 確定: 790件 (Win 259 / Loss 308 / Flat 223) / pending 3件 / skip 563件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000666 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $111.81

## 6. Latest Market Context

- 更新: 2026-07-30T13:26:15.528999+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64850.8
- Funnel: target 920 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +56.90% | $2,825,522.86 |
| ESP/USDT:USDT | +25.08% | $4,780,719.69 |
| MMT/USDT:USDT | +21.53% | $1,647,281.35 |
| CAP/USDT:USDT | +21.39% | $1,658,114.87 |
| ROBO/USDT:USDT | +20.51% | $1,132,007.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +4.56% | +4.62% |
| KORU/USDT:USDT | below_1h_threshold | +4.53% | +4.59% |
| EVAA/USDT:USDT | below_1h_threshold | +3.98% | +4.05% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +3.42% | +3.49% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.27% | +3.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
