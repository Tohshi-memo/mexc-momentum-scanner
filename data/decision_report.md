# Decision Report

- generated_at: 2026-08-10T03:46:42.993593+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11120**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=11120, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.78% | **+1.60%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.50% | **+1.50%** |
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_BB3S | 2/15 | 13.3% | +5.72% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +2.23% | **+2.23%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.17% | **+0.97%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.55% | **+0.54%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.28% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.97** / 初期 $100.00 (+524.97%)
- 確定: 3933件 (Win 1230 / Loss 1282 / Flat 1421) / skip 3748件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $624.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3018件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1283件 (Win 397 / Loss 493 / Flat 393) / pending 0件 / skip 1311件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000058 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` EXPIRED account +0.20% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-10T03:46:31.378886+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=65010.0
- Funnel: target 961 → liquid 161 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.4 >= 65=1, 4h RSI 68.7 >= 65=1, 4h RSI 70.7 >= 65=1, 4h RSI 85.3 >= 65=1, 4h RSI 91.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +58.03% | $83,226,117.46 |
| BMT/USDT:USDT | +57.06% | $19,198,093.88 |
| CAP/USDT:USDT | +25.52% | $2,779,826.57 |
| CASHCAT/USDT:USDT | +19.21% | $1,272,977.99 |
| TST/USDT:USDT | +16.90% | $2,978,827.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +4.41% | +4.52% |
| TST/USDT:USDT | below_1h_threshold | +3.99% | +4.09% |
| COOKIE/USDT:USDT | below_1h_threshold | +2.74% | +2.85% |
| BOME/USDT:USDT | below_1h_threshold | +1.89% | +2.00% |
| CAP/USDT:USDT | below_1h_threshold | +1.72% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
