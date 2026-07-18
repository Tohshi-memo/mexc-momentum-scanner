# Decision Report

- generated_at: 2026-07-18T00:01:09.985594+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8898**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=8898, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_BB3S | 4/20 | 20.0% | +5.78% | **+1.16%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.71%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.16% | **+0.70%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.40% | **+0.24%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$365.74** / 初期 $100.00 (+265.74%)
- 確定: 3013件 (Win 937 / Loss 958 / Flat 1118) / skip 2446件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $365.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$112.09** / 初期 $100.00 (+12.09%)
- 確定: 860件 (Win 203 / Loss 174 / Flat 483) / skip 1449件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $112.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.58** / 初期 $100.00 (-0.42%)
- 確定: 157件 (Win 50 / Loss 84 / Flat 23) / pending 4件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.58

## 6. Latest Market Context

- 更新: 2026-07-18T00:01:04.023772+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63922.5
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +47.07% | $9,885,189.25 |
| CASHCAT/USDT:USDT | +21.69% | $1,183,747.73 |
| AKE/USDT:USDT | +16.69% | $48,413,903.22 |
| CRO/USDT:USDT | +7.78% | $2,156,419.15 |
| XEC/USDT:USDT | +7.51% | $3,397,200.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +1.14% | +1.11% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.06% | +1.04% |
| APT/USDT:USDT | below_1h_threshold | +0.50% | +0.47% |
| RAVE/USDT:USDT | below_1h_threshold | +0.43% | +0.40% |
| AKE/USDT:USDT | below_1h_threshold | +0.40% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
