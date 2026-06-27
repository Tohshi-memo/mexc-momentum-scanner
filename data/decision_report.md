# Decision Report

- generated_at: 2026-06-27T10:21:16.311886+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7688**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7688, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.87% | **+0.09%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.19% | **+0.87%** |
| ASK_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.38% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$233.69** / 初期 $100.00 (+133.69%)
- 確定: 2213件 (Win 662 / Loss 738 / Flat 813) / skip 2036件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $233.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.17** / 初期 $100.00 (+8.17%)
- 確定: 419件 (Win 114 / Loss 104 / Flat 201) / skip 680件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0468 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $108.17

## 5. Latest Market Context

- 更新: 2026-06-27T10:21:11.620238+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=60450.0
- Funnel: target 806 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +91.75% | $96,196,976.29 |
| MYX/USDT:USDT | +41.95% | $12,096,081.18 |
| SYRUP/USDT:USDT | +20.23% | $1,963,450.03 |
| PUNDIX/USDT:USDT | +18.17% | $6,346,122.33 |
| ARX/USDT:USDT | +14.80% | $2,696,640.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.29% | +2.19% |
| XPL/USDT:USDT | below_1h_threshold | +1.10% | +1.00% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.95% | +0.85% |
| AAVE/USDT:USDT | below_1h_threshold | +0.71% | +0.61% |
| AGI/USDT:USDT | below_1h_threshold | +0.68% | +0.58% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
