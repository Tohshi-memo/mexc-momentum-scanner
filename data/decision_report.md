# Decision Report

- generated_at: 2026-05-14T03:02:55.914116+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4267**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.59% / filled 20/20。**
- 全期間 MARKET基準: n=4267, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.59% | **+1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.61% | **+1.61%** |
| MARKET | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.72% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.39% | **+1.07%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.73% | **+0.48%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 485件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T03:02:52.655651+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79420.6
- Funnel: target 765 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +29.38% | $15,071,059.53 |
| IRYS/USDT:USDT | +25.61% | $6,133,787.07 |
| TROLLSOL/USDT:USDT | +22.16% | $1,926,721.57 |
| CSCOSTOCK/USDT:USDT | +21.40% | $4,798,731.00 |
| UP/USDT:USDT | +21.09% | $5,022,778.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +1.80% | +1.69% |
| UB/USDT:USDT | below_1h_threshold | +1.24% | +1.13% |
| LAB/USDT:USDT | below_1h_threshold | +1.19% | +1.07% |
| RIF/USDT:USDT | below_1h_threshold | +1.04% | +0.92% |
| SAGA/USDT:USDT | below_1h_threshold | +0.74% | +0.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
