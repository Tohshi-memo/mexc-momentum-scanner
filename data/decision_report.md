# Decision Report

- generated_at: 2026-06-12T17:54:09.990460+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6532**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=6532, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| ASK | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.98% | **+1.09%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.22% | **+0.97%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.81% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.83% | **+1.13%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.20% | **+0.14%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.14% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$94.22** / 初期 $100.00 (-5.78%)
- 確定トレード: 22件 (TP 3 / SL 18 / EXP 1)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $94.22
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$165.48** / 初期 $100.00 (+65.48%)
- 確定: 1405件 (Win 387 / Loss 458 / Flat 560) / skip 1688件
- 成長率目線: 平均log +0.000358 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $165.48

## 4. Latest Market Context

- 更新: 2026-06-12T17:54:04.204548+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=63819.4
- Funnel: target 774 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +12.60% | $1,656,990.20 |
| H/USDT:USDT | +11.99% | $30,059,616.68 |
| ESPORTS/USDT:USDT | +11.93% | $67,542,946.34 |
| PLAY/USDT:USDT | +11.82% | $9,025,947.89 |
| HOME/USDT:USDT | +7.03% | $3,151,873.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.49% | +4.70% |
| ASTEROID/USDT:USDT | below_1h_threshold | +4.40% | +4.61% |
| AIN/USDT:USDT | below_1h_threshold | +4.13% | +4.34% |
| HOME/USDT:USDT | below_1h_threshold | +4.13% | +4.34% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.62% | +2.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
