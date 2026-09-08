# Decision Report

- generated_at: 2026-09-08T09:01:21.113627+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13969**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=13969, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.20% | **+0.06%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.84% | **+0.67%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,014.95** / 初期 $100.00 (+914.95%)
- 確定: 5242件 (Win 1581 / Loss 1703 / Flat 1958) / skip 5288件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FORM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,014.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.81** / 初期 $100.00 (+88.81%)
- 確定: 2574件 (Win 718 / Loss 619 / Flat 1237) / skip 4806件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1059 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $188.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.53** / 初期 $100.00 (+22.53%)
- 確定: 2558件 (Win 753 / Loss 960 / Flat 845) / pending 5件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000269 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.53

## 6. Latest Market Context

- 更新: 2026-09-08T09:01:10.695699+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78354.9
- Funnel: target 1065 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +114.81% | $11,737,476.89 |
| BNCSTOCK/USDT:USDT | +46.29% | $1,364,782.03 |
| FORM/USDT:USDT | +36.82% | $3,195,205.38 |
| MEMEROBINHOOD/USDT:USDT | +19.40% | $6,326,255.73 |
| AKE/USDT:USDT | +15.28% | $12,384,856.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.93% | +1.98% |
| HNT/USDT:USDT | below_1h_threshold | +0.95% | +1.00% |
| VVV/USDT:USDT | below_1h_threshold | +0.35% | +0.40% |
| BONER/USDT:USDT | below_1h_threshold | +0.32% | +0.37% |
| W/USDT:USDT | below_1h_threshold | +0.26% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
