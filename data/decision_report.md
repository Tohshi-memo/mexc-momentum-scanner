# Decision Report

- generated_at: 2026-09-22T20:51:45.064344+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15360**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15360, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.29% | **-1.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.11% | **+1.40%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.62% | **+1.39%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.37% | **+1.09%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.10% | **+1.08%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.16% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,161.63** / 初期 $100.00 (+1061.63%)
- 確定: 5843件 (Win 1729 / Loss 1879 / Flat 2235) / skip 6078件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSEBOOK/USDT:USDT `LIMIT_8PCT_LONG` TP_HIT account +1.00% 残高後 $1,161.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5418件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.15** / 初期 $100.00 (+22.15%)
- 確定: 3115件 (Win 914 / Loss 1222 / Flat 979) / pending 5件 / skip 3721件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUSEBOOK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.15

## 6. Latest Market Context

- 更新: 2026-09-22T20:51:30.646686+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=86268.4
- Funnel: target 1058 → liquid 190 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.6 >= 65=1, 4h RSI 89.0 >= 65=1, 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUSEBOOK/USDT:USDT | +52.94% | $1,082,769.91 |
| DRIFT/USDT:USDT | +31.67% | $1,449,219.31 |
| FOLKS/USDT:USDT | +22.55% | $1,361,669.13 |
| MUBARAK/USDT:USDT | +19.73% | $15,935,707.17 |
| 4/USDT:USDT | +18.42% | $1,996,343.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.41% | +3.26% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.31% | +2.16% |
| PENGU/USDT:USDT | below_1h_threshold | +2.22% | +2.07% |
| FORM/USDT:USDT | below_1h_threshold | +2.17% | +2.02% |
| APT/USDT:USDT | below_1h_threshold | +2.04% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
