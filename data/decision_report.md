# Decision Report

- generated_at: 2026-09-17T22:21:16.372743+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14846**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14846, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.96% | **-0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +2.57% | **+1.28%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.71% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.28% | **+2.46%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.09% | **+2.16%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.94% | **+1.55%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.47% | **+1.39%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.31% | **+1.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5603件 (Win 1679 / Loss 1814 / Flat 2110) / skip 5804件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.08** / 初期 $100.00 (+143.08%)
- 確定: 3140件 (Win 874 / Loss 748 / Flat 1518) / skip 5117件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1092 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $243.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2958件 (Win 878 / Loss 1165 / Flat 915) / pending 0件 / skip 3362件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000397 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T22:21:05.943390+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=76217.6
- Funnel: target 1052 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +46.43% | $37,092,702.01 |
| CNPY/USDT:USDT | +46.07% | $2,919,162.92 |
| COTI/USDT:USDT | +26.53% | $4,718,495.60 |
| CROSS/USDT:USDT | +19.54% | $1,345,225.72 |
| PIEVERSE/USDT:USDT | +6.82% | $1,493,528.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.33% | +3.54% |
| COTI/USDT:USDT | below_1h_threshold | +1.33% | +1.54% |
| SAGA/USDT:USDT | below_1h_threshold | +1.11% | +1.32% |
| MERL/USDT:USDT | below_1h_threshold | +0.53% | +0.74% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +0.45% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
