# Decision Report

- generated_at: 2026-07-28T16:41:21.118502+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9710**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9710, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.53% | **-0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.48% | **+0.44%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.63% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.85% | **+2.14%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.59% | **+1.43%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.99% | **+1.20%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.75% | **+0.96%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.50% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$486.90** / 初期 $100.00 (+386.90%)
- 確定: 3480件 (Win 1099 / Loss 1128 / Flat 1253) / skip 2791件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $486.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1895件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1200 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.58** / 初期 $100.00 (+9.58%)
- 確定: 728件 (Win 237 / Loss 278 / Flat 213) / pending 5件 / skip 449件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000459 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $109.58

## 6. Latest Market Context

- 更新: 2026-07-28T16:41:11.703521+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63847.0
- Funnel: target 904 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +12.47% | $6,337,129.08 |
| AEON1/USDT:USDT | +4.64% | $2,724,429.79 |
| ZIL/USDT:USDT | +4.13% | $1,186,585.57 |
| BULLA/USDT:USDT | +2.93% | $2,388,735.63 |
| LIT/USDT:USDT | +2.84% | $3,371,453.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEON1/USDT:USDT | below_1h_threshold | +4.65% | +4.73% |
| ZIL/USDT:USDT | below_1h_threshold | +4.14% | +4.22% |
| LIT/USDT:USDT | below_1h_threshold | +2.94% | +3.02% |
| BULLA/USDT:USDT | below_1h_threshold | +2.94% | +3.02% |
| BASTOCK/USDT:USDT | below_1h_threshold | +2.45% | +2.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
