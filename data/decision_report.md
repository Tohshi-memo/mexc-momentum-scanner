# Decision Report

- generated_at: 2026-06-27T19:01:30.908146+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7714**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7714, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +7.36% | **+0.74%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| ASK | 20/20 | 100.0% | -0.12% | **-0.12%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.46% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.76% | **+1.76%** |
| ASK_LONG | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.75% | **+0.49%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.37** / 初期 $100.00 (+138.37%)
- 確定: 2223件 (Win 667 / Loss 741 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: S/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $238.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.77** / 初期 $100.00 (+7.77%)
- 確定: 445件 (Win 119 / Loss 114 / Flat 212) / skip 680件
- 成長率目線: 平均log +0.000168 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0377 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: S/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.68% 残高後 $107.77

## 5. Latest Market Context

- 更新: 2026-06-27T19:01:26.348224+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=60550.4
- Funnel: target 806 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| S/USDT:USDT | +15.48% | $2,207,426.31 |
| SLX/USDT:USDT | +15.30% | $15,789,448.03 |
| RE/USDT:USDT | +8.51% | $5,846,983.31 |
| BAS/USDT:USDT | +8.03% | $1,751,911.42 |
| RAVE/USDT:USDT | +4.99% | $3,907,710.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +1.07% | +1.05% |
| S/USDT:USDT | below_1h_threshold | +0.98% | +0.96% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.54% | +0.52% |
| H/USDT:USDT | below_1h_threshold | +0.35% | +0.34% |
| BAS/USDT:USDT | below_1h_threshold | +0.32% | +0.30% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
