# Decision Report

- generated_at: 2026-08-01T04:56:27.169917+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10060**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.95% / filled 20/20。**
- 全期間 MARKET基準: n=10060, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.95% | **+1.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_ATR | 7/20 | 35.0% | +2.91% | **+1.02%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.57% | **+0.94%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.51% | **-0.15%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.48% | **-0.19%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.56% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$562.70** / 初期 $100.00 (+462.70%)
- 確定: 3612件 (Win 1152 / Loss 1183 / Flat 1277) / skip 3009件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $562.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2192件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.70** / 初期 $100.00 (+11.70%)
- 確定: 876件 (Win 283 / Loss 347 / Flat 246) / pending 4件 / skip 655件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000203 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.70

## 6. Latest Market Context

- 更新: 2026-08-01T04:56:15.778401+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63067.9
- Funnel: target 921 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +30.67% | $1,254,709.43 |
| KOMA/USDT:USDT | +30.11% | $18,602,104.50 |
| BTW/USDT:USDT | +23.23% | $2,959,937.93 |
| GIGGLE/USDT:USDT | +18.60% | $24,613,041.24 |
| LAB/USDT:USDT | +15.89% | $2,191,994.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +2.78% | +2.63% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.61% | +2.47% |
| ZRO/USDT:USDT | below_1h_threshold | +1.71% | +1.56% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.21% | +1.06% |
| PI/USDT:USDT | below_1h_threshold | +1.02% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
