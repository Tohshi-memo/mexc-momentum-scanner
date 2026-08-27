# Decision Report

- generated_at: 2026-08-27T05:06:37.049363+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12778**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.13% / filled 20/20。**
- 全期間 MARKET基準: n=12778, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_4PCT | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.81% | **+0.72%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.74% | **+0.59%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | -0.11% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$723.24** / 初期 $100.00 (+623.24%)
- 確定: 4665件 (Win 1414 / Loss 1530 / Flat 1721) / skip 4674件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $723.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2002件 (Win 544 / Loss 483 / Flat 975) / skip 4187件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0724 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1984件 (Win 580 / Loss 758 / Flat 646) / pending 0件 / skip 2266件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000177 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-27T05:06:24.107620+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=78643.7
- Funnel: target 1023 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +30.47% | $12,802,954.65 |
| BTR/USDT:USDT | +25.11% | $29,145,245.30 |
| MOVR/USDT:USDT | +24.90% | $1,950,773.80 |
| BICO/USDT:USDT | +21.96% | $22,157,384.18 |
| RUNE/USDT:USDT | +21.54% | $1,251,088.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +3.50% | +3.63% |
| TUT/USDT:USDT | below_1h_threshold | +1.87% | +2.00% |
| RUNE/USDT:USDT | below_1h_threshold | +1.01% | +1.14% |
| GRASS/USDT:USDT | below_1h_threshold | +0.57% | +0.70% |
| BLESS/USDT:USDT | below_1h_threshold | +0.46% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
