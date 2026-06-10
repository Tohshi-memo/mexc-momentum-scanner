# Decision Report

- generated_at: 2026-06-10T01:55:47.919693+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6177**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6177, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.06% | **+1.42%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.68% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| ASK_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.74** / 初期 $100.00 (+48.74%)
- 確定: 1194件 (Win 298 / Loss 375 / Flat 521) / skip 1544件
- 成長率目線: 平均log +0.000333 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $148.74

## 4. Latest Market Context

- 更新: 2026-06-10T01:55:44.446344+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=61721.4
- Funnel: target 778 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1, 4h RSI 80.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +78.18% | $16,327,342.30 |
| STG/USDT:USDT | +36.69% | $3,619,460.77 |
| HOME/USDT:USDT | +15.96% | $4,429,896.87 |
| UB/USDT:USDT | +13.92% | $1,498,535.89 |
| SENT/USDT:USDT | +9.00% | $1,702,606.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.16% | +4.42% |
| IO/USDT:USDT | below_1h_threshold | +2.46% | +2.72% |
| NEAR/USDT:USDT | below_1h_threshold | +2.10% | +2.37% |
| LIT/USDT:USDT | below_1h_threshold | +1.71% | +1.98% |
| UB/USDT:USDT | below_1h_threshold | +1.32% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
