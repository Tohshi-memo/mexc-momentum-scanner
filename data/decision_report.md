# Decision Report

- generated_at: 2026-09-21T22:51:29.029396+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15281**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15281, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +0.35% | **+0.25%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.88% | **+0.22%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.13% | **+0.03%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.08% | **-0.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.51% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.94%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.13% | **+0.73%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,186.74** / 初期 $100.00 (+1086.74%)
- 確定: 5772件 (Win 1717 / Loss 1854 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,186.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$250.53** / 初期 $100.00 (+150.53%)
- 確定: 3321件 (Win 918 / Loss 766 / Flat 1637) / skip 5371件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0679 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $250.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.21** / 初期 $100.00 (+23.21%)
- 確定: 3054件 (Win 898 / Loss 1193 / Flat 963) / pending 5件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000307 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.21

## 6. Latest Market Context

- 更新: 2026-09-21T22:51:20.261348+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=86352.1
- Funnel: target 1055 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +29.39% | $8,352,777.09 |
| ALCH/USDT:USDT | +28.60% | $2,026,313.08 |
| PTB/USDT:USDT | +16.41% | $1,197,817.01 |
| GRASS/USDT:USDT | +16.07% | $1,868,360.79 |
| 4STOCK/USDT:USDT | +14.50% | $1,008,675.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +3.43% | +3.66% |
| PTB/USDT:USDT | below_1h_threshold | +2.73% | +2.96% |
| OP/USDT:USDT | below_1h_threshold | +2.20% | +2.42% |
| EVAA/USDT:USDT | below_1h_threshold | +2.00% | +2.22% |
| WLD/USDT:USDT | below_1h_threshold | +1.66% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
