# Decision Report

- generated_at: 2026-05-26T09:34:37.325927+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4894**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=4894, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +1.56% | **+1.01%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.65% | **+0.58%** |
| LIMIT_BB3S | 3/18 | 16.7% | +2.24% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +8.00% | **+8.00%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.60% | **+0.33%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.81% | **+0.32%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.65% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.87** / 初期 $100.00 (+29.87%)
- 確定: 675件 (Win 171 / Loss 214 / Flat 290) / skip 780件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DRIFT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $129.87

## 4. Latest Market Context

- 更新: 2026-05-26T09:34:34.514256+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=76697.6
- Funnel: target 769 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +82.14% | $2,622,285.89 |
| DRIFT/USDT:USDT | +33.21% | $2,039,992.63 |
| WLD/USDT:USDT | +22.57% | $83,768,928.39 |
| OKB/USDT:USDT | +13.12% | $1,017,179.37 |
| GRASS/USDT:USDT | +9.73% | $9,232,294.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.25% | +2.24% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.20% | +2.19% |
| POND/USDT:USDT | below_1h_threshold | +1.20% | +1.19% |
| ICP/USDT:USDT | below_1h_threshold | +0.90% | +0.88% |
| GENIUS/USDT:USDT | below_1h_threshold | +0.80% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
