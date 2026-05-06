# Decision Report

- generated_at: 2026-05-06T13:27:15.588377+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3461**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=3461, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.39% | **+0.66%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.88% | **+0.47%** |
| ASK | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.26% | **+0.16%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 13件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T13:27:13.540623+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=81838.6
- Funnel: target 770 → liquid 200 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +90.60% | $2,804,652.37 |
| IO/USDT:USDT | +36.73% | $14,626,163.49 |
| TONCOIN/USDT:USDT | +34.63% | $228,067,187.88 |
| ZEC/USDT:USDT | +34.14% | $768,843,092.10 |
| BILL/USDT:USDT | +32.70% | $4,916,168.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IO/USDT:USDT | below_1h_threshold | +2.42% | +2.85% |
| H/USDT:USDT | below_1h_threshold | +2.16% | +2.59% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.46% | +1.88% |
| M/USDT:USDT | below_1h_threshold | +0.98% | +1.41% |
| JTO/USDT:USDT | below_1h_threshold | +0.97% | +1.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
