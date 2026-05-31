# Decision Report

- generated_at: 2026-05-31T12:01:30.221719+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5191**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=5191, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.55% | **+0.52%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.00% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.23%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.36% | **+1.02%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.07** / 初期 $100.00 (+25.07%)
- 確定: 826件 (Win 189 / Loss 247 / Flat 390) / skip 926件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $125.07

## 4. Latest Market Context

- 更新: 2026-05-31T12:01:27.969806+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=73956.4
- Funnel: target 773 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +42.12% | $6,837,908.82 |
| AIA/USDT:USDT | +35.41% | $3,011,936.11 |
| PORTAL/USDT:USDT | +23.22% | $11,080,889.70 |
| TA/USDT:USDT | +21.50% | $2,441,084.69 |
| STG/USDT:USDT | +18.61% | $3,869,053.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +1.21% | +1.15% |
| PLAY/USDT:USDT | below_1h_threshold | +1.06% | +1.00% |
| GUA/USDT:USDT | below_1h_threshold | +0.92% | +0.86% |
| MYX/USDT:USDT | below_1h_threshold | +0.74% | +0.69% |
| HIVE/USDT:USDT | below_1h_threshold | +0.74% | +0.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
