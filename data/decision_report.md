# Decision Report

- generated_at: 2026-05-31T11:06:46.536429+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5189**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.12% / filled 20/20。**
- 全期間 MARKET基準: n=5189, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.97% | **+0.87%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.85% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.13% | **+1.02%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.97% | **+0.83%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.07** / 初期 $100.00 (+25.07%)
- 確定: 824件 (Win 189 / Loss 247 / Flat 388) / skip 926件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $125.07

## 4. Latest Market Context

- 更新: 2026-05-31T11:06:43.972165+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=73896.6
- Funnel: target 773 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +45.02% | $5,679,379.60 |
| AIA/USDT:USDT | +30.72% | $2,860,953.03 |
| PORTAL/USDT:USDT | +21.58% | $11,715,084.48 |
| TA/USDT:USDT | +21.55% | $2,449,737.15 |
| HOME/USDT:USDT | +17.05% | $1,086,475.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +1.96% | +1.92% |
| MYX/USDT:USDT | below_1h_threshold | +0.95% | +0.91% |
| ALGO/USDT:USDT | below_1h_threshold | +0.77% | +0.74% |
| SEI/USDT:USDT | below_1h_threshold | +0.76% | +0.72% |
| ZRO/USDT:USDT | below_1h_threshold | +0.69% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
