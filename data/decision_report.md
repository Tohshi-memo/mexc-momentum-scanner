# Decision Report

- generated_at: 2026-07-04T13:55:07.793645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8268**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8268, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.19% | **+0.22%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.24% | **-0.17%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.53% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$328.60** / 初期 $100.00 (+228.60%)
- 確定: 2585件 (Win 817 / Loss 864 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $328.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1042件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T13:54:59.207779+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=62541.1
- Funnel: target 834 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +116.71% | $79,901,369.99 |
| ANSEM/USDT:USDT | +77.94% | $5,905,681.60 |
| TLM/USDT:USDT | +67.47% | $57,673,989.10 |
| HMSTR/USDT:USDT | +55.21% | $13,596,443.30 |
| BAS/USDT:USDT | +50.06% | $4,768,982.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +4.91% | +5.05% |
| TLM/USDT:USDT | below_1h_threshold | +3.57% | +3.71% |
| BEAT/USDT:USDT | below_1h_threshold | +2.28% | +2.43% |
| BAS/USDT:USDT | below_1h_threshold | +1.86% | +2.01% |
| BTW/USDT:USDT | below_1h_threshold | +1.35% | +1.50% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
