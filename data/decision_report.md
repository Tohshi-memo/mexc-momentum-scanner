# Decision Report

- generated_at: 2026-10-20T15:26:35.433274+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17066**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17066, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/10 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.09% | **+1.57%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.51% | **+1.29%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.45% | **+1.01%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.03% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 247件 (TP 91 / SL 149 / EXP 7)
- 最新: BAT/USDT:USDT SL_HIT PnL -3.97% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,330.85** / 初期 $100.00 (+1230.85%)
- 確定: 6485件 (Win 1887 / Loss 2070 / Flat 2528) / skip 7142件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,330.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$282.07** / 初期 $100.00 (+182.07%)
- 確定: 3814件 (Win 1050 / Loss 890 / Flat 1874) / skip 6663件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0746 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $282.07

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5230件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T15:26:20.612979+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.90% price=82493.4
- Funnel: target 1084 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +132.44% | $23,234,871.38 |
| APR/USDT:USDT | +20.76% | $1,562,664.07 |
| ALT/USDT:USDT | +19.77% | $2,654,198.89 |
| BAT/USDT:USDT | +17.40% | $9,695,898.39 |
| BR/USDT:USDT | +15.29% | $50,868,473.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.72% | +5.62% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +3.01% | +3.91% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.85% | +3.75% |
| XMR/USDT:USDT | below_1h_threshold | +0.71% | +1.61% |
| BTW/USDT:USDT | below_1h_threshold | +0.70% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
