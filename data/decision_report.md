# Decision Report

- generated_at: 2026-08-16T18:16:14.497490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11758**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=11758, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.83% | **+0.62%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.40% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.82% | **+1.91%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.50% | **+0.90%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.63% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.02% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4136件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.89** / 初期 $100.00 (+54.89%)
- 確定: 1784件 (Win 495 / Loss 417 / Flat 872) / skip 3385件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0012 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CROSS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.30** / 初期 $100.00 (+19.30%)
- 確定: 1655件 (Win 501 / Loss 626 / Flat 528) / pending 3件 / skip 1572件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $119.30

## 6. Latest Market Context

- 更新: 2026-08-16T18:16:07.651009+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63113.1
- Funnel: target 986 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +17.90% | $7,396,910.71 |
| APR/USDT:USDT | +10.73% | $4,739,579.25 |
| CYS/USDT:USDT | +6.42% | $48,438,022.85 |
| RIVER/USDT:USDT | +5.61% | $2,021,339.55 |
| BASED/USDT:USDT | +2.88% | $4,670,055.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +4.84% | +4.87% |
| CYS/USDT:USDT | below_1h_threshold | +3.64% | +3.66% |
| BEAT/USDT:USDT | below_1h_threshold | +1.90% | +1.92% |
| SPORTFUN/USDT:USDT | below_1h_threshold | +1.34% | +1.37% |
| TUT/USDT:USDT | below_1h_threshold | +1.14% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
