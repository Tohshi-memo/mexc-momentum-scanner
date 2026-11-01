# Decision Report

- generated_at: 2026-11-01T03:36:32.825657+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17925**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.49% / filled 20/20。**
- 全期間 MARKET基準: n=17925, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.49% | **+2.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.49% | **+2.49%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.13% | **+0.85%** |
| LIMIT_BB3S | 4/18 | 22.2% | +3.73% | **+0.83%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.79% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.74% | **-0.33%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -1.59% | **-0.56%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -2.01% | **-0.90%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 257件 (TP 95 / SL 154 / EXP 8)
- 最新: JCT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.74** / 初期 $100.00 (+1385.74%)
- 確定: 6821件 (Win 1976 / Loss 2188 / Flat 2657) / skip 7665件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GANG/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,485.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$370.19** / 初期 $100.00 (+270.19%)
- 確定: 4418件 (Win 1185 / Loss 983 / Flat 2250) / skip 6918件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0583 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $370.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6085件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000492 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-01T03:36:15.188915+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77752.0
- Funnel: target 1089 → liquid 119 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.1 >= 65=1, 4h RSI 73.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +23.96% | $22,833,193.18 |
| POWR/USDT:USDT | +17.93% | $1,782,473.65 |
| ESPORTS/USDT:USDT | +12.72% | $1,390,235.93 |
| IDOL/USDT:USDT | +11.97% | $5,029,959.15 |
| LIT/USDT:USDT | +8.54% | $16,684,053.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.57% | +4.49% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.59% | +3.51% |
| AIOT/USDT:USDT | below_1h_threshold | +3.44% | +3.36% |
| PONS/USDT:USDT | below_1h_threshold | +3.28% | +3.20% |
| BTW/USDT:USDT | below_1h_threshold | +2.56% | +2.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
