# Decision Report

- generated_at: 2026-06-01T02:26:53.786709+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5262**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=5262, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.44% | **+0.44%** |
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.66% | **+0.46%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.13% | **+0.41%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.69** / 初期 $100.00 (+31.69%)
- 確定: 893件 (Win 207 / Loss 268 / Flat 418) / skip 930件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.69

## 4. Latest Market Context

- 更新: 2026-06-01T02:26:50.413956+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=73490.6
- Funnel: target 777 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.8 >= 65=1, 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +201.15% | $25,222,160.72 |
| H/USDT:USDT | +73.45% | $19,137,082.22 |
| STG/USDT:USDT | +22.47% | $22,300,845.39 |
| CTR/USDT:USDT | +19.95% | $1,436,386.38 |
| WLD/USDT:USDT | +15.74% | $55,393,281.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +4.91% | +4.59% |
| VVV/USDT:USDT | below_1h_threshold | +4.27% | +3.96% |
| STG/USDT:USDT | below_1h_threshold | +3.80% | +3.48% |
| CTR/USDT:USDT | below_1h_threshold | +3.75% | +3.43% |
| ICP/USDT:USDT | below_1h_threshold | +3.17% | +2.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
