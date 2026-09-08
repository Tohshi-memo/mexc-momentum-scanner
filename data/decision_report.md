# Decision Report

- generated_at: 2026-09-08T09:11:23.343197+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13971**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=13971, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.58% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.05% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.25% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.83% | **+0.62%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.95% | **+0.61%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,015.07** / 初期 $100.00 (+915.07%)
- 確定: 5243件 (Win 1582 / Loss 1703 / Flat 1958) / skip 5289件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOFTBANKSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.01% 残高後 $1,015.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.81** / 初期 $100.00 (+88.81%)
- 確定: 2575件 (Win 718 / Loss 619 / Flat 1238) / skip 4807件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0959 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.53** / 初期 $100.00 (+22.53%)
- 確定: 2560件 (Win 753 / Loss 960 / Flat 847) / pending 4件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.53

## 6. Latest Market Context

- 更新: 2026-09-08T09:11:11.160838+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78342.4
- Funnel: target 1065 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +119.70% | $12,102,175.37 |
| BNCSTOCK/USDT:USDT | +50.15% | $1,395,382.70 |
| FORM/USDT:USDT | +39.41% | $3,271,578.42 |
| MEMEROBINHOOD/USDT:USDT | +19.64% | $6,333,542.19 |
| AKE/USDT:USDT | +15.50% | $12,435,989.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FORM/USDT:USDT | below_1h_threshold | +2.62% | +2.69% |
| SOPH/USDT:USDT | below_1h_threshold | +2.55% | +2.62% |
| SOXS/USDT:USDT | below_1h_threshold | +1.93% | +2.00% |
| XPL/USDT:USDT | below_1h_threshold | +1.28% | +1.34% |
| SOLV/USDT:USDT | below_1h_threshold | +0.97% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
