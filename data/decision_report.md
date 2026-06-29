# Decision Report

- generated_at: 2026-06-29T07:05:35.720066+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7796**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7796, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.65% | **-0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.62% | **+0.16%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +0.01% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.54% | **+1.07%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.01% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.43% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$258.12** / 初期 $100.00 (+158.12%)
- 確定: 2300件 (Win 698 / Loss 766 / Flat 836) / skip 2057件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $258.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 456件 (Win 120 / Loss 119 / Flat 217) / skip 751件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0194 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T07:05:28.828561+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=59989.7
- Funnel: target 806 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +63.41% | $23,467,323.94 |
| G/USDT:USDT | +17.45% | $1,687,945.89 |
| SLX/USDT:USDT | +16.88% | $11,208,955.29 |
| HIGH/USDT:USDT | +15.54% | $1,586,753.94 |
| UB/USDT:USDT | +12.56% | $1,236,976.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACT/USDT:USDT | below_1h_threshold | +2.90% | +3.00% |
| SYN/USDT:USDT | below_1h_threshold | +1.19% | +1.29% |
| H/USDT:USDT | below_1h_threshold | +1.11% | +1.21% |
| POWR/USDT:USDT | below_1h_threshold | +1.07% | +1.17% |
| BAS/USDT:USDT | below_1h_threshold | +0.97% | +1.07% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
