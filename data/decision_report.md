# Decision Report

- generated_at: 2026-09-13T04:51:21.319033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14386**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14386, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 12/20 | 60.0% | +2.13% | **+1.28%** |
| LIMIT_8PCT | 10/20 | 50.0% | +2.34% | **+1.17%** |
| LIMIT_9PCT | 8/20 | 40.0% | +1.57% | **+0.63%** |
| LIMIT_10PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.77% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/12 | 50.0% | +5.70% | **+2.85%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.56% | **+1.56%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.49% | **+1.41%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.52% | **+0.38%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5517件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$225.46** / 初期 $100.00 (+125.46%)
- 確定: 2904件 (Win 808 / Loss 685 / Flat 1411) / skip 4893件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $225.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.86** / 初期 $100.00 (+27.86%)
- 確定: 2834件 (Win 846 / Loss 1093 / Flat 895) / pending 5件 / skip 3020件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000443 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $127.86

## 6. Latest Market Context

- 更新: 2026-09-13T04:51:10.253863+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77183.1
- Funnel: target 1068 → liquid 126 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.1 >= 65=1, 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +318.59% | $82,376,920.70 |
| VTHO/USDT:USDT | +41.88% | $3,092,896.91 |
| POWR/USDT:USDT | +31.18% | $1,953,848.95 |
| ZCAT/USDT:USDT | +30.73% | $1,250,655.63 |
| SAGA/USDT:USDT | +24.44% | $1,011,544.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +2.93% | +2.90% |
| STORJ/USDT:USDT | below_1h_threshold | +2.41% | +2.38% |
| KOMA/USDT:USDT | below_1h_threshold | +2.28% | +2.25% |
| RIVER/USDT:USDT | below_1h_threshold | +2.07% | +2.04% |
| VET/USDT:USDT | below_1h_threshold | +1.38% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
