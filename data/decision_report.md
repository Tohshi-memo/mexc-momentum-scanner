# Decision Report

- generated_at: 2026-06-28T06:45:08.235832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7731**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7731, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.78% | **+1.16%** |
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |
| ASK | 20/20 | 100.0% | -0.05% | **-0.05%** |
| LIMIT_5PCT | 7/20 | 35.0% | -1.17% | **-0.41%** |
| LIMIT_6PCT | 5/20 | 25.0% | -1.65% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| ASK_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.15% | **-0.02%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$243.11** / 初期 $100.00 (+143.11%)
- 確定: 2239件 (Win 676 / Loss 748 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $243.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 687件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T06:45:00.202742+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=59948.8
- Funnel: target 805 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +34.13% | $4,119,948.90 |
| BAS/USDT:USDT | +25.99% | $3,685,466.80 |
| LAB/USDT:USDT | +18.18% | $38,614,079.46 |
| ACT/USDT:USDT | +17.60% | $1,423,790.78 |
| S/USDT:USDT | +15.77% | $5,419,710.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +4.97% | +4.98% |
| BAS/USDT:USDT | below_1h_threshold | +4.88% | +4.89% |
| LAB/USDT:USDT | below_1h_threshold | +3.95% | +3.96% |
| BASED/USDT:USDT | below_1h_threshold | +2.01% | +2.03% |
| SLX/USDT:USDT | below_1h_threshold | +1.71% | +1.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
