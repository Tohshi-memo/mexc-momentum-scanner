# Decision Report

- generated_at: 2026-08-11T10:46:31.605929+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11245**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11245, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 19/20 | 95.0% | +1.07% | **+1.02%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.14% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.90% | **+1.74%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.80% | **+1.40%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 177件 (TP 68 / SL 104 / EXP 5)
- 最新: EPIC/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3937件 (Win 1230 / Loss 1285 / Flat 1422) / skip 3869件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1514件 (Win 424 / Loss 361 / Flat 729) / skip 3142件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.84** / 初期 $100.00 (+14.84%)
- 確定: 1330件 (Win 407 / Loss 524 / Flat 399) / pending 1件 / skip 1388件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000059 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.84

## 6. Latest Market Context

- 更新: 2026-08-11T10:46:22.198872+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64253.8
- Funnel: target 963 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1, 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +90.67% | $19,561,688.47 |
| VELVET/USDT:USDT | +61.99% | $8,798,912.94 |
| BTR/USDT:USDT | +38.80% | $1,241,501.02 |
| TOAD/USDT:USDT | +24.88% | $1,492,971.55 |
| CYS/USDT:USDT | +22.23% | $27,472,562.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQD/USDT:USDT | below_1h_threshold | +3.14% | +3.18% |
| CYS/USDT:USDT | below_1h_threshold | +2.54% | +2.59% |
| BTW/USDT:USDT | below_1h_threshold | +1.81% | +1.85% |
| CAP/USDT:USDT | below_1h_threshold | +1.13% | +1.18% |
| MAV/USDT:USDT | below_1h_threshold | +0.88% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
