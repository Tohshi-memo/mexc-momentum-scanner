# Decision Report

- generated_at: 2026-06-27T20:24:53.002889+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7716**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7716, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.61% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.46% | **-0.16%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.72% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.16% | **+2.16%** |
| ASK_LONG | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.15% | **+1.39%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.37% | **+1.30%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.27% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.36** / 初期 $100.00 (+138.36%)
- 確定: 2225件 (Win 668 / Loss 742 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $238.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.34** / 初期 $100.00 (+8.34%)
- 確定: 447件 (Win 120 / Loss 114 / Flat 213) / skip 680件
- 成長率目線: 平均log +0.000179 / 幾何平均 +0.018% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0487 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $108.34

## 5. Latest Market Context

- 更新: 2026-06-27T20:24:48.386911+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=60243.8
- Funnel: target 806 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +14.02% | $17,231,654.42 |
| S/USDT:USDT | +12.26% | $3,531,018.11 |
| BAS/USDT:USDT | +7.65% | $1,882,250.01 |
| RAVE/USDT:USDT | +7.07% | $4,599,658.04 |
| BASED/USDT:USDT | +6.21% | $1,093,084.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +4.04% | +3.88% |
| LAB/USDT:USDT | below_1h_threshold | +2.70% | +2.54% |
| ARX/USDT:USDT | below_1h_threshold | +2.41% | +2.26% |
| M/USDT:USDT | below_1h_threshold | +2.05% | +1.90% |
| JTO/USDT:USDT | below_1h_threshold | +1.69% | +1.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
