# Decision Report

- generated_at: 2026-09-04T04:11:30.435861+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13578**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.53% / filled 20/20。**
- 全期間 MARKET基準: n=13578, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.91% | **+1.24%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.20% | **+1.08%** |
| LIMIT_BB3S | 3/18 | 16.7% | +6.15% | **+1.02%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.31% | **+0.85%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -1.08% | **-0.43%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.57% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5130件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.51** / 初期 $100.00 (+85.51%)
- 確定: 2394件 (Win 678 / Loss 576 / Flat 1140) / skip 4595件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0774 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRIA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.51** / 初期 $100.00 (+16.51%)
- 確定: 2233件 (Win 664 / Loss 875 / Flat 694) / pending 4件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRIA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.51

## 6. Latest Market Context

- 更新: 2026-09-04T04:11:18.821622+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80836.8
- Funnel: target 1046 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +32.84% | $11,270,952.78 |
| TRIA/USDT:USDT | +28.92% | $1,600,423.18 |
| BASECAT/USDT:USDT | +24.05% | $2,047,130.82 |
| PONS/USDT:USDT | +17.70% | $9,504,361.02 |
| PROM/USDT:USDT | +13.55% | $2,844,696.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +4.93% | +4.90% |
| TRIA/USDT:USDT | below_1h_threshold | +3.85% | +3.81% |
| DASH/USDT:USDT | below_1h_threshold | +2.22% | +2.18% |
| PROM/USDT:USDT | below_1h_threshold | +2.11% | +2.08% |
| BTR/USDT:USDT | below_1h_threshold | +1.72% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
