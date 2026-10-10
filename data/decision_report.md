# Decision Report

- generated_at: 2026-10-10T12:21:08.570234+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16490**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.02% / filled 20/20。**
- 全期間 MARKET基準: n=16490, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.04% | **+1.63%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.21% | **+1.03%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.35% | **+0.25%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.16% | **+1.30%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.15% | **+0.08%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.61% | **-0.09%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.19% | **-0.11%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.13% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,303.26** / 初期 $100.00 (+1203.26%)
- 確定: 6286件 (Win 1845 / Loss 2014 / Flat 2427) / skip 6765件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LPT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.46% 残高後 $1,303.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3636件 (Win 1010 / Loss 853 / Flat 1773) / skip 6265件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4650件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000240 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-10T12:20:59.940217+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=82826.3
- Funnel: target 1089 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +37.00% | $3,331,092.23 |
| ERA/USDT:USDT | +26.39% | $1,060,786.07 |
| BAT/USDT:USDT | +22.42% | $21,523,962.32 |
| CAP/USDT:USDT | +21.71% | $2,983,456.74 |
| MAGIC/USDT:USDT | +17.67% | $24,750,556.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_1h_threshold | +2.44% | +2.45% |
| CAP/USDT:USDT | below_1h_threshold | +2.29% | +2.30% |
| BAT/USDT:USDT | below_1h_threshold | +2.16% | +2.18% |
| WLD/USDT:USDT | below_1h_threshold | +1.35% | +1.37% |
| ZRX/USDT:USDT | below_1h_threshold | +1.17% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
