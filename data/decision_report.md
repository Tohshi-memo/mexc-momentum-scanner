# Decision Report

- generated_at: 2026-06-25T08:51:09.945009+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7536**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7536, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.25% | **-0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_BB3S | 4/16 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.14% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.52% | **+1.89%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.84% | **+1.56%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.90% | **+1.43%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.30% | **+1.32%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.16% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 1965件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 597件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T08:51:04.961075+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=61761.5
- Funnel: target 807 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +37.86% | $16,045,415.50 |
| RESOLV/USDT:USDT | +19.84% | $3,056,873.08 |
| BAS/USDT:USDT | +17.27% | $8,078,920.05 |
| MUSTOCK/USDT:USDT | +17.01% | $123,278,908.30 |
| KORU/USDT:USDT | +16.98% | $5,527,054.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SEI/USDT:USDT | below_1h_threshold | +2.11% | +2.31% |
| MVLL/USDT:USDT | below_1h_threshold | +1.90% | +2.10% |
| SLX/USDT:USDT | below_1h_threshold | +1.82% | +2.03% |
| HEI/USDT:USDT | below_1h_threshold | +0.97% | +1.17% |
| BCH/USDT:USDT | below_1h_threshold | +0.72% | +0.92% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
