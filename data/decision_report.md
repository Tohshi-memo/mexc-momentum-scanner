# Decision Report

- generated_at: 2026-08-06T09:56:53.478403+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10563**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10563, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.47% | **+0.33%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.44** / 初期 $100.00 (+505.44%)
- 確定: 3792件 (Win 1203 / Loss 1246 / Flat 1343) / skip 3332件
- 成長率目線: 平均log +0.000475 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.80** / 初期 $100.00 (+40.80%)
- 確定: 1398件 (Win 389 / Loss 331 / Flat 678) / skip 2576件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0818 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $140.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000196 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T09:56:36.446512+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=64646.1
- Funnel: target 955 → liquid 189 → pre 50 → checked 50 → surge 8 → strict 2
- Surge前reject: below_1h_threshold=42, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1, 4h RSI 80.7 >= 65=1, 4h RSI 84.8 >= 65=1, 4h RSI 74.9 >= 65=1, 4h RSI 73.9 >= 65=1, 4h RSI 78.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +79.42% | $66,619,439.00 |
| CTSI/USDT:USDT | +48.97% | $1,083,589.69 |
| BLESS/USDT:USDT | +47.36% | $124,106,553.75 |
| CASHCAT/USDT:USDT | +44.59% | $1,366,852.12 |
| DODO/USDT:USDT | +41.59% | $10,144,611.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.82% | +5.23% |
| QBTSSTOCK/USDT:USDT | below_1h_threshold | +4.57% | +4.99% |
| SYN/USDT:USDT | below_1h_threshold | +3.95% | +4.37% |
| ROBO/USDT:USDT | below_1h_threshold | +2.25% | +2.66% |
| ZINC/USDT:USDT | below_1h_threshold | +1.65% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
