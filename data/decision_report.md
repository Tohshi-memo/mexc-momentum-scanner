# Decision Report

- generated_at: 2026-05-27T16:14:50.645960+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4931**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=4931, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.07% | **+1.02%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.15% | **+0.98%** |
| ASK | 20/20 | 100.0% | +0.92% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.79% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.46% | **+0.87%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.52% | **+0.76%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.50% | **+0.17%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.07% | **+0.06%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 808件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T16:14:48.505064+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=75257.0
- Funnel: target 774 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +2.41% | $20,434,300.88 |
| ORDI/USDT:USDT | +1.74% | $3,920,057.34 |
| FF/USDT:USDT | +1.60% | $1,647,955.09 |
| SNDKSTOCK/USDT:USDT | +1.46% | $5,453,144.57 |
| SKYAI/USDT:USDT | +1.46% | $6,660,566.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.40% | +2.46% |
| ORDI/USDT:USDT | below_1h_threshold | +1.74% | +1.80% |
| FF/USDT:USDT | below_1h_threshold | +1.61% | +1.66% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.51% | +1.56% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.46% | +1.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
