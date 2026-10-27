# Decision Report

- generated_at: 2026-10-27T13:36:21.916779+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17600**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17600, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_9PCT | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_BB3S | 4/17 | 23.5% | +2.52% | **+0.59%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.22% | **+1.66%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.86** / 初期 $100.00 (+21.86%)
- 確定トレード: 253件 (TP 94 / SL 151 / EXP 8)
- 最新: MRNASTOCK/USDT:USDT TP_HIT PnL +6.21% 残高後 $121.86
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6723件 (Win 1956 / Loss 2152 / Flat 2615) / skip 7438件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$336.27** / 初期 $100.00 (+236.27%)
- 確定: 4129件 (Win 1131 / Loss 960 / Flat 2038) / skip 6882件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1451 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_8PCT` TP_HIT account +0.69% 残高後 $336.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5762件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000354 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T13:36:12.525993+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=80209.5
- Funnel: target 1083 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +193.90% | $9,144,456.27 |
| TAG/USDT:USDT | +25.10% | $2,852,316.26 |
| BTW/USDT:USDT | +22.33% | $21,898,307.67 |
| Q/USDT:USDT | +17.12% | $55,874,244.92 |
| BEAT/USDT:USDT | +15.78% | $10,446,761.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +3.67% | +3.83% |
| JCT/USDT:USDT | below_1h_threshold | +3.24% | +3.40% |
| ARIA/USDT:USDT | below_1h_threshold | +2.93% | +3.09% |
| DNA/USDT:USDT | below_1h_threshold | +2.64% | +2.79% |
| BR/USDT:USDT | below_1h_threshold | +2.26% | +2.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
