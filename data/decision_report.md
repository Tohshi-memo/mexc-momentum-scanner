# Decision Report

- generated_at: 2026-06-26T19:01:43.566714+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7648**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7648, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.82% | **-1.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 5/12 | 41.7% | +1.05% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.08% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.86%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +1.28% | **+0.73%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +2.86% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$233.67** / 初期 $100.00 (+133.67%)
- 確定: 2173件 (Win 647 / Loss 720 / Flat 806) / skip 2036件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $233.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 383件 (Win 103 / Loss 100 / Flat 180) / skip 676件
- 成長率目線: 平均log +0.000191 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0181 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T19:01:38.981316+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=59611.0
- Funnel: target 806 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +15.24% | $1,527,049.80 |
| VELVET/USDT:USDT | +9.51% | $19,008,290.92 |
| JTO/USDT:USDT | +8.59% | $9,578,276.46 |
| ICNT/USDT:USDT | +7.07% | $3,454,065.70 |
| IDOL/USDT:USDT | +6.23% | $1,106,749.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +3.17% | +3.23% |
| VELVET/USDT:USDT | below_1h_threshold | +1.17% | +1.24% |
| BEAT/USDT:USDT | below_1h_threshold | +0.37% | +0.43% |
| TIA/USDT:USDT | below_1h_threshold | +0.37% | +0.43% |
| SYN/USDT:USDT | below_1h_threshold | +0.33% | +0.39% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
