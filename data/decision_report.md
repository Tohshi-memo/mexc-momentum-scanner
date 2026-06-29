# Decision Report

- generated_at: 2026-06-29T12:52:17.611155+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7815**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7815, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.95% | **+0.39%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.64% | **+0.79%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$102.14** / 初期 $100.00 (+2.14%)
- 確定トレード: 42件 (TP 15 / SL 26 / EXP 1)
- 最新: G/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$264.57** / 初期 $100.00 (+164.57%)
- 確定: 2319件 (Win 707 / Loss 773 / Flat 839) / skip 2057件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BAS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $264.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 456件 (Win 120 / Loss 119 / Flat 217) / skip 770件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0216 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T12:52:12.937275+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=59779.3
- Funnel: target 810 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +152.86% | $25,041,903.37 |
| GWEI/USDT:USDT | +49.03% | $2,064,707.23 |
| RAVE/USDT:USDT | +34.09% | $43,955,538.45 |
| G/USDT:USDT | +24.72% | $2,664,076.55 |
| UB/USDT:USDT | +23.73% | $2,337,676.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +4.78% | +5.03% |
| TAC/USDT:USDT | below_1h_threshold | +4.49% | +4.74% |
| RAVE/USDT:USDT | below_1h_threshold | +4.31% | +4.56% |
| BAS/USDT:USDT | below_1h_threshold | +3.34% | +3.60% |
| ORDI/USDT:USDT | below_1h_threshold | +2.35% | +2.60% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
