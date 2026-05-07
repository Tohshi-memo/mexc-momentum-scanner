# Decision Report

- generated_at: 2026-05-07T10:17:42.141842+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3614**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=3614, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.47% | **+1.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_BB3S | 2/13 | 15.4% | +3.09% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.72% | **+0.47%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.86% | **+0.46%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.50% | **+0.25%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.21% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.00** / 初期 $100.00 (+6.00%)
- 確定: 108件 (Win 35 / Loss 44 / Flat 29) / skip 67件
- 成長率目線: 平均log +0.000540 / 幾何平均 +0.054% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $106.00

## 4. Latest Market Context

- 更新: 2026-05-07T10:17:38.417144+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80900.0
- Funnel: target 771 → liquid 182 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +158.78% | $2,130,398.66 |
| B3/USDT:USDT | +109.61% | $11,075,873.20 |
| PENGUIN/USDT:USDT | +100.75% | $3,164,419.44 |
| DOGS/USDT:USDT | +66.29% | $14,804,825.02 |
| SIREN/USDT:USDT | +44.82% | $12,039,054.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.43% | +2.41% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.20% | +2.18% |
| DYDX/USDT:USDT | below_1h_threshold | +1.75% | +1.74% |
| ENA/USDT:USDT | below_1h_threshold | +1.70% | +1.69% |
| VVV/USDT:USDT | below_1h_threshold | +1.52% | +1.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
