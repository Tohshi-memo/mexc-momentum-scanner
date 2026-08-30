# Decision Report

- generated_at: 2026-08-30T06:56:21.503405+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13032**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13032, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 14/19 | 73.7% | +1.49% | **+1.10%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |
| LIMIT_10PCT | 5/20 | 25.0% | +0.29% | **+0.07%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.14% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.99% | **+1.99%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.64% | **+1.32%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.58% | **+1.11%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.79% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$794.40** / 初期 $100.00 (+694.40%)
- 確定: 4802件 (Win 1463 / Loss 1579 / Flat 1760) / skip 4791件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $794.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.48** / 初期 $100.00 (+72.48%)
- 確定: 2116件 (Win 591 / Loss 517 / Flat 1008) / skip 4327件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0387 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $172.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.73** / 初期 $100.00 (+17.73%)
- 確定: 2074件 (Win 610 / Loss 803 / Flat 661) / pending 6件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000250 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.73

## 6. Latest Market Context

- 更新: 2026-08-30T06:56:09.822778+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=78234.2
- Funnel: target 1023 → liquid 118 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1, 4h RSI 74.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +79.64% | $36,723,388.18 |
| NIULAI/USDT:USDT | +71.99% | $2,945,128.60 |
| PONS/USDT:USDT | +69.23% | $1,691,642.66 |
| FONE/USDT:USDT | +43.93% | $1,459,649.44 |
| PROM/USDT:USDT | +30.35% | $15,534,041.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.70% | +4.54% |
| MOVR/USDT:USDT | below_1h_threshold | +4.54% | +4.38% |
| 4/USDT:USDT | below_1h_threshold | +4.02% | +3.86% |
| SPX/USDT:USDT | below_1h_threshold | +1.51% | +1.35% |
| UNI/USDT:USDT | below_1h_threshold | +1.33% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
