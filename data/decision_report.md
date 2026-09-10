# Decision Report

- generated_at: 2026-09-10T02:01:07.857484+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14141**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=14141, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.98% | **+1.19%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.49% | **+0.46%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.82% | **+0.41%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +2.97% | **+2.53%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.16% | **+1.94%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.46% | **+1.02%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.49% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,027.36** / 初期 $100.00 (+927.36%)
- 確定: 5321件 (Win 1599 / Loss 1717 / Flat 2005) / skip 5381件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,027.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$203.24** / 初期 $100.00 (+103.24%)
- 確定: 2735件 (Win 755 / Loss 641 / Flat 1339) / skip 4817件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0639 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $203.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.89** / 初期 $100.00 (+20.89%)
- 確定: 2646件 (Win 779 / Loss 1011 / Flat 856) / pending 4件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000506 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $120.89

## 6. Latest Market Context

- 更新: 2026-09-10T02:01:00.618317+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78031.3
- Funnel: target 1064 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +53.00% | $1,329,472.80 |
| BTR/USDT:USDT | +14.85% | $2,255,465.91 |
| CATE/USDT:USDT | +11.98% | $2,780,876.85 |
| KAS/USDT:USDT | +3.00% | $4,035,223.32 |
| EGLD/USDT:USDT | +2.44% | $2,416,074.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MINA/USDT:USDT | below_1h_threshold | +0.81% | +0.85% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.71% | +0.75% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.73% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.54% | +0.57% |
| BTR/USDT:USDT | below_1h_threshold | +0.51% | +0.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
