# Decision Report

- generated_at: 2026-06-12T16:22:55.113422+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6522**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6522, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.31% | **+0.20%** |
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.24% | **+1.91%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.81% | **+0.53%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.76% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$166.33** / 初期 $100.00 (+66.33%)
- 確定: 1395件 (Win 385 / Loss 454 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000365 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $166.33

## 4. Latest Market Context

- 更新: 2026-06-12T16:22:49.615126+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=63805.1
- Funnel: target 774 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +7.25% | $2,581,254.55 |
| RKLBSTOCK/USDT:USDT | +5.28% | $1,004,378.70 |
| SOXL/USDT:USDT | +3.29% | $4,126,449.70 |
| ESPORTS/USDT:USDT | +3.27% | $65,089,338.24 |
| COAI/USDT:USDT | +3.05% | $4,127,799.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RKLBSTOCK/USDT:USDT | below_relative_strength | +5.29% | +4.90% |
| COAI/USDT:USDT | below_1h_threshold | +3.34% | +2.95% |
| SOXL/USDT:USDT | below_1h_threshold | +3.29% | +2.90% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.09% | +2.70% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
