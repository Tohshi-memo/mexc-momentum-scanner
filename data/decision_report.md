# Decision Report

- generated_at: 2026-08-30T06:41:24.849776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13029**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13029, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 14/18 | 77.8% | +1.87% | **+1.45%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.74% | **+0.96%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.73% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_10PCT | 4/20 | 20.0% | +1.36% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.12% | **+1.56%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.37% | **+1.42%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$793.04** / 初期 $100.00 (+693.04%)
- 確定: 4799件 (Win 1462 / Loss 1578 / Flat 1759) / skip 4791件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $793.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.69** / 初期 $100.00 (+73.69%)
- 確定: 2113件 (Win 591 / Loss 515 / Flat 1007) / skip 4327件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0533 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $173.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.73** / 初期 $100.00 (+17.73%)
- 確定: 2072件 (Win 610 / Loss 803 / Flat 659) / pending 6件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000281 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.73

## 6. Latest Market Context

- 更新: 2026-08-30T06:41:14.670966+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=78230.1
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.5 >= 65=1, 4h RSI 74.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +71.74% | $36,015,327.58 |
| NIULAI/USDT:USDT | +69.63% | $2,862,179.39 |
| PONS/USDT:USDT | +57.86% | $1,620,420.92 |
| FONE/USDT:USDT | +45.53% | $1,449,683.07 |
| PROM/USDT:USDT | +31.21% | $15,449,231.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.52% | +3.36% |
| MOVR/USDT:USDT | below_1h_threshold | +3.08% | +2.93% |
| PROM/USDT:USDT | below_1h_threshold | +1.57% | +1.41% |
| 4/USDT:USDT | below_1h_threshold | +1.54% | +1.39% |
| DOS/USDT:USDT | below_1h_threshold | +1.46% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
