# Decision Report

- generated_at: 2026-09-04T18:16:27.108397+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13656**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13656, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.84% | **-0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.31% | **+0.28%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.07% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +2.05% | **+1.53%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.35% | **+1.22%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.79% | **+1.16%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.43% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5206件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2421件 (Win 682 / Loss 577 / Flat 1162) / skip 4646件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0375 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.39** / 初期 $100.00 (+17.39%)
- 確定: 2295件 (Win 680 / Loss 881 / Flat 734) / pending 4件 / skip 2831件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.39

## 6. Latest Market Context

- 更新: 2026-09-04T18:16:15.464250+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79491.9
- Funnel: target 1050 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +37.42% | $2,253,112.30 |
| MARSCOIN/USDT:USDT | +15.01% | $7,255,709.88 |
| SKR/USDT:USDT | +13.22% | $6,782,597.93 |
| USELESS/USDT:USDT | +8.10% | $43,710,505.50 |
| UAI/USDT:USDT | +6.37% | $5,951,685.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.40% | +4.33% |
| BASECAT/USDT:USDT | below_1h_threshold | +1.70% | +1.62% |
| USELESS/USDT:USDT | below_1h_threshold | +1.59% | +1.51% |
| CATI/USDT:USDT | below_1h_threshold | +1.19% | +1.11% |
| HNT/USDT:USDT | below_1h_threshold | +1.14% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
