# Decision Report

- generated_at: 2026-05-08T16:57:35.433153+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3806**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=3806, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.75% | **+0.64%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.41% | **+0.29%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.39% | **+0.20%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.17% | **+0.06%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.10% | **+0.06%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.35% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 175件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T16:57:31.542931+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=79798.3
- Funnel: target 772 → liquid 182 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.4 >= 65=1, 4h RSI 79.0 >= 65=1, 4h RSI 81.7 >= 65=1, 4h RSI 90.4 >= 65=1, 4h RSI 81.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHIP/USDT:USDT | +10.74% | $47,608,436.76 |
| INTCSTOCK/USDT:USDT | +6.55% | $6,976,194.13 |
| JUP/USDT:USDT | +5.82% | $3,607,435.53 |
| ONDO/USDT:USDT | +5.11% | $73,330,610.29 |
| SPORTFUN/USDT:USDT | +4.96% | $1,355,747.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_1h_threshold | +4.19% | +4.58% |
| PENGUIN/USDT:USDT | below_1h_threshold | +4.02% | +4.42% |
| SIREN/USDT:USDT | below_1h_threshold | +3.95% | +4.34% |
| MEGA/USDT:USDT | below_1h_threshold | +3.13% | +3.53% |
| SNX/USDT:USDT | below_1h_threshold | +3.12% | +3.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
