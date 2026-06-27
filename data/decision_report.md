# Decision Report

- generated_at: 2026-06-27T18:36:23.067331+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7713**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7713, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +7.36% | **+0.74%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.28% | **-0.11%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.14% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.43% | **+1.43%** |
| ASK_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.21% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.18** / 初期 $100.00 (+137.18%)
- 確定: 2222件 (Win 666 / Loss 741 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $237.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.04** / 初期 $100.00 (+7.04%)
- 確定: 444件 (Win 118 / Loss 114 / Flat 212) / skip 680件
- 成長率目線: 平均log +0.000153 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $107.04

## 5. Latest Market Context

- 更新: 2026-06-27T18:36:10.414544+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=60538.1
- Funnel: target 806 → liquid 127 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +16.37% | $15,288,898.57 |
| S/USDT:USDT | +12.75% | $1,681,084.70 |
| BAS/USDT:USDT | +6.92% | $1,745,436.44 |
| RE/USDT:USDT | +6.60% | $5,562,356.27 |
| ARX/USDT:USDT | +3.89% | $3,077,554.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +4.07% | +4.00% |
| S/USDT:USDT | below_1h_threshold | +2.57% | +2.50% |
| PI/USDT:USDT | below_1h_threshold | +1.68% | +1.61% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.61% | +1.54% |
| LAB/USDT:USDT | below_1h_threshold | +0.70% | +0.63% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
