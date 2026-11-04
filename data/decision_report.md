# Decision Report

- generated_at: 2026-11-04T18:01:18.877388+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18128**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18128, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.40% | **+0.22%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.95% | **+1.33%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.70% | **+1.08%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.19% | **+0.99%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,490.41** / 初期 $100.00 (+1390.41%)
- 確定: 6947件 (Win 2008 / Loss 2228 / Flat 2711) / skip 7742件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,490.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$371.47** / 初期 $100.00 (+271.47%)
- 確定: 4539件 (Win 1216 / Loss 1020 / Flat 2303) / skip 7000件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $371.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6294件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000099 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T18:01:08.449851+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=80489.9
- Funnel: target 1078 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INTW/USDT:USDT | +6.52% | $2,006,030.00 |
| CLANKER/USDT:USDT | +5.85% | $8,771,089.66 |
| LYN/USDT:USDT | +5.66% | $1,239,519.63 |
| SOXL/USDT:USDT | +5.01% | $732,925,180.66 |
| AIN/USDT:USDT | +4.07% | $1,875,387.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTW/USDT:USDT | below_1h_threshold | +3.24% | +3.11% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.26% |
| TESLA/USDT:USDT | below_1h_threshold | +1.55% | +1.42% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.51% | +1.38% |
| NGAS/USDT:USDT | below_1h_threshold | +1.32% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
