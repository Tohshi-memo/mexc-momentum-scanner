# Decision Report

- generated_at: 2026-06-28T11:03:10.869448+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7742**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7742, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$247.98** / 初期 $100.00 (+147.98%)
- 確定: 2250件 (Win 683 / Loss 752 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACT/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $247.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 698件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T11:03:05.129041+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=60211.4
- Funnel: target 805 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACT/USDT:USDT | +41.44% | $2,439,111.65 |
| SIREN/USDT:USDT | +21.08% | $1,654,280.85 |
| O/USDT:USDT | +20.10% | $11,584,985.01 |
| BASED/USDT:USDT | +19.27% | $1,839,444.12 |
| S/USDT:USDT | +17.96% | $7,426,209.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.44% | +3.32% |
| ACT/USDT:USDT | below_1h_threshold | +2.35% | +2.23% |
| BEAT/USDT:USDT | below_1h_threshold | +1.33% | +1.21% |
| SIREN/USDT:USDT | below_1h_threshold | +1.20% | +1.07% |
| BASED/USDT:USDT | below_1h_threshold | +0.88% | +0.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
