# Decision Report

- generated_at: 2026-06-28T15:53:03.256466+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7762**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7762, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 7/20 | 35.0% | +4.82% | **+1.69%** |
| LIMIT_10PCT | 6/20 | 30.0% | +5.58% | **+1.67%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.14% | **+0.96%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.73% | **+0.96%** |
| LIMIT_BB3S | 10/15 | 66.7% | +0.86% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.94% | **+1.94%** |
| ASK_LONG | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.67% | **+0.67%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.82% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.10** / 初期 $100.00 (+160.10%)
- 確定: 2270件 (Win 694 / Loss 761 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUMPFUN/USDT:USDT `MARKET_LONG` EXPIRED account -0.18% 残高後 $260.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 718件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T15:52:57.204432+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=59971.8
- Funnel: target 805 → liquid 122 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.2 >= 65=1, 4h RSI 92.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MANTA/USDT:USDT | +88.28% | $9,617,729.73 |
| ACT/USDT:USDT | +56.55% | $10,271,353.05 |
| S/USDT:USDT | +33.00% | $10,018,581.59 |
| VELVET/USDT:USDT | +27.65% | $229,410,010.22 |
| O/USDT:USDT | +21.80% | $13,803,194.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.69% | +3.73% |
| O/USDT:USDT | below_1h_threshold | +3.22% | +3.26% |
| OPN/USDT:USDT | below_1h_threshold | +2.93% | +2.97% |
| S/USDT:USDT | below_1h_threshold | +2.75% | +2.79% |
| UB/USDT:USDT | below_1h_threshold | +2.46% | +2.50% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
