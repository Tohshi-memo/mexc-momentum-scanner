# Decision Report

- generated_at: 2026-10-22T10:11:28.631904+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17140**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17140, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.38% | **-2.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_BB3S | 3/17 | 17.6% | +1.30% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.14% | **+1.61%** |
| MARKET_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.93% | **+0.77%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.44% | **+0.51%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.96% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,383.02** / 初期 $100.00 (+1283.02%)
- 確定: 6522件 (Win 1897 / Loss 2077 / Flat 2548) / skip 7179件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PTB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,383.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.63** / 初期 $100.00 (+177.63%)
- 確定: 3841件 (Win 1055 / Loss 899 / Flat 1887) / skip 6710件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0535 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $277.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5301件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T10:11:14.313130+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=81974.8
- Funnel: target 1090 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PTB/USDT:USDT | +66.28% | $1,893,629.60 |
| MAGMA/USDT:USDT | +46.86% | $4,124,532.12 |
| BTW/USDT:USDT | +20.62% | $34,533,387.61 |
| AGT/USDT:USDT | +17.57% | $4,926,660.15 |
| SOXS/USDT:USDT | +11.61% | $12,099,431.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXIS/USDT:USDT | below_1h_threshold | +2.44% | +2.36% |
| BTW/USDT:USDT | below_1h_threshold | +2.23% | +2.16% |
| Q/USDT:USDT | below_1h_threshold | +1.83% | +1.76% |
| AKE/USDT:USDT | below_1h_threshold | +1.78% | +1.71% |
| BILL/USDT:USDT | below_1h_threshold | +1.75% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
