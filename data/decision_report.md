# Decision Report

- generated_at: 2026-05-28T13:59:38.391931+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4964**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.63% / filled 20/20。**
- 全期間 MARKET基準: n=4964, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.44% | **+1.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.14% | **+1.03%** |
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.03% | **+0.72%** |
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.40% | **+0.14%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.14% | **-0.08%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.24% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 699件 (Win 172 / Loss 220 / Flat 307) / skip 826件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T13:59:35.438173+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.68% price=72993.9
- Funnel: target 776 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +33.95% | $11,287,679.61 |
| ONDSSTOCK/USDT:USDT | +24.80% | $1,153,685.00 |
| XLM/USDT:USDT | +22.27% | $201,902,350.24 |
| PRL/USDT:USDT | +16.28% | $2,421,225.55 |
| NBISSTOCK/USDT:USDT | +9.20% | $2,148,192.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +3.99% | +4.67% |
| HBAR/USDT:USDT | below_1h_threshold | +3.91% | +4.59% |
| CRO/USDT:USDT | below_1h_threshold | +2.54% | +3.23% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +2.16% | +2.85% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.89% | +2.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
