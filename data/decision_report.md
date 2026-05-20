# Decision Report

- generated_at: 2026-05-20T15:18:44.898633+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4550**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=4550, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.12% | **+1.06%** |
| ASK | 20/20 | 100.0% | +0.67% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.51% | **+0.35%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.27% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.05% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.72** / 初期 $100.00 (+23.72%)
- 確定: 512件 (Win 135 / Loss 175 / Flat 202) / skip 599件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $123.72

## 4. Latest Market Context

- 更新: 2026-05-20T15:18:42.896613+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=77563.9
- Funnel: target 763 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +95.58% | $2,952,274.26 |
| FIDA/USDT:USDT | +53.13% | $6,253,179.36 |
| EDEN/USDT:USDT | +32.38% | $24,006,645.21 |
| LIT/USDT:USDT | +27.30% | $11,036,063.05 |
| BANANAS31/USDT:USDT | +24.03% | $3,323,964.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.33% | +3.15% |
| ZEC/USDT:USDT | below_1h_threshold | +2.59% | +2.40% |
| INJ/USDT:USDT | below_1h_threshold | +1.71% | +1.52% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.57% | +1.38% |
| EDEN/USDT:USDT | below_1h_threshold | +1.53% | +1.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
