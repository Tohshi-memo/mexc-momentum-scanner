# Decision Report

- generated_at: 2026-09-04T05:01:37.619918+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13582**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=13582, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.25% | **+0.88%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_BB3S | 2/18 | 11.1% | +5.22% | **+0.58%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.66% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.47% | **-0.21%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.35% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5134件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.64** / 初期 $100.00 (+85.64%)
- 確定: 2398件 (Win 679 / Loss 576 / Flat 1143) / skip 4595件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0487 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.55** / 初期 $100.00 (+16.55%)
- 確定: 2235件 (Win 665 / Loss 875 / Flat 695) / pending 5件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000141 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.55

## 6. Latest Market Context

- 更新: 2026-09-04T05:01:26.427379+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=80955.9
- Funnel: target 1046 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +24.25% | $11,813,941.01 |
| TRIA/USDT:USDT | +20.44% | $2,552,037.98 |
| USELESS/USDT:USDT | +18.40% | $29,961,586.28 |
| BASECAT/USDT:USDT | +17.29% | $2,141,130.52 |
| BTR/USDT:USDT | +15.99% | $9,052,407.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +4.90% | +5.00% |
| ZEST/USDT:USDT | below_1h_threshold | +2.01% | +2.11% |
| TRIA/USDT:USDT | below_1h_threshold | +1.60% | +1.70% |
| KORU/USDT:USDT | below_1h_threshold | +1.56% | +1.66% |
| MUU/USDT:USDT | below_1h_threshold | +1.49% | +1.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
