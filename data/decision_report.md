# Decision Report

- generated_at: 2026-09-25T22:46:29.595852+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15546**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15546, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.12% | **-1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.42% | **+0.27%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.09% | **+0.09%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.45% | **-0.09%** |
| LIMIT_BB3S | 5/14 | 35.7% | -0.44% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.33% | **+1.63%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.33% | **+1.50%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +5.73% | **+1.15%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.69% | **+1.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,198.50** / 初期 $100.00 (+1098.50%)
- 確定: 5910件 (Win 1743 / Loss 1895 / Flat 2272) / skip 6197件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,198.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.50** / 初期 $100.00 (+156.50%)
- 確定: 3479件 (Win 953 / Loss 793 / Flat 1733) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0317 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.59** / 初期 $100.00 (+19.59%)
- 確定: 3176件 (Win 934 / Loss 1258 / Flat 984) / pending 5件 / skip 3839件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000244 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.59

## 6. Latest Market Context

- 更新: 2026-09-25T22:46:15.564025+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=84037.8
- Funnel: target 1067 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +27.76% | $1,084,826.28 |
| PHA/USDT:USDT | +25.78% | $22,221,940.24 |
| BR/USDT:USDT | +16.90% | $9,262,248.46 |
| ARK/USDT:USDT | +11.60% | $2,723,827.68 |
| SEI/USDT:USDT | +11.35% | $33,527,008.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +4.64% | +4.29% |
| PENGU/USDT:USDT | below_1h_threshold | +3.36% | +3.01% |
| LTC/USDT:USDT | below_1h_threshold | +3.29% | +2.94% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.17% | +2.82% |
| JUP/USDT:USDT | below_1h_threshold | +3.05% | +2.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
