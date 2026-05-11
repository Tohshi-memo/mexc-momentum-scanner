# Decision Report

- generated_at: 2026-05-11T07:02:48.778674+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4015**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=4015, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| ASK | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.87% | **+0.94%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.96% | **+0.72%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.45% | **+0.32%** |
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.25% | **+0.16%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.57% | **+0.11%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.03% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定トレード: 32件 (TP 8 / SL 21 / EXP 3)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 358件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T07:02:45.851182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80759.1
- Funnel: target 761 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +35.02% | $5,852,385.67 |
| US/USDT:USDT | +34.55% | $10,892,689.13 |
| SAGA/USDT:USDT | +22.55% | $1,407,522.62 |
| TROLLSOL/USDT:USDT | +18.70% | $4,940,620.99 |
| ALCH/USDT:USDT | +17.71% | $4,532,508.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.27% | +3.31% |
| US/USDT:USDT | below_1h_threshold | +0.44% | +0.48% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +0.44% | +0.48% |
| UB/USDT:USDT | below_1h_threshold | +0.39% | +0.43% |
| LDO/USDT:USDT | below_1h_threshold | +0.35% | +0.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
