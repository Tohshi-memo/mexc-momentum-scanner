# Decision Report

- generated_at: 2026-05-15T22:18:24.761927+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4353**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4353, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/14 | 42.9% | +2.09% | **+0.89%** |
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.45% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.06% | **+0.05%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.52% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 524件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-15T22:18:21.510766+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79027.3
- Funnel: target 759 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARCSOL/USDT:USDT | +25.80% | $1,067,996.18 |
| ASTEROID/USDT:USDT | +22.72% | $3,054,649.29 |
| STORJ/USDT:USDT | +22.58% | $4,025,839.47 |
| PEAQ/USDT:USDT | +14.17% | $5,392,201.76 |
| LAB/USDT:USDT | +11.00% | $147,726,550.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PNUT/USDT:USDT | below_1h_threshold | +0.93% | +0.81% |
| GUA/USDT:USDT | below_1h_threshold | +0.74% | +0.62% |
| VVV/USDT:USDT | below_1h_threshold | +0.73% | +0.61% |
| CHZ/USDT:USDT | below_1h_threshold | +0.73% | +0.61% |
| ZRO/USDT:USDT | below_1h_threshold | +0.69% | +0.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
