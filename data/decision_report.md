# Decision Report

- generated_at: 2026-07-31T15:56:25.017611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10016**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10016, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.33% | **+0.27%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.14% | **+0.12%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.66% | **+0.80%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.63% | **+0.31%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.71% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$547.70** / 初期 $100.00 (+447.70%)
- 確定: 3573件 (Win 1141 / Loss 1168 / Flat 1264) / skip 3004件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $547.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2149件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.20** / 初期 $100.00 (+11.20%)
- 確定: 846件 (Win 273 / Loss 335 / Flat 238) / pending 6件 / skip 638件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $111.20

## 6. Latest Market Context

- 更新: 2026-07-31T15:56:16.558242+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=62726.3
- Funnel: target 921 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +104.63% | $6,450,879.84 |
| KOMA/USDT:USDT | +66.98% | $15,343,723.44 |
| GIGGLE/USDT:USDT | +34.96% | $11,964,369.71 |
| AXTISTOCK/USDT:USDT | +28.82% | $10,513,344.31 |
| AMZU/USDT:USDT | +24.91% | $1,909,950.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXTISTOCK/USDT:USDT | below_relative_strength | +5.06% | +4.96% |
| GGLL/USDT:USDT | below_1h_threshold | +4.93% | +4.83% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +2.55% | +2.45% |
| CHIP/USDT:USDT | below_1h_threshold | +2.36% | +2.26% |
| COTI/USDT:USDT | below_1h_threshold | +2.23% | +2.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
