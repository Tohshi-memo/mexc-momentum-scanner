# Decision Report

- generated_at: 2026-09-17T13:36:32.520016+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14799**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.88% / filled 20/20。**
- 全期間 MARKET基準: n=14799, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.53% | **+2.41%** |
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.16% | **+0.64%** |
| LIMIT_BB3S | 2/17 | 11.8% | +2.00% | **+0.24%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.10% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5602件 (Win 1679 / Loss 1814 / Flat 2109) / skip 5758件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.89** / 初期 $100.00 (+139.89%)
- 確定: 3130件 (Win 870 / Loss 747 / Flat 1513) / skip 5080件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2958件 (Win 878 / Loss 1165 / Flat 915) / pending 0件 / skip 3317件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T13:36:20.691400+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.61% price=76233.1
- Funnel: target 1050 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AVA/USDT:USDT | +88.67% | $3,531,329.11 |
| ONE/USDT:USDT | +58.08% | $11,911,061.83 |
| BATON/USDT:USDT | +35.51% | $2,573,082.62 |
| 4STOCK/USDT:USDT | +28.12% | $1,100,767.04 |
| GENIUS/USDT:USDT | +28.03% | $1,823,845.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +3.63% | +4.24% |
| MVLL/USDT:USDT | below_1h_threshold | +2.70% | +3.31% |
| SNXX/USDT:USDT | below_1h_threshold | +2.48% | +3.09% |
| PONS/USDT:USDT | below_1h_threshold | +2.29% | +2.90% |
| MUU/USDT:USDT | below_1h_threshold | +1.67% | +2.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
