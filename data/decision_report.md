# Decision Report

- generated_at: 2026-09-17T20:26:33.435828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14836**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14836, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.78% | **+1.39%** |
| LIMIT_6PCT | 8/20 | 40.0% | +3.44% | **+1.38%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.65% | **+2.12%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.32% | **+1.97%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.53% | **+1.46%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.87% | **+1.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.18% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5603件 (Win 1679 / Loss 1814 / Flat 2110) / skip 5794件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$242.27** / 初期 $100.00 (+142.27%)
- 確定: 3134件 (Win 873 / Loss 747 / Flat 1514) / skip 5113件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1027 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $242.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2958件 (Win 878 / Loss 1165 / Flat 915) / pending 0件 / skip 3355件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000267 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T20:26:20.504623+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=76683.3
- Funnel: target 1052 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +43.81% | $2,148,903.63 |
| COTI/USDT:USDT | +17.97% | $3,136,283.65 |
| ONE/USDT:USDT | +17.40% | $32,803,256.20 |
| PIEVERSE/USDT:USDT | +12.28% | $1,384,113.14 |
| UNI/USDT:USDT | +9.35% | $49,092,992.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +2.89% | +2.73% |
| AKE/USDT:USDT | below_1h_threshold | +2.81% | +2.65% |
| USELESS/USDT:USDT | below_1h_threshold | +2.37% | +2.21% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.21% | +2.05% |
| UNI/USDT:USDT | below_1h_threshold | +2.02% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
