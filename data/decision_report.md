# Decision Report

- generated_at: 2026-09-10T00:21:20.662587+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14134**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.36% / filled 20/20。**
- 全期間 MARKET基準: n=14134, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.36% | **+2.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.36% | **+2.36%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.60% | **+2.34%** |
| LIMIT_ATR | 12/20 | 60.0% | +3.14% | **+1.88%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.65% | **+1.86%** |
| LIMIT_5PCT | 5/20 | 25.0% | +3.77% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.45% | **+0.36%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.27% | **+0.26%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.57% | **+0.23%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,001.87** / 初期 $100.00 (+901.87%)
- 確定: 5314件 (Win 1595 / Loss 1715 / Flat 2004) / skip 5381件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,001.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$199.80** / 初期 $100.00 (+99.80%)
- 確定: 2728件 (Win 751 / Loss 639 / Flat 1338) / skip 4817件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0680 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $199.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.86** / 初期 $100.00 (+19.86%)
- 確定: 2639件 (Win 775 / Loss 1009 / Flat 855) / pending 3件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000446 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $119.86

## 6. Latest Market Context

- 更新: 2026-09-10T00:21:09.705864+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78210.0
- Funnel: target 1064 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +14.42% | $2,088,206.29 |
| CATE/USDT:USDT | +10.69% | $2,809,817.52 |
| WAVES/USDT:USDT | +9.57% | $1,215,156.47 |
| SOCK/USDT:USDT | +5.02% | $1,127,333.89 |
| MINA/USDT:USDT | +4.41% | $1,212,572.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +1.35% | +1.42% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.85% | +0.92% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.71% | +0.78% |
| BTR/USDT:USDT | below_1h_threshold | +0.51% | +0.58% |
| MUU/USDT:USDT | below_1h_threshold | +0.46% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
