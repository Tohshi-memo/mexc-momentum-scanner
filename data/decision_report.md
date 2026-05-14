# Decision Report

- generated_at: 2026-05-14T02:07:43.516455+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4266**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=4266, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.35% | **+1.21%** |
| ASK | 20/20 | 100.0% | +1.19% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.48% | **+0.96%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.53% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.84% | **+0.50%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.35% | **+0.26%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 484件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T02:07:40.045094+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79600.9
- Funnel: target 765 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +25.77% | $6,285,252.97 |
| SAGA/USDT:USDT | +22.93% | $14,784,937.19 |
| TROLLSOL/USDT:USDT | +22.75% | $1,899,583.45 |
| CSCOSTOCK/USDT:USDT | +22.44% | $4,730,541.18 |
| UP/USDT:USDT | +22.08% | $4,962,584.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.38% | +3.33% |
| BILL/USDT:USDT | below_1h_threshold | +1.85% | +1.80% |
| GIGA/USDT:USDT | below_1h_threshold | +1.19% | +1.14% |
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +0.98% | +0.93% |
| AIN/USDT:USDT | below_1h_threshold | +0.89% | +0.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
