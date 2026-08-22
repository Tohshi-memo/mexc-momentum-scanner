# Decision Report

- generated_at: 2026-08-22T01:26:15.574815+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12284**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12284, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.80% | **+1.68%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.88% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.30% | **+3.01%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.51% | **+2.81%** |
| MARKET_LONG | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.39% | **+1.69%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +3.50% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$681.31** / 初期 $100.00 (+581.31%)
- 確定: 4403件 (Win 1347 / Loss 1440 / Flat 1616) / skip 4442件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ENS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $681.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.32** / 初期 $100.00 (+55.32%)
- 確定: 1890件 (Win 521 / Loss 451 / Flat 918) / skip 3805件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1766 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ENS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $155.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.77** / 初期 $100.00 (+17.77%)
- 確定: 1834件 (Win 544 / Loss 694 / Flat 596) / pending 5件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000361 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ENS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $117.77

## 6. Latest Market Context

- 更新: 2026-08-22T01:26:06.428528+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=78019.0
- Funnel: target 1018 → liquid 216 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +261.64% | $3,547,678.44 |
| CATE/USDT:USDT | +63.76% | $12,028,062.01 |
| AGI/USDT:USDT | +23.44% | $1,713,871.56 |
| JIMOTHY/USDT:USDT | +19.64% | $1,654,109.46 |
| ETC/USDT:USDT | +19.29% | $9,561,411.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.43% | +4.30% |
| PYTH/USDT:USDT | below_1h_threshold | +2.67% | +2.54% |
| XLM/USDT:USDT | below_1h_threshold | +2.06% | +1.93% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.98% | +1.85% |
| ETC/USDT:USDT | below_1h_threshold | +1.64% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
