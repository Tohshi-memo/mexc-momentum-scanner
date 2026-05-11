# Decision Report

- generated_at: 2026-05-11T02:32:42.559530+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4004**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=4004, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |
| ASK | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_BB3S | 6/12 | 50.0% | +2.96% | **+1.48%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.56% | **+1.33%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.35% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.95% | **+1.46%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.09% | **+0.99%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.00% | **+0.90%** |
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.11** / 初期 $100.00 (+9.11%)
- 確定: 210件 (Win 53 / Loss 72 / Flat 85) / skip 355件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ENS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $109.11

## 4. Latest Market Context

- 更新: 2026-05-11T02:32:39.374064+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=81121.5
- Funnel: target 775 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +30.27% | $9,709,095.20 |
| ALCH/USDT:USDT | +19.81% | $3,902,573.51 |
| TROLLSOL/USDT:USDT | +17.73% | $5,399,208.90 |
| B/USDT:USDT | +12.47% | $2,753,751.96 |
| OPG/USDT:USDT | +11.33% | $1,215,288.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +2.21% | +2.63% |
| BEAT/USDT:USDT | below_1h_threshold | +1.37% | +1.79% |
| OPG/USDT:USDT | below_1h_threshold | +1.37% | +1.79% |
| BAS/USDT:USDT | below_1h_threshold | +1.35% | +1.77% |
| TRUTH/USDT:USDT | below_1h_threshold | +0.64% | +1.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
