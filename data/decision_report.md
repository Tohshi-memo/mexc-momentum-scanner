# Decision Report

- generated_at: 2026-06-25T05:40:54.797347+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7528**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7528, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/15 | 13.3% | +1.52% | **+0.20%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT | 14/20 | 70.0% | -0.17% | **-0.12%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.67% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.15% | **+1.08%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.45% | **+0.86%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.91% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.56** / 初期 $100.00 (+122.56%)
- 確定: 2128件 (Win 629 / Loss 712 / Flat 787) / skip 1961件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $222.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 589件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T05:40:50.283458+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=61517.5
- Funnel: target 808 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=2, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +39.81% | $14,519,550.45 |
| KORU/USDT:USDT | +21.63% | $5,681,278.00 |
| H/USDT:USDT | +20.38% | $23,486,247.32 |
| MUSTOCK/USDT:USDT | +19.30% | $110,557,913.79 |
| RESOLV/USDT:USDT | +17.11% | $2,687,849.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_relative_strength | +5.28% | +4.96% |
| SLX/USDT:USDT | below_relative_strength | +5.24% | +4.92% |
| ORDI/USDT:USDT | below_1h_threshold | +3.48% | +3.16% |
| TIA/USDT:USDT | below_1h_threshold | +3.23% | +2.92% |
| GRASS/USDT:USDT | below_1h_threshold | +3.04% | +2.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
