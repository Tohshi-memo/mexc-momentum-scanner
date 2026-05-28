# Decision Report

- generated_at: 2026-05-28T13:49:01.415691+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4962**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.82% / filled 20/20。**
- 全期間 MARKET基準: n=4962, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.82% | **+1.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.39% | **+1.92%** |
| ASK | 20/20 | 100.0% | +1.91% | **+1.91%** |
| MARKET | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.08% | **+1.76%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.85% | **+1.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.34% | **+0.23%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.16% | **+0.23%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.04% | **+0.01%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.57% | **-0.26%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -3.95% | **-0.39%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 697件 (Win 172 / Loss 220 / Flat 305) / skip 826件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDSSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T13:48:59.241896+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.91% price=72827.4
- Funnel: target 776 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +32.38% | $11,032,358.07 |
| XLM/USDT:USDT | +22.61% | $191,630,231.71 |
| ONDSSTOCK/USDT:USDT | +21.15% | $1,132,068.07 |
| PRL/USDT:USDT | +16.03% | $2,405,715.69 |
| NBISSTOCK/USDT:USDT | +9.48% | $2,135,687.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +4.25% | +5.16% |
| HBAR/USDT:USDT | below_1h_threshold | +2.78% | +3.69% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.91% | +2.82% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +1.84% | +2.75% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.67% | +2.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
