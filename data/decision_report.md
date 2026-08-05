# Decision Report

- generated_at: 2026-08-05T19:26:24.701428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10448**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10448, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.02% | **+0.01%** |
| LIMIT_BB3S | 5/20 | 25.0% | -0.18% | **-0.04%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.81% | **+1.82%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.52% | **+1.37%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.32% | **+1.04%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.98% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3239件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.29** / 初期 $100.00 (+40.29%)
- 確定: 1346件 (Win 377 / Loss 317 / Flat 652) / skip 2513件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1446 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.74** / 初期 $100.00 (+17.74%)
- 確定: 1142件 (Win 365 / Loss 444 / Flat 333) / pending 0件 / skip 782件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000522 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.74

## 6. Latest Market Context

- 更新: 2026-08-05T19:26:13.515363+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64873.3
- Funnel: target 948 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +47.29% | $92,295,924.55 |
| HEI/USDT:USDT | +33.91% | $40,873,496.01 |
| UB/USDT:USDT | +19.77% | $22,751,327.50 |
| ESPORTS/USDT:USDT | +18.69% | $4,912,843.18 |
| BICO/USDT:USDT | +15.41% | $13,493,931.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.38% | +4.21% |
| SYN/USDT:USDT | below_1h_threshold | +3.30% | +3.13% |
| MMT/USDT:USDT | below_1h_threshold | +1.45% | +1.28% |
| ON/USDT:USDT | below_1h_threshold | +1.26% | +1.09% |
| CYS/USDT:USDT | below_1h_threshold | +1.18% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
