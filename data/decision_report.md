# Decision Report

- generated_at: 2026-07-17T21:26:17.954649+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8887**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.37% / filled 20/20。**
- 全期間 MARKET基準: n=8887, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/19 | 21.1% | +3.74% | **+0.79%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.08% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.58% | **+0.35%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.21% | **+0.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.12% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$363.87** / 初期 $100.00 (+263.87%)
- 確定: 3002件 (Win 934 / Loss 954 / Flat 1114) / skip 2446件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $363.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.54** / 初期 $100.00 (+11.54%)
- 確定: 849件 (Win 201 / Loss 173 / Flat 475) / skip 1449件
- 成長率目線: 平均log +0.000129 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0853 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $111.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.42** / 初期 $100.00 (-0.58%)
- 確定: 147件 (Win 47 / Loss 80 / Flat 20) / pending 2件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000319 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.42

## 6. Latest Market Context

- 更新: 2026-07-17T21:26:11.418532+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64132.8
- Funnel: target 885 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +30.82% | $44,342,695.14 |
| ESPORTS/USDT:USDT | +25.10% | $9,258,417.19 |
| XEC/USDT:USDT | +8.56% | $3,185,406.03 |
| VVV/USDT:USDT | +6.34% | $2,481,470.59 |
| CRO/USDT:USDT | +5.57% | $2,266,312.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EGLD/USDT:USDT | below_1h_threshold | +2.67% | +2.60% |
| SLX/USDT:USDT | below_1h_threshold | +1.69% | +1.62% |
| ORDI/USDT:USDT | below_1h_threshold | +1.07% | +0.99% |
| US/USDT:USDT | below_1h_threshold | +1.05% | +0.98% |
| DODO/USDT:USDT | below_1h_threshold | +0.84% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
