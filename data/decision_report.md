# Decision Report

- generated_at: 2026-09-10T06:06:20.887855+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14154**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14154, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.85% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.25% | **+2.44%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.53% | **+2.27%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,064.33** / 初期 $100.00 (+964.33%)
- 確定: 5334件 (Win 1605 / Loss 1720 / Flat 2009) / skip 5381件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,064.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.19** / 初期 $100.00 (+108.19%)
- 確定: 2748件 (Win 761 / Loss 644 / Flat 1343) / skip 4817件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0971 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $208.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.35** / 初期 $100.00 (+22.35%)
- 確定: 2659件 (Win 785 / Loss 1014 / Flat 860) / pending 1件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000435 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.35

## 6. Latest Market Context

- 更新: 2026-09-10T06:06:10.638376+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=78396.0
- Funnel: target 1064 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +42.28% | $3,334,814.14 |
| CATE/USDT:USDT | +21.59% | $2,746,879.73 |
| BULLA/USDT:USDT | +9.68% | $4,006,795.30 |
| VET/USDT:USDT | +5.75% | $5,644,258.98 |
| KAS/USDT:USDT | +4.85% | $4,347,415.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +2.17% | +2.31% |
| CATE/USDT:USDT | below_1h_threshold | +1.75% | +1.89% |
| BULLA/USDT:USDT | below_1h_threshold | +0.92% | +1.06% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +0.24% | +0.38% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.18% | +0.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
