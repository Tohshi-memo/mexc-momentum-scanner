# Decision Report

- generated_at: 2026-06-28T15:08:34.468541+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7761**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7761, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 7/20 | 35.0% | +4.82% | **+1.69%** |
| LIMIT_10PCT | 6/20 | 30.0% | +5.58% | **+1.67%** |
| LIMIT_8PCT | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.20% | **+1.10%** |
| LIMIT_BB3S | 10/15 | 66.7% | +0.87% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| ASK_LONG | 20/20 | 100.0% | +2.38% | **+2.38%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.67% | **+0.67%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.82% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.57** / 初期 $100.00 (+160.57%)
- 確定: 2269件 (Win 694 / Loss 760 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANTA/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $260.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 717件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T15:08:27.628312+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=60044.5
- Funnel: target 805 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MANTA/USDT:USDT | +83.90% | $6,206,066.74 |
| ACT/USDT:USDT | +63.79% | $9,826,516.27 |
| S/USDT:USDT | +28.87% | $9,811,986.87 |
| VELVET/USDT:USDT | +24.46% | $223,118,202.39 |
| RAVE/USDT:USDT | +20.79% | $10,757,231.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MANTA/USDT:USDT | below_1h_threshold | +2.67% | +2.59% |
| O/USDT:USDT | below_1h_threshold | +1.60% | +1.52% |
| BILL/USDT:USDT | below_1h_threshold | +1.60% | +1.52% |
| UB/USDT:USDT | below_1h_threshold | +1.38% | +1.30% |
| BEAT/USDT:USDT | below_1h_threshold | +1.12% | +1.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
