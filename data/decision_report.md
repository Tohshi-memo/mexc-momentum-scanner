# Decision Report

- generated_at: 2026-09-09T18:21:35.989372+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14101**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14101, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.86% | **-1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +7.36% | **+1.47%** |
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.62% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.16% | **+2.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.68% | **+1.88%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +6.14% | **+1.84%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +5.97% | **+1.49%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5349件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$191.83** / 初期 $100.00 (+91.83%)
- 確定: 2695件 (Win 740 / Loss 631 / Flat 1324) / skip 4817件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0480 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $191.83

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.84** / 初期 $100.00 (+17.84%)
- 確定: 2620件 (Win 765 / Loss 1001 / Flat 854) / pending 1件 / skip 2959件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000412 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account -0.09% 残高後 $117.84

## 6. Latest Market Context

- 更新: 2026-09-09T18:21:22.387381+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=78562.7
- Funnel: target 1064 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.8 >= 65=1, 4h RSI 87.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOCK/USDT:USDT | +19.17% | $1,534,379.85 |
| IOST/USDT:USDT | +19.04% | $21,720,659.33 |
| BULLA/USDT:USDT | +14.99% | $3,059,717.10 |
| OL/USDT:USDT | +8.59% | $2,700,544.29 |
| BTR/USDT:USDT | +7.17% | $1,030,357.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_1h_threshold | +4.39% | +4.61% |
| WAVES/USDT:USDT | below_1h_threshold | +2.88% | +3.11% |
| BTR/USDT:USDT | below_1h_threshold | +2.38% | +2.61% |
| RAY/USDT:USDT | below_1h_threshold | +2.31% | +2.54% |
| PHA/USDT:USDT | below_1h_threshold | +2.18% | +2.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
