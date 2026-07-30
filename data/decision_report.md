# Decision Report

- generated_at: 2026-07-30T06:46:29.533894+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9863**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.70% / filled 20/20。**
- 全期間 MARKET基準: n=9863, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.70% | **+3.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.70% | **+3.70%** |
| LIMIT_1PCT | 16/20 | 80.0% | +4.00% | **+3.20%** |
| LIMIT_2PCT | 11/20 | 55.0% | +3.19% | **+1.75%** |
| LIMIT_3PCT | 7/20 | 35.0% | +3.15% | **+1.10%** |
| LIMIT_BB3S | 4/16 | 25.0% | +4.14% | **+1.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.37% | **-0.13%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.36% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 170件 (TP 67 / SL 98 / EXP 5)
- 最新: LASERTECSTOCK/USDT:USDT TP_HIT PnL +3.98% 残高後 $121.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2905件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2032件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.51** / 初期 $100.00 (+10.51%)
- 確定: 773件 (Win 251 / Loss 299 / Flat 223) / pending 3件 / skip 562件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000874 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $110.51

## 6. Latest Market Context

- 更新: 2026-07-30T06:46:21.792423+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63992.0
- Funnel: target 916 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +18.83% | $1,639,304.28 |
| MMT/USDT:USDT | +14.43% | $1,091,247.58 |
| RE/USDT:USDT | +14.07% | $9,009,839.73 |
| MSFU/USDT:USDT | +12.66% | $2,836,864.85 |
| ADVANTESTSTOCK/USDT:USDT | +10.71% | $1,400,075.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +4.18% | +4.21% |
| ZIL/USDT:USDT | below_1h_threshold | +2.60% | +2.63% |
| US/USDT:USDT | below_1h_threshold | +1.77% | +1.81% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.59% | +1.62% |
| ADVANTESTSTOCK/USDT:USDT | below_1h_threshold | +1.23% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
