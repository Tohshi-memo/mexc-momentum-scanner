# Decision Report

- generated_at: 2026-08-01T06:31:27.572434+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10066**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=10066, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.02% | **+0.46%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.96% | **+0.38%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.42% | **+0.23%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.07% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | -0.06% | **-0.04%** |
| MARKET_LONG | 20/20 | 100.0% | -0.08% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$562.76** / 初期 $100.00 (+462.76%)
- 確定: 3618件 (Win 1154 / Loss 1185 / Flat 1279) / skip 3009件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $562.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2198件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.60** / 初期 $100.00 (+11.60%)
- 確定: 880件 (Win 284 / Loss 349 / Flat 247) / pending 4件 / skip 655件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000232 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.60

## 6. Latest Market Context

- 更新: 2026-08-01T06:31:17.756812+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=63044.6
- Funnel: target 921 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGGLE/USDT:USDT | +36.89% | $27,574,203.59 |
| BTW/USDT:USDT | +32.97% | $3,703,107.16 |
| JIMOTHY/USDT:USDT | +23.80% | $1,256,732.14 |
| TLM/USDT:USDT | +18.15% | $1,977,404.19 |
| KOMA/USDT:USDT | +16.11% | $17,322,372.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.58% | +4.51% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.10% | +2.03% |
| OUSTSTOCK/USDT:USDT | below_1h_threshold | +1.99% | +1.92% |
| MYX/USDT:USDT | below_1h_threshold | +1.69% | +1.62% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.16% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
