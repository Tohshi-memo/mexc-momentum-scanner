# Decision Report

- generated_at: 2026-05-29T08:49:38.871017+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5032**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=5032, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.69% | **+0.69%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.16% | **+0.99%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.03% | **+0.81%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.11% | **+0.78%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$99.59** / 初期 $100.00 (-0.41%)
- 確定トレード: 72件 (TP 22 / SL 47 / EXP 3)
- 最新: SAGA/USDT:USDT TP_HIT PnL +5.72% 残高後 $99.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 853件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T08:49:35.756196+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=73716.0
- Funnel: target 777 → liquid 146 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +137.08% | $73,151,053.62 |
| CTR/USDT:USDT | +36.76% | $1,466,263.78 |
| DELLSTOCK/USDT:USDT | +34.18% | $8,924,918.08 |
| CLO/USDT:USDT | +19.71% | $1,710,338.08 |
| AIGENSYN/USDT:USDT | +18.93% | $1,876,721.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CTR/USDT:USDT | below_1h_threshold | +4.12% | +3.81% |
| NIL/USDT:USDT | below_1h_threshold | +2.83% | +2.51% |
| CLO/USDT:USDT | below_1h_threshold | +2.07% | +1.76% |
| ALGO/USDT:USDT | below_1h_threshold | +2.06% | +1.75% |
| NOWSTOCK/USDT:USDT | below_1h_threshold | +1.76% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
