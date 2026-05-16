# Decision Report

- generated_at: 2026-05-16T00:23:23.470630+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4359**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=4359, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.71% | **+0.71%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.20% | **+0.35%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.70% | **+0.38%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 530件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T00:23:20.067908+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=79130.0
- Funnel: target 759 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +29.83% | $3,310,176.90 |
| ARCSOL/USDT:USDT | +25.68% | $1,269,625.57 |
| STORJ/USDT:USDT | +15.86% | $4,874,278.37 |
| PEAQ/USDT:USDT | +14.94% | $5,040,603.05 |
| LAB/USDT:USDT | +14.39% | $150,807,236.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POLYX/USDT:USDT | below_1h_threshold | +3.57% | +3.50% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.99% | +2.92% |
| SIREN/USDT:USDT | below_1h_threshold | +2.92% | +2.85% |
| QNT/USDT:USDT | below_1h_threshold | +2.19% | +2.12% |
| CGPT/USDT:USDT | below_1h_threshold | +1.78% | +1.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
