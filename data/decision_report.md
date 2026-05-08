# Decision Report

- generated_at: 2026-05-08T17:27:41.699344+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3810**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=3810, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| ASK | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.64% | **+0.55%** |
| LIMIT_BB3S | 3/14 | 21.4% | +0.68% | **+0.14%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.86% | **+0.43%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.15% | **+0.06%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.01% | **+0.01%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.38% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 179件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T17:27:38.332181+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=79977.0
- Funnel: target 772 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SIREN/USDT:USDT | +10.67% | $15,147,092.51 |
| COLLECT/USDT:USDT | +8.37% | $1,448,337.94 |
| JUP/USDT:USDT | +8.23% | $4,094,376.98 |
| CHIP/USDT:USDT | +7.11% | $49,225,484.23 |
| INTCSTOCK/USDT:USDT | +6.92% | $8,138,878.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_1h_threshold | +4.04% | +3.78% |
| SATO/USDT:USDT | below_1h_threshold | +3.58% | +3.32% |
| PLAY/USDT:USDT | below_1h_threshold | +3.46% | +3.20% |
| OP/USDT:USDT | below_1h_threshold | +3.13% | +2.87% |
| JUP/USDT:USDT | below_1h_threshold | +2.67% | +2.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
