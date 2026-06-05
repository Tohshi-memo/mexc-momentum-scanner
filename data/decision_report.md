# Decision Report

- generated_at: 2026-06-05T10:45:41.640043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5713**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=5713, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| ASK | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.45% | **+1.16%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.84% | **+0.64%** |
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.01% | **+0.51%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1264件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T10:45:38.373804+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=62571.3
- Funnel: target 773 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +84.18% | $23,598,210.34 |
| BABY/USDT:USDT | +48.60% | $5,602,325.31 |
| CLO/USDT:USDT | +20.36% | $1,119,655.31 |
| BEAT/USDT:USDT | +11.69% | $28,493,194.17 |
| OPN/USDT:USDT | +10.77% | $40,857,668.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APPSTOCK/USDT:USDT | below_1h_threshold | +2.54% | +2.96% |
| BTW/USDT:USDT | below_1h_threshold | +2.35% | +2.76% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.72% | +2.13% |
| UP/USDT:USDT | below_1h_threshold | +0.89% | +1.31% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +0.41% | +0.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
