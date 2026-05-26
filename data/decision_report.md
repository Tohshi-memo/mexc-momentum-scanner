# Decision Report

- generated_at: 2026-05-26T14:13:55.315913+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4901**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=4901, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 12/20 | 60.0% | +1.51% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +8.00% | **+8.00%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +2.40% | **+0.72%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.25% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.87** / 初期 $100.00 (+29.87%)
- 確定: 675件 (Win 171 / Loss 214 / Flat 290) / skip 787件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DRIFT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $129.87

## 4. Latest Market Context

- 更新: 2026-05-26T14:13:53.418815+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77271.1
- Funnel: target 769 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +65.00% | $2,877,394.30 |
| WLD/USDT:USDT | +25.43% | $162,185,886.02 |
| DRIFT/USDT:USDT | +21.11% | $3,958,522.70 |
| IO/USDT:USDT | +16.78% | $1,327,945.66 |
| OKB/USDT:USDT | +14.13% | $1,674,035.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RENDER/USDT:USDT | below_1h_threshold | +2.16% | +2.07% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.05% | +1.96% |
| XPL/USDT:USDT | below_1h_threshold | +1.88% | +1.79% |
| HYPE/USDT:USDT | below_1h_threshold | +1.72% | +1.63% |
| RIVER/USDT:USDT | below_1h_threshold | +1.50% | +1.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
