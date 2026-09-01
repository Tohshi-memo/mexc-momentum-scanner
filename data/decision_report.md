# Decision Report

- generated_at: 2026-09-01T01:01:27.765496+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13215**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.56% / filled 20/20。**
- 全期間 MARKET基準: n=13215, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.01% | **+0.96%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.11% | **+1.44%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.70% | **+0.60%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.98% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 195件 (TP 73 / SL 117 / EXP 5)
- 最新: ARB/USDT:USDT SL_HIT PnL -2.46% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4878件 (Win 1485 / Loss 1609 / Flat 1784) / skip 4898件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.13** / 初期 $100.00 (+74.13%)
- 確定: 2197件 (Win 609 / Loss 529 / Flat 1059) / skip 4429件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0551 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DASH/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $174.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 0件 / skip 2605件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000126 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-09-01T01:01:16.496088+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=78695.7
- Funnel: target 1031 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +33.18% | $37,467,263.02 |
| BTR/USDT:USDT | +23.47% | $6,367,308.66 |
| USELESS/USDT:USDT | +22.35% | $16,802,022.20 |
| 0G/USDT:USDT | +17.39% | $20,400,152.20 |
| OP/USDT:USDT | +12.93% | $5,627,565.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHEINSTOCK/USDT:USDT | below_1h_threshold | +4.48% | +4.38% |
| KORU/USDT:USDT | below_1h_threshold | +2.15% | +2.05% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.39% | +1.29% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +0.95% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.91% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
