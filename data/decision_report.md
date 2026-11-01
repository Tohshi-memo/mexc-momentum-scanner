# Decision Report

- generated_at: 2026-11-01T02:31:21.912659+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17920**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.58% / filled 20/20。**
- 全期間 MARKET基準: n=17920, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.58% | **+3.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.58% | **+3.58%** |
| LIMIT_1PCT | 15/20 | 75.0% | +2.58% | **+1.94%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.47% | **+1.48%** |
| LIMIT_BB3S | 6/17 | 35.3% | +2.79% | **+0.99%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.82% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -1.70% | **-0.51%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -1.07% | **-0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 257件 (TP 95 / SL 154 / EXP 8)
- 最新: JCT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.74** / 初期 $100.00 (+1385.74%)
- 確定: 6821件 (Win 1976 / Loss 2188 / Flat 2657) / skip 7660件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GANG/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,485.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$370.19** / 初期 $100.00 (+270.19%)
- 確定: 4418件 (Win 1185 / Loss 983 / Flat 2250) / skip 6913件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $370.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6078件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000551 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-01T02:31:08.979204+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77690.8
- Funnel: target 1089 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POWR/USDT:USDT | +17.43% | $1,442,254.44 |
| GANG/USDT:USDT | +16.75% | $1,119,342.92 |
| LIT/USDT:USDT | +6.55% | $16,121,718.71 |
| MAGMA/USDT:USDT | +5.15% | $1,407,827.25 |
| AIOT/USDT:USDT | +4.95% | $1,071,218.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +1.71% | +1.70% |
| AAVE/USDT:USDT | below_1h_threshold | +1.29% | +1.28% |
| XPL/USDT:USDT | below_1h_threshold | +1.00% | +0.99% |
| STX/USDT:USDT | below_1h_threshold | +0.69% | +0.68% |
| XMR/USDT:USDT | below_1h_threshold | +0.67% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
