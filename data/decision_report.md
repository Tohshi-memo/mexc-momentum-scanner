# Decision Report

- generated_at: 2026-09-22T20:41:27.394588+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15358**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15358, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.88% | **-1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.38% | **+0.31%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +6.33% | **+3.16%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.63% | **+0.92%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.48% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,155.90** / 初期 $100.00 (+1055.90%)
- 確定: 5841件 (Win 1728 / Loss 1878 / Flat 2235) / skip 6078件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TIA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,155.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5416件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.36** / 初期 $100.00 (+22.36%)
- 確定: 3113件 (Win 914 / Loss 1221 / Flat 978) / pending 6件 / skip 3720件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000048 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $122.36

## 6. Latest Market Context

- 更新: 2026-09-22T20:41:16.016328+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=86299.9
- Funnel: target 1058 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1, 4h RSI 89.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUSEBOOK/USDT:USDT | +51.61% | $1,043,690.99 |
| DRIFT/USDT:USDT | +34.79% | $1,405,206.61 |
| FOLKS/USDT:USDT | +22.33% | $1,135,976.12 |
| MUBARAK/USDT:USDT | +18.44% | $15,812,644.82 |
| 4/USDT:USDT | +18.15% | $1,973,681.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_relative_strength | +5.08% | +4.89% |
| PONS/USDT:USDT | below_1h_threshold | +3.54% | +3.36% |
| PENGU/USDT:USDT | below_1h_threshold | +2.32% | +2.14% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.16% | +1.97% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.88% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
