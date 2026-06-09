# Decision Report

- generated_at: 2026-06-09T11:34:06.480669+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6132**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=6132, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.67% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.64% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.84% | **+0.43%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.75% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.65% | **+0.36%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.18% | **+0.09%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | -0.08% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.67** / 初期 $100.00 (+52.67%)
- 確定: 1172件 (Win 294 / Loss 364 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $152.67

## 4. Latest Market Context

- 更新: 2026-06-09T11:34:03.528685+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=62589.9
- Funnel: target 774 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +49.41% | $21,386,093.89 |
| SLX/USDT:USDT | +30.25% | $5,091,286.26 |
| POWER/USDT:USDT | +19.92% | $2,514,916.40 |
| PLAY/USDT:USDT | +16.88% | $1,802,150.86 |
| SKHYNIXSTOCK/USDT:USDT | +11.29% | $4,422,143.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.83% | +3.09% |
| SLX/USDT:USDT | below_1h_threshold | +2.78% | +3.04% |
| ALLO/USDT:USDT | below_1h_threshold | +2.47% | +2.73% |
| BSB/USDT:USDT | below_1h_threshold | +2.28% | +2.54% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.93% | +2.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
