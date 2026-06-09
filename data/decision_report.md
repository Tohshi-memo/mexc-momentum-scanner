# Decision Report

- generated_at: 2026-06-09T13:31:57.783025+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6138**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.85% / filled 20/20。**
- 全期間 MARKET基準: n=6138, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.88% | **+1.88%** |
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.62% | **+1.22%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.12% | **+0.95%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.64% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.43% | **+0.21%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.63** / 初期 $100.00 (+49.63%)
- 確定: 1178件 (Win 295 / Loss 369 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.63

## 4. Latest Market Context

- 更新: 2026-06-09T13:31:52.229959+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=62378.6
- Funnel: target 774 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +39.01% | $23,183,757.98 |
| POWER/USDT:USDT | +29.55% | $3,643,480.52 |
| SLX/USDT:USDT | +28.83% | $5,554,017.03 |
| JCT/USDT:USDT | +27.28% | $1,022,476.81 |
| IO/USDT:USDT | +20.45% | $1,001,222.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.01% | +3.38% |
| HOME/USDT:USDT | below_1h_threshold | +2.98% | +3.35% |
| ALLO/USDT:USDT | below_1h_threshold | +2.82% | +3.19% |
| CTR/USDT:USDT | below_1h_threshold | +2.61% | +2.98% |
| BTW/USDT:USDT | below_1h_threshold | +2.07% | +2.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
