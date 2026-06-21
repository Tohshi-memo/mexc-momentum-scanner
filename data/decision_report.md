# Decision Report

- generated_at: 2026-06-21T17:23:35.357393+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7319**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.53% / filled 20/20。**
- 全期間 MARKET基準: n=7319, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |
| ASK | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.93% | **+0.79%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.89% | **+0.63%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.10% | **-0.07%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.27% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2030件 (Win 599 / Loss 668 / Flat 763) / skip 1850件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 419件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T17:23:29.678264+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64133.8
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STO/USDT:USDT | +30.74% | $1,058,101.60 |
| RESOLV/USDT:USDT | +6.35% | $13,312,134.07 |
| SLX/USDT:USDT | +4.21% | $1,014,625.12 |
| UAI/USDT:USDT | +4.21% | $1,500,508.08 |
| UB/USDT:USDT | +3.85% | $4,104,172.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EIGEN/USDT:USDT | below_1h_threshold | +3.66% | +3.64% |
| VELVET/USDT:USDT | below_1h_threshold | +2.87% | +2.85% |
| BLESS/USDT:USDT | below_1h_threshold | +2.78% | +2.76% |
| SLX/USDT:USDT | below_1h_threshold | +2.22% | +2.20% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.08% | +2.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
