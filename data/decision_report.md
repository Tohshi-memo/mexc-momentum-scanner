# Decision Report

- generated_at: 2026-09-03T19:41:44.156406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13531**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=13531, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.31% | **+0.85%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.94% | **+0.85%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.11% | **+0.83%** |
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.07% | **+0.53%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +1.07% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5084件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4569件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.46** / 初期 $100.00 (+17.46%)
- 確定: 2204件 (Win 659 / Loss 863 / Flat 682) / pending 6件 / skip 2798件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000452 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $117.46

## 6. Latest Market Context

- 更新: 2026-09-03T19:41:29.750350+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=81556.8
- Funnel: target 1046 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +25.00% | $65,146,061.02 |
| HNT/USDT:USDT | +22.00% | $3,790,754.43 |
| APR/USDT:USDT | +11.05% | $2,184,357.12 |
| PROM/USDT:USDT | +10.34% | $3,726,495.75 |
| CASHCAT/USDT:USDT | +6.64% | $1,004,021.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BONER/USDT:USDT | below_relative_strength | +5.02% | +4.61% |
| CASHCAT/USDT:USDT | below_relative_strength | +5.01% | +4.60% |
| AKE/USDT:USDT | below_1h_threshold | +4.91% | +4.50% |
| BR/USDT:USDT | below_1h_threshold | +2.51% | +2.10% |
| MUU/USDT:USDT | below_1h_threshold | +2.14% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
