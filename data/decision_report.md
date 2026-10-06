# Decision Report

- generated_at: 2026-10-06T15:56:57.833368+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16227**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16227, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.13% | **+0.08%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.37% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.00% | **+1.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.87% | **+0.57%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.52% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,362.80** / 初期 $100.00 (+1262.80%)
- 確定: 6268件 (Win 1845 / Loss 2005 / Flat 2418) / skip 6520件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,362.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.00** / 初期 $100.00 (+175.00%)
- 確定: 3631件 (Win 1010 / Loss 852 / Flat 1769) / skip 6007件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0683 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $275.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4395件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000439 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T15:56:35.732965+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.81% price=85864.2
- Funnel: target 1074 → liquid 172 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.3 >= 65=1, 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZCAT/USDT:USDT | +59.84% | $1,086,203.91 |
| BR/USDT:USDT | +57.06% | $62,638,293.14 |
| RLC/USDT:USDT | +49.63% | $42,745,422.74 |
| NMR/USDT:USDT | +41.86% | $11,965,921.61 |
| US/USDT:USDT | +41.22% | $1,501,753.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NMR/USDT:USDT | below_1h_threshold | +3.38% | +4.19% |
| ZRO/USDT:USDT | below_1h_threshold | +2.15% | +2.96% |
| US/USDT:USDT | below_1h_threshold | +1.77% | +2.58% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.75% | +2.57% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.75% | +2.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
