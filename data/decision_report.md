# Decision Report

- generated_at: 2026-05-10T01:02:45.168051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3931**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=3931, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.67% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.77% | **+0.97%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.71% | **+0.36%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 196件 (Win 48 / Loss 66 / Flat 82) / skip 296件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T01:02:42.197839+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=80555.0
- Funnel: target 769 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INX/USDT:USDT | +37.19% | $11,034,168.12 |
| SATO/USDT:USDT | +15.68% | $5,524,605.20 |
| BILL/USDT:USDT | +14.91% | $38,524,464.02 |
| MITO/USDT:USDT | +13.22% | $3,647,432.02 |
| JASMY/USDT:USDT | +12.51% | $16,208,195.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KITE/USDT:USDT | below_1h_threshold | +1.42% | +1.52% |
| BILL/USDT:USDT | below_1h_threshold | +1.24% | +1.34% |
| STRK/USDT:USDT | below_1h_threshold | +0.60% | +0.70% |
| PHAROS/USDT:USDT | below_1h_threshold | +0.36% | +0.46% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.32% | +0.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
