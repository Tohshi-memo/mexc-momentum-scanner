# Decision Report

- generated_at: 2026-09-03T17:46:36.271796+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13521**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.05% / filled 20/20。**
- 全期間 MARKET基準: n=13521, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.12% | **+0.95%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.17% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.05% | **+0.58%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.86% | **+0.47%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.79% | **+0.40%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.42% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5074件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4559件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.46** / 初期 $100.00 (+16.46%)
- 確定: 2198件 (Win 655 / Loss 861 / Flat 682) / pending 4件 / skip 2792件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000390 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.46

## 6. Latest Market Context

- 更新: 2026-09-03T17:46:24.024456+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=81038.0
- Funnel: target 1046 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1, 4h RSI 78.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +15.62% | $68,096,244.36 |
| PROM/USDT:USDT | +11.07% | $3,812,027.58 |
| MUBARAK/USDT:USDT | +5.99% | $3,650,305.06 |
| BR/USDT:USDT | +5.55% | $8,164,251.34 |
| ENA/USDT:USDT | +4.58% | $42,423,583.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +4.73% | +4.60% |
| 4/USDT:USDT | below_1h_threshold | +4.41% | +4.28% |
| PROM/USDT:USDT | below_1h_threshold | +3.66% | +3.53% |
| JASMY/USDT:USDT | below_1h_threshold | +3.01% | +2.88% |
| ENA/USDT:USDT | below_1h_threshold | +2.78% | +2.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
