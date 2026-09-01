# Decision Report

- generated_at: 2026-09-01T16:06:24.809267+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13254**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=13254, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.21% | **+1.09%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.97% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.70% | **+0.66%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.31% | **+0.59%** |
| MARKET_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.23% | **+0.43%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.45% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$787.97** / 初期 $100.00 (+687.97%)
- 確定: 4889件 (Win 1487 / Loss 1614 / Flat 1788) / skip 4926件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.22% 残高後 $787.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.47** / 初期 $100.00 (+73.47%)
- 確定: 2233件 (Win 622 / Loss 539 / Flat 1072) / skip 4432件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0271 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.28** / 初期 $100.00 (+15.28%)
- 確定: 2087件 (Win 610 / Loss 815 / Flat 662) / pending 0件 / skip 2637件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.28

## 6. Latest Market Context

- 更新: 2026-09-01T16:06:13.567453+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77934.9
- Funnel: target 1036 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +4.53% | $1,605,759.19 |
| PROM/USDT:USDT | +3.72% | $4,708,048.39 |
| MARSCOIN/USDT:USDT | +2.42% | $3,444,298.85 |
| SKYAI/USDT:USDT | +2.19% | $2,079,061.17 |
| TRIA/USDT:USDT | +1.71% | $1,562,496.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +4.54% | +4.47% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.57% | +3.49% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.42% | +2.35% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.20% | +2.12% |
| TRIA/USDT:USDT | below_1h_threshold | +1.72% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
