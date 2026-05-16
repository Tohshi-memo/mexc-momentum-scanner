# Decision Report

- generated_at: 2026-05-16T14:42:41.539445+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4368**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=4368, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.79% | **+0.47%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.53% | **+0.76%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.05% | **+0.03%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.38% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 391件 (Win 97 / Loss 136 / Flat 158) / skip 538件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T14:42:38.798782+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=78145.4
- Funnel: target 760 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARCSOL/USDT:USDT | +28.56% | $3,353,456.55 |
| RECALL/USDT:USDT | +22.40% | $1,946,104.50 |
| ASTEROID/USDT:USDT | +20.67% | $4,951,703.36 |
| FHE/USDT:USDT | +18.33% | $1,576,420.48 |
| LAB/USDT:USDT | +16.78% | $101,193,481.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RECALL/USDT:USDT | below_1h_threshold | +3.54% | +3.33% |
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +1.82% | +1.61% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.74% | +1.53% |
| FHE/USDT:USDT | below_1h_threshold | +1.52% | +1.31% |
| CHZ/USDT:USDT | below_1h_threshold | +1.23% | +1.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
