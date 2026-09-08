# Decision Report

- generated_at: 2026-09-08T15:01:20.869055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14005**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.42% / filled 20/20。**
- 全期間 MARKET基準: n=14005, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.56% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.00% | **+0.30%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.07% | **+0.04%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.12% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.08% | **+0.73%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.73% | **+0.70%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.50% | **+0.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.05% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,007.04** / 初期 $100.00 (+907.04%)
- 確定: 5269件 (Win 1584 / Loss 1707 / Flat 1978) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,007.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.18** / 初期 $100.00 (+90.18%)
- 確定: 2608件 (Win 723 / Loss 622 / Flat 1263) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0386 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VVV/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.14** / 初期 $100.00 (+20.14%)
- 確定: 2594件 (Win 760 / Loss 982 / Flat 852) / pending 2件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000309 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VVV/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $120.14

## 6. Latest Market Context

- 更新: 2026-09-08T15:01:12.742915+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78545.2
- Funnel: target 1070 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +60.62% | $33,677,007.28 |
| VVV/USDT:USDT | +32.79% | $6,182,000.16 |
| USELESS/USDT:USDT | +32.23% | $16,694,844.45 |
| BNCSTOCK/USDT:USDT | +24.60% | $2,393,397.19 |
| AKE/USDT:USDT | +19.49% | $10,532,105.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.43% | +2.41% |
| USELESS/USDT:USDT | below_1h_threshold | +1.49% | +1.47% |
| TESLA/USDT:USDT | below_1h_threshold | +1.32% | +1.29% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.20% | +1.18% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.48% | +0.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
