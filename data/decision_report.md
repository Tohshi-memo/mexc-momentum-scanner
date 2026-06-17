# Decision Report

- generated_at: 2026-06-17T18:10:11.705516+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6961**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6961, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/17 | 35.3% | +2.12% | **+0.75%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.81% | **+4.81%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.82% | **+1.28%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.07% | **+0.86%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1816件 (Win 496 / Loss 573 / Flat 747) / skip 1706件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NBISSTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.59% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.56** / 初期 $100.00 (+3.56%)
- 確定: 234件 (Win 62 / Loss 56 / Flat 116) / skip 138件
- 成長率目線: 平均log +0.000150 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0966 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $103.56

## 5. Latest Market Context

- 更新: 2026-06-17T18:10:07.485732+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.06% price=65363.1
- Funnel: target 790 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +16.78% | $1,366,563.41 |
| ESPORTS/USDT:USDT | +6.20% | $14,225,604.00 |
| TAC/USDT:USDT | +5.36% | $2,067,441.01 |
| BRETT/USDT:USDT | +5.27% | $1,049,644.23 |
| BR/USDT:USDT | +3.29% | $7,264,800.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RE/USDT:USDT | below_1h_threshold | +2.85% | +3.91% |
| BR/USDT:USDT | below_1h_threshold | +0.80% | +1.86% |
| HYPE/USDT:USDT | below_1h_threshold | +0.70% | +1.76% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.57% | +1.63% |
| ALLO/USDT:USDT | below_1h_threshold | +0.52% | +1.59% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
