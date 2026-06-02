# Decision Report

- generated_at: 2026-06-02T04:08:06.105257+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5401**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.02% / filled 20/20。**
- 全期間 MARKET基準: n=5401, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.83% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.60% | **+0.57%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.27% | **+0.17%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.11% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.59** / 初期 $100.00 (+32.59%)
- 確定: 913件 (Win 212 / Loss 272 / Flat 429) / skip 1049件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MRVLSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $132.59

## 4. Latest Market Context

- 更新: 2026-06-02T04:08:03.736581+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=70908.5
- Funnel: target 777 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +23.77% | $199,110,626.00 |
| SKYAI/USDT:USDT | +23.65% | $4,433,683.59 |
| MRVLSTOCK/USDT:USDT | +22.09% | $1,501,198.82 |
| RIF/USDT:USDT | +20.31% | $1,335,412.25 |
| ESPORTS/USDT:USDT | +18.09% | $10,921,041.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +1.88% | +1.90% |
| LAB/USDT:USDT | below_1h_threshold | +1.86% | +1.87% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.73% | +1.74% |
| H/USDT:USDT | below_1h_threshold | +1.69% | +1.71% |
| STG/USDT:USDT | below_1h_threshold | +1.41% | +1.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
