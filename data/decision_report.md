# Decision Report

- generated_at: 2026-10-19T23:29:34.913518+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17030**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17030, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_BB3S | 2/16 | 12.5% | +0.87% | **+0.11%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.18% | **+0.07%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.94% | **-0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +4.88% | **+4.88%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.64% | **+2.11%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.93% | **+1.83%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.21% | **+1.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,281.88** / 初期 $100.00 (+1181.88%)
- 確定: 6470件 (Win 1878 / Loss 2065 / Flat 2527) / skip 7121件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZRO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.41% 残高後 $1,281.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.39** / 初期 $100.00 (+178.39%)
- 確定: 3795件 (Win 1044 / Loss 886 / Flat 1865) / skip 6646件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0464 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZRO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.27% 残高後 $278.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5192件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000182 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T23:29:20.470494+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=82020.1
- Funnel: target 1090 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +27.41% | $10,797,489.67 |
| BR/USDT:USDT | +15.96% | $31,876,317.31 |
| BTW/USDT:USDT | +14.08% | $28,410,621.83 |
| APR/USDT:USDT | +12.11% | $1,519,778.51 |
| BAT/USDT:USDT | +6.89% | $6,419,837.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +4.73% | +4.73% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.44% | +1.44% |
| Q/USDT:USDT | below_1h_threshold | +1.28% | +1.28% |
| WLD/USDT:USDT | below_1h_threshold | +0.95% | +0.95% |
| BAT/USDT:USDT | below_1h_threshold | +0.83% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
