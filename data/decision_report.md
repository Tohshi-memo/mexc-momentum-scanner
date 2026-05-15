# Decision Report

- generated_at: 2026-05-15T11:09:29.415698+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4333**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.90% / filled 20/20。**
- 全期間 MARKET基準: n=4333, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.04% | **+2.04%** |
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.87% | **+1.59%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.07% | **+1.45%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.66% | **+1.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.52% | **+0.84%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.61% | **+0.36%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.39% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.81** / 初期 $100.00 (+19.81%)
- 確定: 384件 (Win 97 / Loss 132 / Flat 155) / skip 510件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $119.81

## 4. Latest Market Context

- 更新: 2026-05-15T11:09:25.970779+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=80576.4
- Funnel: target 764 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +28.29% | $4,878,394.71 |
| PEAQ/USDT:USDT | +27.94% | $4,264,134.37 |
| GWEI/USDT:USDT | +23.61% | $1,583,181.32 |
| IRYS/USDT:USDT | +20.28% | $3,207,536.50 |
| FF/USDT:USDT | +15.15% | $1,789,830.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +0.85% | +0.97% |
| GWEI/USDT:USDT | below_1h_threshold | +0.71% | +0.82% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.52% | +0.64% |
| USOIL/USDT:USDT | below_1h_threshold | +0.52% | +0.63% |
| RIVER/USDT:USDT | below_1h_threshold | +0.51% | +0.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
