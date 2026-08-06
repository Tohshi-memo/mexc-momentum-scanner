# Decision Report

- generated_at: 2026-08-06T09:01:24.381915+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10556**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=10556, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.52% | **+1.22%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.38% | **+0.96%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.18% | **+2.18%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.07% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$609.98** / 初期 $100.00 (+509.98%)
- 確定: 3785件 (Win 1201 / Loss 1242 / Flat 1342) / skip 3332件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $609.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.36** / 初期 $100.00 (+41.36%)
- 確定: 1391件 (Win 386 / Loss 327 / Flat 678) / skip 2576件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1244 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $141.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 886件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000248 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T09:01:13.571670+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64899.9
- Funnel: target 955 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +146.56% | $57,983,022.47 |
| DODO/USDT:USDT | +55.23% | $9,876,499.38 |
| BLESS/USDT:USDT | +50.82% | $121,067,239.80 |
| ZBT/USDT:USDT | +34.29% | $2,164,195.67 |
| CASHCAT/USDT:USDT | +31.35% | $1,271,432.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QBTSSTOCK/USDT:USDT | below_1h_threshold | +4.57% | +4.60% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.70% | +1.73% |
| ZINC/USDT:USDT | below_1h_threshold | +1.65% | +1.67% |
| HFT/USDT:USDT | below_1h_threshold | +0.88% | +0.90% |
| BTW/USDT:USDT | below_1h_threshold | +0.83% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
