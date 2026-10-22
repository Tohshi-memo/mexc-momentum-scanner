# Decision Report

- generated_at: 2026-10-22T13:51:21.133836+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17147**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17147, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/20 | 30.0% | +4.83% | **+1.45%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.98% | **+0.68%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.61% | **+0.88%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.16% | **+0.08%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.03% | **-0.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.94% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.04** / 初期 $100.00 (+1242.04%)
- 確定: 6529件 (Win 1897 / Loss 2083 / Flat 2549) / skip 7179件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,342.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.63** / 初期 $100.00 (+177.63%)
- 確定: 3847件 (Win 1055 / Loss 899 / Flat 1893) / skip 6711件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $277.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5308件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T13:51:09.672552+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=81431.9
- Funnel: target 1096 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PTB/USDT:USDT | +46.81% | $2,859,570.20 |
| MAGMA/USDT:USDT | +42.57% | $5,754,044.16 |
| AGT/USDT:USDT | +24.36% | $5,131,508.60 |
| BILL/USDT:USDT | +15.77% | $1,264,480.22 |
| BTW/USDT:USDT | +14.83% | $34,661,894.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +3.73% | +3.99% |
| AXIS/USDT:USDT | below_1h_threshold | +2.58% | +2.85% |
| PHA/USDT:USDT | below_1h_threshold | +1.91% | +2.18% |
| SOXS/USDT:USDT | below_1h_threshold | +1.71% | +1.97% |
| Q/USDT:USDT | below_1h_threshold | +0.72% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
