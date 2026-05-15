# Decision Report

- generated_at: 2026-05-15T13:33:26.315663+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4338**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.79% / filled 20/20。**
- 全期間 MARKET基準: n=4338, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.79% | **+2.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.87% | **+2.87%** |
| MARKET | 20/20 | 100.0% | +2.79% | **+2.79%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.68% | **+2.28%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.31% | **+1.73%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.41% | **+1.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.92% | **+0.55%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.92% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.58** / 初期 $100.00 (+18.58%)
- 確定: 388件 (Win 97 / Loss 135 / Flat 156) / skip 511件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UP/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $118.58

## 4. Latest Market Context

- 更新: 2026-05-15T13:33:22.519800+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.80% price=79709.9
- Funnel: target 764 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +26.02% | $8,626,633.83 |
| GWEI/USDT:USDT | +25.06% | $1,796,254.85 |
| PEAQ/USDT:USDT | +18.35% | $4,573,405.41 |
| UP/USDT:USDT | +17.99% | $5,547,154.71 |
| GUA/USDT:USDT | +16.17% | $1,492,649.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUTH/USDT:USDT | below_1h_threshold | +4.02% | +4.82% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.66% | +3.46% |
| GUA/USDT:USDT | below_1h_threshold | +2.21% | +3.01% |
| RIVER/USDT:USDT | below_1h_threshold | +1.50% | +2.30% |
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +1.48% | +2.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
