# Decision Report

- generated_at: 2026-05-20T12:28:53.996061+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4542**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.89% / filled 20/20。**
- 全期間 MARKET基準: n=4542, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.91% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.71% | **+0.60%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.72% | **+0.51%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.04% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.07% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.01% | **+0.01%** |
| MARKET_LONG | 20/20 | 100.0% | -0.12% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.76** / 初期 $100.00 (+23.76%)
- 確定: 504件 (Win 131 / Loss 174 / Flat 199) / skip 599件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $123.76

## 4. Latest Market Context

- 更新: 2026-05-20T12:28:51.767453+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=77465.4
- Funnel: target 763 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +88.94% | $2,189,352.54 |
| FIDA/USDT:USDT | +44.80% | $3,538,149.46 |
| PLAY/USDT:USDT | +30.59% | $10,618,923.94 |
| BANANAS31/USDT:USDT | +27.73% | $2,050,310.15 |
| PROMPT/USDT:USDT | +26.31% | $12,760,680.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +4.15% | +4.00% |
| ZEST/USDT:USDT | below_1h_threshold | +4.08% | +3.93% |
| UP/USDT:USDT | below_1h_threshold | +2.68% | +2.53% |
| PLAY/USDT:USDT | below_1h_threshold | +2.39% | +2.24% |
| NIL/USDT:USDT | below_1h_threshold | +1.93% | +1.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
