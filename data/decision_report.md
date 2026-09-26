# Decision Report

- generated_at: 2026-09-26T07:21:13.211351+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15583**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15583, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.30% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.34% | **+2.22%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.28% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,252.82** / 初期 $100.00 (+1152.82%)
- 確定: 5944件 (Win 1755 / Loss 1906 / Flat 2283) / skip 6200件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PAID/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,252.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$264.00** / 初期 $100.00 (+164.00%)
- 確定: 3513件 (Win 967 / Loss 801 / Flat 1745) / skip 5481件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0999 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PAID/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $264.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3186件 (Win 937 / Loss 1262 / Flat 987) / pending 0件 / skip 3866件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000390 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T07:21:02.476313+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=83981.4
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +365.05% | $1,454,600.39 |
| RARE/USDT:USDT | +36.37% | $2,691,732.79 |
| BATON/USDT:USDT | +29.11% | $1,579,955.40 |
| ARK/USDT:USDT | +21.98% | $3,813,003.87 |
| BR/USDT:USDT | +14.59% | $10,103,789.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PAID/USDT:USDT | below_1h_threshold | +4.24% | +4.09% |
| ZRO/USDT:USDT | below_1h_threshold | +2.79% | +2.64% |
| RARE/USDT:USDT | below_1h_threshold | +1.89% | +1.74% |
| ONE/USDT:USDT | below_1h_threshold | +1.67% | +1.53% |
| CC/USDT:USDT | below_1h_threshold | +1.37% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
