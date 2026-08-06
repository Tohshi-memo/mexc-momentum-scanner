# Decision Report

- generated_at: 2026-08-06T03:21:36.681093+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10494**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.14% / filled 20/20。**
- 全期間 MARKET基準: n=10494, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.14% | **+2.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.40% | **+1.19%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.97% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.36% | **-0.13%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.54% | **-0.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3771件 (Win 1195 / Loss 1236 / Flat 1340) / skip 3284件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.64** / 初期 $100.00 (+40.64%)
- 確定: 1356件 (Win 379 / Loss 319 / Flat 658) / skip 2549件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $140.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 823件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T03:21:26.427118+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64507.1
- Funnel: target 949 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +44.10% | $43,058,504.10 |
| DODO/USDT:USDT | +41.53% | $7,059,623.84 |
| BLESS/USDT:USDT | +33.43% | $113,372,467.76 |
| BICO/USDT:USDT | +29.75% | $11,354,446.23 |
| ESPORTS/USDT:USDT | +27.28% | $7,074,748.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +4.08% | +4.14% |
| BICO/USDT:USDT | below_1h_threshold | +3.99% | +4.06% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.41% | +3.48% |
| HFT/USDT:USDT | below_1h_threshold | +2.39% | +2.46% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.32% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
