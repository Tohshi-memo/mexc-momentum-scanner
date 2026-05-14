# Decision Report

- generated_at: 2026-05-14T04:12:30.478616+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4270**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.89% / filled 20/20。**
- 全期間 MARKET基準: n=4270, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.24% | **+1.12%** |
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.90% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.90% | **+1.45%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.69% | **+0.67%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.42% | **+0.57%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 488件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T04:12:27.245400+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=79219.9
- Funnel: target 765 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CSCOSTOCK/USDT:USDT | +23.00% | $4,932,066.20 |
| UP/USDT:USDT | +19.94% | $5,043,856.39 |
| IRYS/USDT:USDT | +16.35% | $5,917,216.67 |
| SAGA/USDT:USDT | +15.63% | $16,504,147.69 |
| AIN/USDT:USDT | +14.62% | $2,661,028.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.01% | +2.74% |
| VELVET/USDT:USDT | below_1h_threshold | +2.40% | +2.13% |
| JCT/USDT:USDT | below_1h_threshold | +2.34% | +2.07% |
| GIGA/USDT:USDT | below_1h_threshold | +2.11% | +1.84% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.84% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
