# Decision Report

- generated_at: 2026-09-29T00:01:29.058368+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15749**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=15749, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.12% | **+0.95%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.07% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.45% | **+0.29%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.40% | **+0.28%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.01% | **-0.01%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5984件 (Win 1766 / Loss 1925 / Flat 2293) / skip 6326件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NMR/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5626件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.78** / 初期 $100.00 (+17.78%)
- 確定: 3308件 (Win 958 / Loss 1302 / Flat 1048) / pending 2件 / skip 3909件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000124 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NMR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.78

## 6. Latest Market Context

- 更新: 2026-09-29T00:01:17.743867+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=83457.5
- Funnel: target 1066 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NMR/USDT:USDT | +27.84% | $5,029,102.86 |
| BTW/USDT:USDT | +16.21% | $18,346,185.96 |
| CRV/USDT:USDT | +15.74% | $9,938,950.47 |
| GRASS/USDT:USDT | +9.65% | $4,399,713.39 |
| MARSCOIN/USDT:USDT | +9.07% | $4,295,223.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARKM/USDT:USDT | below_1h_threshold | +4.04% | +4.05% |
| XDP/USDT:USDT | below_1h_threshold | +0.87% | +0.88% |
| CRV/USDT:USDT | below_1h_threshold | +0.45% | +0.45% |
| GRASS/USDT:USDT | below_1h_threshold | +0.28% | +0.29% |
| ALGO/USDT:USDT | below_1h_threshold | +0.24% | +0.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
