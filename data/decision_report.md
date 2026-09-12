# Decision Report

- generated_at: 2026-09-12T05:11:17.778633+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14287**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14287, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.35% | **+0.84%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.83% | **+1.46%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.73% | **+1.30%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.39% | **+0.83%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5427件 (Win 1635 / Loss 1760 / Flat 2032) / skip 5421件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2834件 (Win 780 / Loss 656 / Flat 1398) / skip 4864件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.76** / 初期 $100.00 (+23.76%)
- 確定: 2765件 (Win 818 / Loss 1062 / Flat 885) / pending 2件 / skip 2991件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000348 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.76

## 6. Latest Market Context

- 更新: 2026-09-12T05:11:08.338340+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77150.4
- Funnel: target 1067 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +106.16% | $2,574,286.30 |
| LSK/USDT:USDT | +60.61% | $9,164,334.29 |
| LAB/USDT:USDT | +31.53% | $15,476,495.40 |
| STORJ/USDT:USDT | +30.99% | $18,096,353.59 |
| BEAT/USDT:USDT | +16.21% | $15,774,063.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MINA/USDT:USDT | below_1h_threshold | +3.14% | +3.19% |
| 4/USDT:USDT | below_1h_threshold | +2.39% | +2.44% |
| VTHO/USDT:USDT | below_1h_threshold | +1.81% | +1.86% |
| BEAT/USDT:USDT | below_1h_threshold | +0.64% | +0.69% |
| LSK/USDT:USDT | below_1h_threshold | +0.53% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
