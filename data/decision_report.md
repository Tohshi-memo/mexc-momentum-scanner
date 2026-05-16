# Decision Report

- generated_at: 2026-05-16T00:03:22.732778+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4357**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=4357, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S | 7/17 | 41.2% | +1.69% | **+0.70%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.82% | **+0.49%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.06% | **+0.05%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 528件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T00:03:19.086664+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79054.3
- Funnel: target 759 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +27.10% | $3,262,592.45 |
| ARCSOL/USDT:USDT | +23.25% | $1,223,169.20 |
| STORJ/USDT:USDT | +16.66% | $4,757,922.62 |
| LAB/USDT:USDT | +15.03% | $148,721,631.04 |
| PEAQ/USDT:USDT | +12.58% | $5,013,301.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +0.80% | +0.83% |
| CGPT/USDT:USDT | below_1h_threshold | +0.45% | +0.47% |
| GUA/USDT:USDT | below_1h_threshold | +0.41% | +0.44% |
| TAC/USDT:USDT | below_1h_threshold | +0.39% | +0.42% |
| COLLECT/USDT:USDT | below_1h_threshold | +0.39% | +0.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
