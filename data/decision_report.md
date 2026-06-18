# Decision Report

- generated_at: 2026-06-18T03:09:22.916372+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6993**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6993, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.77% | **+0.31%** |
| LIMIT_10PCT | 5/20 | 25.0% | -0.22% | **-0.05%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.72% | **-0.21%** |
| LIMIT_5PCT | 9/20 | 45.0% | -1.02% | **-0.46%** |
| LIMIT_7PCT | 6/20 | 30.0% | -1.73% | **-0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.20% | **+3.20%** |
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.52% | **+1.64%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +2.00% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$209.85** / 初期 $100.00 (+109.85%)
- 確定: 1839件 (Win 508 / Loss 580 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HIGH/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $209.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.15** / 初期 $100.00 (+5.15%)
- 確定: 266件 (Win 73 / Loss 68 / Flat 125) / skip 138件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0866 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HIGH/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.15

## 5. Latest Market Context

- 更新: 2026-06-18T03:09:18.739485+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=64561.0
- Funnel: target 790 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +81.81% | $30,978,095.04 |
| O/USDT:USDT | +72.23% | $1,659,418.96 |
| SYN/USDT:USDT | +45.72% | $4,473,755.17 |
| UP/USDT:USDT | +22.61% | $2,957,592.81 |
| H/USDT:USDT | +17.48% | $36,666,158.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.89% | +5.03% |
| EVAA/USDT:USDT | below_1h_threshold | +2.16% | +2.30% |
| OPN/USDT:USDT | below_1h_threshold | +1.67% | +1.81% |
| STG/USDT:USDT | below_1h_threshold | +1.64% | +1.78% |
| PLAY/USDT:USDT | below_1h_threshold | +1.31% | +1.45% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
