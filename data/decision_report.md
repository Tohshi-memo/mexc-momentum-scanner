# Decision Report

- generated_at: 2026-06-27T04:30:36.897858+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7670**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7670, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.30% | **-0.09%** |
| LIMIT_BB3S | 3/16 | 18.8% | -1.00% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.21% | **+1.92%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.67% | **+1.60%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.13% | **+1.25%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.64% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.76** / 初期 $100.00 (+135.76%)
- 確定: 2195件 (Win 657 / Loss 731 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $235.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.06** / 初期 $100.00 (+8.06%)
- 確定: 401件 (Win 109 / Loss 100 / Flat 192) / skip 680件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0525 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $108.06

## 5. Latest Market Context

- 更新: 2026-06-27T04:30:28.914636+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=60359.7
- Funnel: target 806 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +33.32% | $36,105,960.47 |
| MYX/USDT:USDT | +30.11% | $4,023,146.11 |
| PUNDIX/USDT:USDT | +28.53% | $5,435,967.89 |
| SLX/USDT:USDT | +15.68% | $10,931,118.56 |
| ARX/USDT:USDT | +14.25% | $2,656,844.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +1.96% | +1.82% |
| LAB/USDT:USDT | below_1h_threshold | +1.60% | +1.46% |
| SNT/USDT:USDT | below_1h_threshold | +1.51% | +1.36% |
| UB/USDT:USDT | below_1h_threshold | +1.28% | +1.14% |
| ICNT/USDT:USDT | below_1h_threshold | +1.26% | +1.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
