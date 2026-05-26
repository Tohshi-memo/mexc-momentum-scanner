# Decision Report

- generated_at: 2026-05-26T10:14:35.110198+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4895**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=4895, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.34% | **+0.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +8.00% | **+8.00%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.48% | **+0.45%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.08% | **+0.38%** |
| MARKET_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.87** / 初期 $100.00 (+29.87%)
- 確定: 675件 (Win 171 / Loss 214 / Flat 290) / skip 781件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DRIFT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $129.87

## 4. Latest Market Context

- 更新: 2026-05-26T10:14:32.939384+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=76682.9
- Funnel: target 769 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +80.71% | $2,667,019.98 |
| DRIFT/USDT:USDT | +32.13% | $2,121,505.62 |
| WLD/USDT:USDT | +26.09% | $90,682,710.27 |
| OKB/USDT:USDT | +13.68% | $1,095,475.29 |
| GRASS/USDT:USDT | +11.17% | $9,238,535.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +1.95% | +1.90% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.55% | +1.49% |
| FET/USDT:USDT | below_1h_threshold | +1.39% | +1.34% |
| RENDER/USDT:USDT | below_1h_threshold | +0.94% | +0.89% |
| NEAR/USDT:USDT | below_1h_threshold | +0.92% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
