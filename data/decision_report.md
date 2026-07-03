# Decision Report

- generated_at: 2026-07-03T08:10:58.737511+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8144**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8144, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.99% | **+1.99%** |
| MARKET_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.44% | **+1.01%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.49% | **+0.97%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.54% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.03** / 初期 $100.00 (+184.03%)
- 確定: 2465件 (Win 758 / Loss 823 / Flat 884) / skip 2240件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $284.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.22** / 初期 $100.00 (+6.22%)
- 確定: 596件 (Win 143 / Loss 141 / Flat 312) / skip 959件
- 成長率目線: 平均log +0.000101 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0290 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.29% 残高後 $106.22

## 5. Latest Market Context

- 更新: 2026-07-03T08:10:52.753161+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=61750.9
- Funnel: target 834 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +38.74% | $7,407,484.14 |
| NEX/USDT:USDT | +34.28% | $1,386,197.49 |
| ZKP/USDT:USDT | +26.19% | $3,610,539.43 |
| THE/USDT:USDT | +23.74% | $2,331,119.84 |
| GUA/USDT:USDT | +20.40% | $8,766,374.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| THE/USDT:USDT | below_1h_threshold | +4.92% | +4.89% |
| MERL/USDT:USDT | below_1h_threshold | +2.41% | +2.38% |
| RPL/USDT:USDT | below_1h_threshold | +2.39% | +2.36% |
| S/USDT:USDT | below_1h_threshold | +2.09% | +2.06% |
| RIF/USDT:USDT | below_1h_threshold | +1.94% | +1.91% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
