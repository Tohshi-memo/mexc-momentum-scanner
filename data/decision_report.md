# Decision Report

- generated_at: 2026-08-09T05:36:28.335821+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10944**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=10944, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.21% | **+1.09%** |
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.17% | **+0.76%** |
| LIMIT_BB3S | 4/17 | 23.5% | +2.41% | **+0.57%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.69% | **+0.27%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.85% | **+0.21%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.26% | **+0.09%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.88% | **-0.39%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.11** / 初期 $100.00 (+528.11%)
- 確定: 3931件 (Win 1230 / Loss 1281 / Flat 1420) / skip 3574件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $628.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2844件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1172件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T05:36:17.446526+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=64758.1
- Funnel: target 961 → liquid 154 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 98.3 >= 65=1, 4h RSI 79.0 >= 65=1, 4h RSI 66.7 >= 65=1, 4h RSI 92.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +137.15% | $33,872,153.98 |
| BLUAI/USDT:USDT | +51.23% | $8,585,628.54 |
| IOTX/USDT:USDT | +35.27% | $3,467,246.07 |
| COOKIE/USDT:USDT | +26.28% | $4,336,886.70 |
| SAGA/USDT:USDT | +25.57% | $3,609,724.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.30% | +4.30% |
| 4/USDT:USDT | below_1h_threshold | +4.23% | +4.23% |
| GIGGLE/USDT:USDT | below_1h_threshold | +3.35% | +3.35% |
| CATI/USDT:USDT | below_1h_threshold | +3.09% | +3.09% |
| BTW/USDT:USDT | below_1h_threshold | +3.08% | +3.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
