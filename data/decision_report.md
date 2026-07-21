# Decision Report

- generated_at: 2026-07-21T17:26:18.342567+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9197**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.94% / filled 20/20。**
- 全期間 MARKET基準: n=9197, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +2.42% | **+2.05%** |
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_BB3S | 3/17 | 17.6% | +3.89% | **+0.69%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_ATR | 7/20 | 35.0% | +0.77% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.38% | **+0.19%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.07% | **-0.03%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.60% | **-0.54%** |

## 2. $100 Live Portfolio

- 残高: **$106.97** / 初期 $100.00 (+6.97%)
- 確定トレード: 127件 (TP 44 / SL 78 / EXP 5)
- 最新: BANK/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3249件 (Win 1021 / Loss 1039 / Flat 1189) / skip 2509件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.12% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.74** / 初期 $100.00 (+31.74%)
- 確定: 1158件 (Win 312 / Loss 251 / Flat 595) / skip 1450件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0065 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $131.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.03** / 初期 $100.00 (+1.03%)
- 確定: 353件 (Win 123 / Loss 155 / Flat 75) / pending 3件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000116 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $101.03

## 6. Latest Market Context

- 更新: 2026-07-21T17:26:11.553822+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=66450.0
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +5.53% | $116,827,687.53 |
| AKE/USDT:USDT | +4.54% | $13,662,866.87 |
| MUU/USDT:USDT | +4.47% | $1,336,468.56 |
| TLM/USDT:USDT | +3.84% | $1,332,368.42 |
| SNXX/USDT:USDT | +3.67% | $1,149,916.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +4.86% | +4.95% |
| SNXX/USDT:USDT | below_1h_threshold | +4.15% | +4.24% |
| KORU/USDT:USDT | below_1h_threshold | +2.71% | +2.79% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.60% | +2.69% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.20% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
