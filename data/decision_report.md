# Decision Report

- generated_at: 2026-05-14T06:03:08.611310+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4273**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=4273, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.08% | **+1.87%** |
| ASK | 20/20 | 100.0% | +1.56% | **+1.56%** |
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.63% | **+1.22%** |
| LIMIT_BB3S | 3/15 | 20.0% | +5.90% | **+1.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.36% | **+3.36%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.39% | **+1.07%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.15% | **+0.97%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.14% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 491件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T06:03:05.381488+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=79823.1
- Funnel: target 766 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CSCOSTOCK/USDT:USDT | +21.75% | $5,021,862.02 |
| UP/USDT:USDT | +19.94% | $5,254,368.33 |
| TROLLSOL/USDT:USDT | +18.76% | $1,962,958.79 |
| IRYS/USDT:USDT | +17.10% | $5,420,310.00 |
| PIEVERSE/USDT:USDT | +16.65% | $1,279,647.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +1.00% | +0.93% |
| AIN/USDT:USDT | below_1h_threshold | +0.87% | +0.81% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.70% | +0.64% |
| SAGA/USDT:USDT | below_1h_threshold | +0.67% | +0.61% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.31% | +0.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
