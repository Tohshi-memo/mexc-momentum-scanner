# Decision Report

- generated_at: 2026-09-11T21:36:24.531279+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14257**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14257, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.51% | **-0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.36% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.03% | **+0.02%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.93% | **+1.54%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.42% | **+0.61%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.44% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,109.61** / 初期 $100.00 (+1009.61%)
- 確定: 5414件 (Win 1633 / Loss 1752 / Flat 2029) / skip 5404件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STONK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,109.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$210.43** / 初期 $100.00 (+110.43%)
- 確定: 2829件 (Win 779 / Loss 655 / Flat 1395) / skip 4839件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1094 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STONK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $210.43

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.44** / 初期 $100.00 (+24.44%)
- 確定: 2749件 (Win 815 / Loss 1053 / Flat 881) / pending 3件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000312 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STONK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $124.44

## 6. Latest Market Context

- 更新: 2026-09-11T21:36:14.572998+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77318.3
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +37.59% | $12,505,919.74 |
| LAB/USDT:USDT | +21.59% | $9,881,857.72 |
| BEAT/USDT:USDT | +17.57% | $10,681,868.04 |
| LSK/USDT:USDT | +12.41% | $2,913,086.52 |
| STONK/USDT:USDT | +6.62% | $1,473,930.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_1h_threshold | +4.14% | +4.12% |
| LSK/USDT:USDT | below_1h_threshold | +3.07% | +3.05% |
| UAI/USDT:USDT | below_1h_threshold | +2.23% | +2.20% |
| ALGO/USDT:USDT | below_1h_threshold | +0.83% | +0.80% |
| RUNE/USDT:USDT | below_1h_threshold | +0.65% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
