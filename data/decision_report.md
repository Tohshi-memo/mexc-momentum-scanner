# Decision Report

- generated_at: 2026-08-08T21:26:18.736544+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10885**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.90% / filled 20/20。**
- 全期間 MARKET基準: n=10885, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.96% | **+1.86%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.14% | **+1.28%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.38% | **+0.96%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.66% | **+0.33%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.50% | **+0.23%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.08% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.53** / 初期 $100.00 (+543.53%)
- 確定: 3886件 (Win 1224 / Loss 1266 / Flat 1396) / skip 3560件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COOKIE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $643.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2785件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0612 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.93** / 初期 $100.00 (+17.93%)
- 確定: 1244件 (Win 389 / Loss 477 / Flat 378) / pending 4件 / skip 1112件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000126 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COOKIE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $117.93

## 6. Latest Market Context

- 更新: 2026-08-08T21:26:10.885606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=65014.0
- Funnel: target 961 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COOKIE/USDT:USDT | +21.25% | $2,125,072.78 |
| LIGHT/USDT:USDT | +13.85% | $1,624,037.08 |
| TUT/USDT:USDT | +13.62% | $17,747,505.87 |
| BLUAI/USDT:USDT | +13.00% | $6,829,252.47 |
| CATI/USDT:USDT | +11.56% | $2,179,171.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAI/USDT:USDT | below_1h_threshold | +3.49% | +3.54% |
| BLUAI/USDT:USDT | below_1h_threshold | +2.47% | +2.53% |
| LIGHT/USDT:USDT | below_1h_threshold | +2.01% | +2.06% |
| ACE/USDT:USDT | below_1h_threshold | +1.67% | +1.72% |
| US/USDT:USDT | below_1h_threshold | +1.26% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
