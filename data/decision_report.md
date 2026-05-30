# Decision Report

- generated_at: 2026-05-30T15:20:06.365745+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5136**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=5136, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.76% | **+1.68%** |
| LIMIT_BB3S | 8/17 | 47.1% | +3.10% | **+1.46%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.82% | **+1.27%** |
| ASK | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.79% | **+3.20%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.12% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 76件 (TP 22 / SL 51 / EXP 3)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 791件 (Win 183 / Loss 242 / Flat 366) / skip 906件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +6.10%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.16% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-30T15:20:04.158974+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=73904.2
- Funnel: target 773 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +48.50% | $4,205,462.35 |
| LAB/USDT:USDT | +36.19% | $145,675,396.00 |
| H/USDT:USDT | +33.09% | $7,716,035.30 |
| STG/USDT:USDT | +26.80% | $2,569,121.09 |
| NFP/USDT:USDT | +25.75% | $3,779,428.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.95% | +3.95% |
| HEI/USDT:USDT | below_1h_threshold | +3.47% | +3.46% |
| WLD/USDT:USDT | below_1h_threshold | +2.85% | +2.84% |
| XLM/USDT:USDT | below_1h_threshold | +1.06% | +1.06% |
| GRASS/USDT:USDT | below_1h_threshold | +0.82% | +0.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
