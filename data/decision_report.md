# Decision Report

- generated_at: 2026-10-11T17:01:20.556398+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16564**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16564, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +1.41% | **+0.65%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.37% | **+0.35%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.40% | **+0.24%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +4.30% | **+3.58%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.31% | **+0.46%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.47% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,298.24** / 初期 $100.00 (+1198.24%)
- 確定: 6290件 (Win 1845 / Loss 2015 / Flat 2430) / skip 6835件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,298.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$273.08** / 初期 $100.00 (+173.08%)
- 確定: 3637件 (Win 1010 / Loss 854 / Flat 1773) / skip 6338件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $273.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4727件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-11T17:01:08.917315+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=83815.2
- Funnel: target 1087 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| S/USDT:USDT | +17.35% | $11,346,891.47 |
| CKB/USDT:USDT | +5.12% | $1,807,660.31 |
| ENA/USDT:USDT | +3.91% | $39,861,073.48 |
| FARTCOIN/USDT:USDT | +2.92% | $6,767,723.15 |
| RAY/USDT:USDT | +2.08% | $3,533,378.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| S/USDT:USDT | below_1h_threshold | +1.37% | +1.43% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.80% | +0.86% |
| CHIP/USDT:USDT | below_1h_threshold | +0.55% | +0.61% |
| SOXL/USDT:USDT | below_1h_threshold | +0.53% | +0.60% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.42% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
