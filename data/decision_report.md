# Decision Report

- generated_at: 2026-08-24T22:26:36.487149+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12548**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12548, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_9PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT | 7/20 | 35.0% | -0.34% | **-0.12%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.39% | **-0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.80% | **+1.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.94% | **+1.17%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$694.73** / 初期 $100.00 (+594.73%)
- 確定: 4531件 (Win 1382 / Loss 1487 / Flat 1662) / skip 4578件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $694.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3986件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.64** / 初期 $100.00 (+15.64%)
- 確定: 1911件 (Win 561 / Loss 726 / Flat 624) / pending 2件 / skip 2113件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000039 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.64

## 6. Latest Market Context

- 更新: 2026-08-24T22:26:25.855596+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=78788.9
- Funnel: target 1022 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +73.71% | $3,303,100.47 |
| CASHCAT/USDT:USDT | +17.09% | $2,571,981.37 |
| ONG/USDT:USDT | +10.43% | $2,179,804.37 |
| STORJ/USDT:USDT | +8.32% | $4,329,765.30 |
| CYS/USDT:USDT | +7.09% | $2,713,006.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MONAD/USDT:USDT | below_1h_threshold | +2.30% | +2.49% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.40% | +1.60% |
| RE/USDT:USDT | below_1h_threshold | +1.10% | +1.30% |
| CRV/USDT:USDT | below_1h_threshold | +0.97% | +1.17% |
| CYS/USDT:USDT | below_1h_threshold | +0.74% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
