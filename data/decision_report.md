# Decision Report

- generated_at: 2026-06-10T22:20:36.879243+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6272**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6272, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.68% | **+1.21%** |
| MARKET_LONG | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.14% | **+0.86%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.97** / 初期 $100.00 (+51.97%)
- 確定: 1258件 (Win 317 / Loss 392 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000333 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $151.97

## 4. Latest Market Context

- 更新: 2026-06-10T22:20:32.915041+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=61092.2
- Funnel: target 785 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1, 4h RSI 73.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +74.86% | $33,561,630.91 |
| BEAT/USDT:USDT | +39.22% | $164,921,336.67 |
| STRAX/USDT:USDT | +21.67% | $1,248,177.18 |
| UAI/USDT:USDT | +5.90% | $1,961,494.90 |
| POWER/USDT:USDT | +5.37% | $1,475,606.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +2.26% | +2.65% |
| XMR/USDT:USDT | below_1h_threshold | +1.30% | +1.68% |
| UB/USDT:USDT | below_1h_threshold | +1.22% | +1.60% |
| POWER/USDT:USDT | below_1h_threshold | +0.86% | +1.24% |
| UAI/USDT:USDT | below_1h_threshold | +0.83% | +1.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
