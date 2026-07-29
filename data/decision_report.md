# Decision Report

- generated_at: 2026-07-29T20:21:23.523514+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9834**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.83% / filled 20/20。**
- 全期間 MARKET基準: n=9834, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.83% | **+3.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.83% | **+3.83%** |
| LIMIT_1PCT | 15/20 | 75.0% | +3.58% | **+2.69%** |
| LIMIT_2PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_3PCT | 8/20 | 40.0% | +1.34% | **+0.54%** |
| LIMIT_4PCT | 6/20 | 30.0% | +0.01% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | -0.64% | **-0.45%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -2.15% | **-0.75%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | -1.54% | **-1.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.67** / 初期 $100.00 (+21.67%)
- 確定トレード: 164件 (TP 65 / SL 94 / EXP 5)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.67
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2876件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2003件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 0件 / skip 542件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-29T20:21:15.753052+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=63635.9
- Funnel: target 911 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +18.21% | $5,292,943.77 |
| AEON1/USDT:USDT | +7.96% | $2,535,842.72 |
| DIA/USDT:USDT | +7.89% | $2,279,580.85 |
| LAB/USDT:USDT | +6.45% | $2,137,012.15 |
| ANSEM/USDT:USDT | +4.75% | $1,031,563.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +3.60% | +3.49% |
| DEXE/USDT:USDT | below_1h_threshold | +2.85% | +2.74% |
| ALLO/USDT:USDT | below_1h_threshold | +2.01% | +1.90% |
| SYN/USDT:USDT | below_1h_threshold | +1.90% | +1.78% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.63% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
