# Decision Report

- generated_at: 2026-10-18T10:26:23.964687+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16950**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16950, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +2.59% | **+1.17%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.32% | **+1.16%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.63% | **+0.65%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.50% | **+1.35%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 245件 (TP 91 / SL 147 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,273.17** / 初期 $100.00 (+1173.17%)
- 確定: 6414件 (Win 1866 / Loss 2052 / Flat 2496) / skip 7097件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.50% 残高後 $1,273.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.65** / 初期 $100.00 (+176.65%)
- 確定: 3715件 (Win 1033 / Loss 881 / Flat 1801) / skip 6646件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0817 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ICNT/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $276.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5110件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000214 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T10:26:11.966482+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=82180.2
- Funnel: target 1084 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +23.86% | $2,932,237.30 |
| ICNT/USDT:USDT | +20.46% | $12,625,921.64 |
| Q/USDT:USDT | +17.15% | $11,714,878.05 |
| AVA/USDT:USDT | +12.30% | $2,767,312.82 |
| AGT/USDT:USDT | +12.02% | $13,784,238.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +1.84% | +1.77% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +1.80% | +1.73% |
| AGT/USDT:USDT | below_1h_threshold | +1.12% | +1.05% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.68% |
| Q/USDT:USDT | below_1h_threshold | +0.52% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
