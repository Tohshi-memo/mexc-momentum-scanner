# Decision Report

- generated_at: 2026-06-27T16:04:07.424283+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7702**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7702, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +5.45% | **+0.82%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_BB3S | 4/17 | 23.5% | +1.53% | **+0.36%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| ASK | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.53% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.52** / 初期 $100.00 (+132.52%)
- 確定: 2216件 (Win 662 / Loss 739 / Flat 815) / skip 2047件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $232.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.83** / 初期 $100.00 (+6.83%)
- 確定: 433件 (Win 116 / Loss 111 / Flat 206) / skip 680件
- 成長率目線: 平均log +0.000152 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0291 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGLD/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.83

## 5. Latest Market Context

- 更新: 2026-06-27T16:04:00.692914+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=60774.2
- Funnel: target 806 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +2.73% | $45,848,906.91 |
| VELVET/USDT:USDT | +2.69% | $176,899,194.99 |
| SHIB/USDT:USDT | +1.65% | $2,552,564.83 |
| M/USDT:USDT | +1.26% | $6,041,526.94 |
| RESOLV/USDT:USDT | +1.22% | $1,090,612.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.69% | +2.76% |
| VELVET/USDT:USDT | below_1h_threshold | +2.65% | +2.72% |
| RESOLV/USDT:USDT | below_1h_threshold | +1.99% | +2.07% |
| SHIB/USDT:USDT | below_1h_threshold | +1.75% | +1.82% |
| M/USDT:USDT | below_1h_threshold | +1.26% | +1.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
