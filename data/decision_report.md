# Decision Report

- generated_at: 2026-09-08T09:06:59.458769+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13970**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=13970, expectancy=-0.01%
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
| LIMIT_1PCT | 18/20 | 90.0% | +0.05% | **+0.05%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.53% | **+0.42%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.59% | **+0.41%** |
| MARKET_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,015.07** / 初期 $100.00 (+915.07%)
- 確定: 5243件 (Win 1582 / Loss 1703 / Flat 1958) / skip 5288件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOFTBANKSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.01% 残高後 $1,015.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.81** / 初期 $100.00 (+88.81%)
- 確定: 2574件 (Win 718 / Loss 619 / Flat 1237) / skip 4807件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0971 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $188.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.53** / 初期 $100.00 (+22.53%)
- 確定: 2559件 (Win 753 / Loss 960 / Flat 846) / pending 4件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000234 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOFTBANKSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.53

## 6. Latest Market Context

- 更新: 2026-09-08T09:06:47.378467+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78408.9
- Funnel: target 1065 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +119.99% | $11,990,493.54 |
| BNCSTOCK/USDT:USDT | +51.15% | $1,379,079.90 |
| FORM/USDT:USDT | +39.69% | $3,237,088.16 |
| MEMEROBINHOOD/USDT:USDT | +20.59% | $6,329,037.00 |
| AKE/USDT:USDT | +14.71% | $12,424,080.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOPH/USDT:USDT | below_1h_threshold | +2.91% | +2.89% |
| FORM/USDT:USDT | below_1h_threshold | +2.73% | +2.72% |
| SOXS/USDT:USDT | below_1h_threshold | +1.93% | +1.91% |
| HNT/USDT:USDT | below_1h_threshold | +0.74% | +0.73% |
| UAI/USDT:USDT | below_1h_threshold | +0.73% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
