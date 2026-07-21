# Decision Report

- generated_at: 2026-07-21T21:56:34.798790+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9214**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9214, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +0.41% | **+0.12%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.10% | **+0.03%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.11% | **+0.03%** |
| LIMIT_9PCT | 4/20 | 20.0% | -0.79% | **-0.16%** |
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.84% | **+0.71%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.82% | **+0.41%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.51% | **+0.23%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.38% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2525件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1466件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.03** / 初期 $100.00 (+1.03%)
- 確定: 362件 (Win 123 / Loss 155 / Flat 84) / pending 5件 / skip 324件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000079 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIGHT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $101.03

## 6. Latest Market Context

- 更新: 2026-07-21T21:56:25.501796+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=66325.8
- Funnel: target 885 → liquid 178 → pre 50 → checked 50 → surge 7 → strict 2
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1, 4h RSI 77.2 >= 65=1, 4h RSI 73.1 >= 65=1, 4h RSI 69.8 >= 65=1, 4h RSI 67.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FWDISTOCK/USDT:USDT | +19.20% | $3,681,547.89 |
| SMCISTOCK/USDT:USDT | +18.91% | $2,947,159.12 |
| SNXX/USDT:USDT | +11.50% | $1,537,062.01 |
| BEAT/USDT:USDT | +10.06% | $11,369,341.66 |
| BOTSTOCK/USDT:USDT | +9.40% | $2,647,987.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.48% | +4.55% |
| NIGHT/USDT:USDT | below_1h_threshold | +4.39% | +4.47% |
| B/USDT:USDT | below_1h_threshold | +3.74% | +3.81% |
| PLAY/USDT:USDT | below_1h_threshold | +2.81% | +2.88% |
| BRKBSTOCK/USDT:USDT | below_1h_threshold | +2.22% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
