# Decision Report

- generated_at: 2026-09-20T03:56:33.579600+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15134**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=15134, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +2.82% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.21% | **+0.84%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.78% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,196.37** / 初期 $100.00 (+1096.37%)
- 確定: 5662件 (Win 1699 / Loss 1834 / Flat 2129) / skip 6033件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $1,196.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.48** / 初期 $100.00 (+147.48%)
- 確定: 3247件 (Win 901 / Loss 762 / Flat 1584) / skip 5298件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0604 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $247.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3631件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000214 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T03:56:19.416242+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=80479.2
- Funnel: target 1050 → liquid 141 → pre 50 → checked 50 → surge 6 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1, 4h RSI 80.9 >= 65=1, 4h RSI 84.7 >= 65=1, 4h RSI 81.7 >= 65=1, 4h RSI 67.3 >= 65=1, 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +71.51% | $3,302,056.50 |
| ONE/USDT:USDT | +34.30% | $48,133,226.79 |
| OFC/USDT:USDT | +33.73% | $2,269,863.60 |
| G/USDT:USDT | +26.34% | $11,728,444.94 |
| ZIL/USDT:USDT | +19.01% | $2,603,396.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STX/USDT:USDT | below_1h_threshold | +4.25% | +4.04% |
| SAGA/USDT:USDT | below_1h_threshold | +4.24% | +4.03% |
| OP/USDT:USDT | below_1h_threshold | +4.17% | +3.96% |
| SAND/USDT:USDT | below_1h_threshold | +3.31% | +3.10% |
| JTO/USDT:USDT | below_1h_threshold | +2.88% | +2.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
