# Decision Report

- generated_at: 2026-09-01T09:21:22.052446+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13241**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=13241, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.42% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.73% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.22% | **+0.43%** |
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.32% | **+0.23%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.25% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$797.75** / 初期 $100.00 (+697.75%)
- 確定: 4879件 (Win 1486 / Loss 1609 / Flat 1784) / skip 4923件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $797.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.08** / 初期 $100.00 (+74.08%)
- 確定: 2220件 (Win 618 / Loss 537 / Flat 1065) / skip 4432件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0242 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $174.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.28** / 初期 $100.00 (+15.28%)
- 確定: 2087件 (Win 610 / Loss 815 / Flat 662) / pending 0件 / skip 2624件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000301 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.28

## 6. Latest Market Context

- 更新: 2026-09-01T09:21:12.693276+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=77807.3
- Funnel: target 1034 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +23.17% | $21,845,428.66 |
| ARB/USDT:USDT | +22.59% | $74,965,837.92 |
| USELESS/USDT:USDT | +19.44% | $22,362,600.83 |
| CRV/USDT:USDT | +11.99% | $6,213,716.38 |
| AKE/USDT:USDT | +10.86% | $4,818,426.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.20% | +4.26% |
| SOXS/USDT:USDT | below_1h_threshold | +3.20% | +3.26% |
| HEMI/USDT:USDT | below_1h_threshold | +1.68% | +1.74% |
| USOIL/USDT:USDT | below_1h_threshold | +1.20% | +1.25% |
| USELESS/USDT:USDT | below_1h_threshold | +1.18% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
