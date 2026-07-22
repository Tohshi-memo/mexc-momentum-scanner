# Decision Report

- generated_at: 2026-07-22T00:31:23.754771+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9226**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9226, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.21% | **-2.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.37% | **+0.84%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.10% | **+0.74%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.58% | **+0.49%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.21% | **+0.44%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.27% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +5.04% | **+3.53%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.60% | **+1.95%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.52% | **+1.41%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.01% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2537件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1478件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定: 371件 (Win 125 / Loss 155 / Flat 91) / pending 4件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000084 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $101.34

## 6. Latest Market Context

- 更新: 2026-07-22T00:31:16.541503+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=66615.2
- Funnel: target 885 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +32.85% | $3,809,809.72 |
| PONS/USDT:USDT | +24.07% | $1,915,630.87 |
| SMCISTOCK/USDT:USDT | +21.09% | $3,414,199.32 |
| BANK/USDT:USDT | +19.78% | $114,836,649.45 |
| SNXX/USDT:USDT | +12.33% | $1,911,790.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.34% | +3.20% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.72% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.10% | +1.96% |
| POETSTOCK/USDT:USDT | below_1h_threshold | +1.92% | +1.78% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +1.55% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
