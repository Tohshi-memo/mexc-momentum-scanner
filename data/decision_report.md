# Decision Report

- generated_at: 2026-07-22T00:41:19.195320+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9228**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9228, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.27% | **-2.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.15% | **+1.03%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.08% | **+0.92%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.13% | **+0.90%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.20% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.28% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.85% | **+3.15%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.51% | **+1.88%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.67% | **+1.50%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +4.08% | **+1.22%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.94% | **+1.03%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2539件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1480件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定: 373件 (Win 125 / Loss 155 / Flat 93) / pending 4件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000084 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $101.34

## 6. Latest Market Context

- 更新: 2026-07-22T00:41:12.085933+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=66666.1
- Funnel: target 885 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +33.34% | $3,846,548.84 |
| BANK/USDT:USDT | +23.08% | $115,681,513.84 |
| PONS/USDT:USDT | +22.47% | $1,955,933.10 |
| SMCISTOCK/USDT:USDT | +20.69% | $3,432,634.90 |
| FWDISTOCK/USDT:USDT | +11.98% | $3,926,192.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.28% | +4.06% |
| RE/USDT:USDT | below_1h_threshold | +3.36% | +3.15% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.64% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.20% | +1.98% |
| POETSTOCK/USDT:USDT | below_1h_threshold | +1.92% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
