# Decision Report

- generated_at: 2026-11-21T16:01:17.678894+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19316**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19316, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.90% | **+1.81%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.78% | **+1.51%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.19% | **+1.09%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.07% | **+1.03%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +3.34% | **+2.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.77% | **+1.66%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +3.17% | **+1.58%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,703.43** / 初期 $100.00 (+1603.43%)
- 確定: 7459件 (Win 2141 / Loss 2401 / Flat 2917) / skip 8418件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,703.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$449.80** / 初期 $100.00 (+349.80%)
- 確定: 5121件 (Win 1363 / Loss 1099 / Flat 2659) / skip 7606件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0166 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $449.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7477件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T16:01:06.220622+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=59917.0
- Funnel: target 1086 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +2.63% | $53,064,623.20 |
| SKYAI/USDT:USDT | +0.83% | $1,053,014.96 |
| PIEVERSE/USDT:USDT | +0.49% | $4,041,099.06 |
| CRCLSTOCK/USDT:USDT | +0.34% | $36,195,331.26 |
| EVAA/USDT:USDT | +0.32% | $29,284,301.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.63% | +2.62% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.80% | +0.79% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.69% | +0.68% |
| MMT/USDT:USDT | below_1h_threshold | +0.23% | +0.22% |
| ENA/USDT:USDT | below_1h_threshold | +0.20% | +0.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
