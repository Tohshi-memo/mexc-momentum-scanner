# Decision Report

- generated_at: 2026-08-06T04:06:20.133891+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10499**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=10499, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.19% | **+0.77%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.00% | **+0.70%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.68% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.47% | **+0.88%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.57% | **+0.71%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.38%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3771件 (Win 1195 / Loss 1236 / Flat 1340) / skip 3289件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.15** / 初期 $100.00 (+40.15%)
- 確定: 1357件 (Win 379 / Loss 320 / Flat 658) / skip 2553件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 829件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T04:06:12.500615+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64500.5
- Funnel: target 949 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +68.74% | $43,032,614.76 |
| BLESS/USDT:USDT | +35.31% | $114,634,391.78 |
| DODO/USDT:USDT | +34.28% | $7,479,473.34 |
| ESPORTS/USDT:USDT | +32.21% | $7,165,583.54 |
| BICO/USDT:USDT | +30.57% | $11,473,525.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +2.82% | +2.82% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.58% | +1.57% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.30% | +1.30% |
| ALLO/USDT:USDT | below_1h_threshold | +0.73% | +0.72% |
| MMT/USDT:USDT | below_1h_threshold | +0.44% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
