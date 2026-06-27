# Decision Report

- generated_at: 2026-06-27T07:56:37.066390+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7678**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7678, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.46% | **+0.07%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.62% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.08% | **+1.35%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.72% | **+1.09%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.93% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.42** / 初期 $100.00 (+138.42%)
- 確定: 2203件 (Win 662 / Loss 734 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $238.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.76** / 初期 $100.00 (+8.76%)
- 確定: 409件 (Win 113 / Loss 102 / Flat 194) / skip 680件
- 成長率目線: 平均log +0.000205 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0869 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: O/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $108.76

## 5. Latest Market Context

- 更新: 2026-06-27T07:56:31.253250+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=60546.8
- Funnel: target 806 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MYX/USDT:USDT | +37.19% | $9,611,975.27 |
| VELVET/USDT:USDT | +32.40% | $60,575,313.42 |
| SYRUP/USDT:USDT | +18.73% | $1,651,914.25 |
| PUNDIX/USDT:USDT | +18.04% | $6,140,996.51 |
| SLX/USDT:USDT | +14.77% | $10,935,135.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +4.59% | +4.25% |
| MYX/USDT:USDT | below_1h_threshold | +3.60% | +3.26% |
| O/USDT:USDT | below_1h_threshold | +3.19% | +2.85% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.55% | +2.22% |
| WIF/USDT:USDT | below_1h_threshold | +2.00% | +1.66% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
