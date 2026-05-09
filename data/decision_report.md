# Decision Report

- generated_at: 2026-05-09T07:22:40.979649+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3863**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=3863, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.04% | **+0.73%** |
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.05% | **+0.26%** |
| LIMIT_BB3S | 7/15 | 46.7% | +0.46% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.58% | **+0.40%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.33% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 230件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T07:22:37.875794+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=80217.6
- Funnel: target 767 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +36.41% | $2,581,680.64 |
| CORE/USDT:USDT | +23.33% | $2,711,552.97 |
| ZEREBRO/USDT:USDT | +23.31% | $1,340,273.61 |
| REZ/USDT:USDT | +18.71% | $1,640,273.57 |
| COLLECT/USDT:USDT | +18.24% | $8,436,072.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYM/USDT:USDT | below_1h_threshold | +4.50% | +4.49% |
| PHAROS/USDT:USDT | below_1h_threshold | +2.50% | +2.49% |
| SIREN/USDT:USDT | below_1h_threshold | +1.75% | +1.74% |
| BILL/USDT:USDT | below_1h_threshold | +1.65% | +1.65% |
| THETA/USDT:USDT | below_1h_threshold | +1.59% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
