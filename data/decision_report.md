# Decision Report

- generated_at: 2026-07-20T06:51:17.596773+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9090**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9090, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.94% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +4.11% | **+0.82%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.59% | **+0.72%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.66%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$108.60** / 初期 $100.00 (+8.60%)
- 確定トレード: 121件 (TP 43 / SL 73 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -3.98% 残高後 $108.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.37** / 初期 $100.00 (+299.37%)
- 確定: 3152件 (Win 986 / Loss 1001 / Flat 1165) / skip 2499件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $399.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.19** / 初期 $100.00 (+26.19%)
- 確定: 1051件 (Win 271 / Loss 218 / Flat 562) / skip 1450件
- 成長率目線: 平均log +0.000221 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0303 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $126.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.98** / 初期 $100.00 (+0.98%)
- 確定: 289件 (Win 96 / Loss 131 / Flat 62) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000156 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.98

## 6. Latest Market Context

- 更新: 2026-07-20T06:51:10.814991+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=63890.3
- Funnel: target 886 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +81.87% | $6,339,293.39 |
| BANK/USDT:USDT | +54.69% | $102,295,338.57 |
| PUMPFUN/USDT:USDT | +18.37% | $20,121,986.82 |
| PROM/USDT:USDT | +17.95% | $2,519,098.52 |
| EVAA/USDT:USDT | +15.22% | $3,691,811.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +3.97% | +4.30% |
| EVAA/USDT:USDT | below_1h_threshold | +3.34% | +3.67% |
| BEAT/USDT:USDT | below_1h_threshold | +2.05% | +2.38% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.54% | +1.87% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.81% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
