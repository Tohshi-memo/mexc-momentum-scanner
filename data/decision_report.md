# Decision Report

- generated_at: 2026-05-29T22:49:41.189090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5073**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=5073, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/19 | 52.6% | +1.92% | **+1.01%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.43% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.42% | **+0.38%** |
| ASK_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.91% | **+0.27%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 894件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T22:49:36.574649+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=73468.3
- Funnel: target 773 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +28.89% | $1,040,779.97 |
| BASED/USDT:USDT | +19.19% | $2,160,739.93 |
| LAB/USDT:USDT | +16.48% | $124,918,563.83 |
| XLM/USDT:USDT | +15.31% | $373,240,376.88 |
| GRASS/USDT:USDT | +6.50% | $4,282,101.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OL/USDT:USDT | below_1h_threshold | +3.63% | +3.52% |
| LAB/USDT:USDT | below_1h_threshold | +3.59% | +3.48% |
| XLM/USDT:USDT | below_1h_threshold | +3.24% | +3.13% |
| BASED/USDT:USDT | below_1h_threshold | +2.90% | +2.78% |
| QNTSTOCK/USDT:USDT | below_1h_threshold | +2.51% | +2.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
