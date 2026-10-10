# Decision Report

- generated_at: 2026-10-10T21:01:17.770449+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16514**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16514, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.98% | **+0.45%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.20% | **+0.06%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.25% | **-0.15%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.39% | **-0.36%** |
| LIMIT_FIB1272 | 13/20 | 65.0% | -0.83% | **-0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.14% | **+1.39%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.30% | **+0.80%** |
| LIMIT_BB3S_LONG | 3/11 | 27.3% | +2.74% | **+0.75%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +1.03% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 237件 (TP 88 / SL 142 / EXP 7)
- 最新: SI/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,298.24** / 初期 $100.00 (+1198.24%)
- 確定: 6288件 (Win 1845 / Loss 2015 / Flat 2428) / skip 6787件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,298.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3636件 (Win 1010 / Loss 853 / Flat 1773) / skip 6289件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4676件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000156 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-10T21:01:08.305495+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=83008.1
- Funnel: target 1087 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHIP/USDT:USDT | +32.10% | $15,204,412.08 |
| SI/USDT:USDT | +14.25% | $1,325,866.81 |
| BR/USDT:USDT | +13.89% | $6,417,790.56 |
| TIA/USDT:USDT | +12.80% | $33,270,943.78 |
| STRK/USDT:USDT | +9.66% | $51,598,058.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +0.58% | +0.56% |
| S/USDT:USDT | below_1h_threshold | +0.42% | +0.41% |
| TIA/USDT:USDT | below_1h_threshold | +0.36% | +0.35% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.25% | +0.23% |
| VVV/USDT:USDT | below_1h_threshold | +0.19% | +0.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
