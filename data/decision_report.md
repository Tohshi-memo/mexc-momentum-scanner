# Decision Report

- generated_at: 2026-06-19T21:10:18.098448+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7173**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7173, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.23% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.06% | **+0.74%** |
| ASK_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.06% | **+0.63%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.14% | **+0.63%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$227.11** / 初期 $100.00 (+127.11%)
- 確定: 1968件 (Win 571 / Loss 639 / Flat 758) / skip 1766件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $227.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 274件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T21:10:12.894645+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63178.7
- Funnel: target 795 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +26.54% | $9,519,394.43 |
| BLESS/USDT:USDT | +19.96% | $4,435,199.58 |
| MYX/USDT:USDT | +12.08% | $3,589,268.79 |
| BTW/USDT:USDT | +9.74% | $7,371,073.81 |
| BASED/USDT:USDT | +9.67% | $9,262,716.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.91% | +4.97% |
| BR/USDT:USDT | below_1h_threshold | +1.37% | +1.44% |
| H/USDT:USDT | below_1h_threshold | +1.24% | +1.31% |
| RIF/USDT:USDT | below_1h_threshold | +1.22% | +1.29% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.21% | +1.28% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
