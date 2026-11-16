# Decision Report

- generated_at: 2026-11-16T04:26:27.978387+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18994**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=18994, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.61% | **+0.49%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.09% | **+0.41%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.52% | **+0.34%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.66% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +0.84% | **+0.67%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +1.07% | **+0.48%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.21% | **+0.15%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.06% | **-0.02%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.04% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,720.18** / 初期 $100.00 (+1620.18%)
- 確定: 7337件 (Win 2107 / Loss 2349 / Flat 2881) / skip 8218件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,720.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.80** / 初期 $100.00 (+329.80%)
- 確定: 4982件 (Win 1331 / Loss 1081 / Flat 2570) / skip 7423件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $429.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7154件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T04:26:18.155591+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=65019.0
- Funnel: target 1066 → liquid 113 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +38.96% | $6,058,549.75 |
| SKR/USDT:USDT | +34.84% | $1,519,049.77 |
| SHELL/USDT:USDT | +12.65% | $1,540,313.56 |
| PIEVERSE/USDT:USDT | +9.09% | $2,008,688.92 |
| MSTRSTOCK/USDT:USDT | +4.50% | $8,665,332.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.48% | +3.57% |
| JCT/USDT:USDT | below_1h_threshold | +1.08% | +1.17% |
| VVV/USDT:USDT | below_1h_threshold | +0.66% | +0.75% |
| BLESS/USDT:USDT | below_1h_threshold | +0.63% | +0.72% |
| QNT/USDT:USDT | below_1h_threshold | +0.44% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
