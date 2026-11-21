# Decision Report

- generated_at: 2026-11-21T16:46:36.781321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19321**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=19321, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +2.33% | **+2.09%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.09% | **+1.99%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_BB3S | 7/15 | 46.7% | +1.98% | **+0.92%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.35% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +4.37% | **+2.18%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +4.34% | **+2.17%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.86% | **+2.00%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +3.14% | **+1.88%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.23% | **+1.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,727.37** / 初期 $100.00 (+1627.37%)
- 確定: 7464件 (Win 2143 / Loss 2402 / Flat 2919) / skip 8418件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.44% 残高後 $1,727.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$448.22** / 初期 $100.00 (+348.22%)
- 確定: 5124件 (Win 1363 / Loss 1100 / Flat 2661) / skip 7608件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0001 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $448.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7482件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T16:46:15.280017+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=60022.6
- Funnel: target 1086 → liquid 141 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +10.92% | $1,435,689.17 |
| BTW/USDT:USDT | +5.42% | $5,184,719.08 |
| DODO/USDT:USDT | +5.30% | $1,369,636.05 |
| PIEVERSE/USDT:USDT | +4.58% | $4,318,518.65 |
| BARD/USDT:USDT | +2.39% | $4,010,079.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.58% | +4.39% |
| BARD/USDT:USDT | below_1h_threshold | +2.40% | +2.21% |
| MMT/USDT:USDT | below_1h_threshold | +2.29% | +2.10% |
| AKE/USDT:USDT | below_1h_threshold | +2.22% | +2.03% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.06% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
