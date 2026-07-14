# Decision Report

- generated_at: 2026-07-14T21:16:20.320939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8704**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=8704, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +6.60% | **+0.66%** |
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.59% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +2.27% | **+2.02%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.98% | **+0.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +5.20% | **+0.52%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$329.76** / 初期 $100.00 (+229.76%)
- 確定: 2863件 (Win 894 / Loss 931 / Flat 1038) / skip 2402件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $329.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.49** / 初期 $100.00 (+5.49%)
- 確定: 693件 (Win 161 / Loss 162 / Flat 370) / skip 1422件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 60件 (Win 19 / Loss 39 / Flat 2) / pending 0件 / skip 114件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000145 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-14T21:16:10.167708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64598.0
- Funnel: target 862 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AEHRSTOCK/USDT:USDT | +32.20% | $1,755,438.18 |
| DODO/USDT:USDT | +10.21% | $2,510,765.00 |
| POETSTOCK/USDT:USDT | +5.33% | $7,032,777.43 |
| SKHYSTOCK/USDT:USDT | +4.94% | $10,466,950.48 |
| US/USDT:USDT | +4.66% | $1,743,826.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SXT/USDT:USDT | below_1h_threshold | +1.00% | +0.91% |
| IBMSTOCK/USDT:USDT | below_1h_threshold | +0.95% | +0.86% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.85% | +0.76% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.80% | +0.71% |
| SLX/USDT:USDT | below_1h_threshold | +0.73% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
