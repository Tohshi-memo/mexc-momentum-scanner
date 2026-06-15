# Decision Report

- generated_at: 2026-06-15T21:10:12.372290+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6812**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=6812, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +3.13% | **+1.72%** |
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.87% | **+0.72%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.66% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.95% | **+0.85%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.05% | **+0.84%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.01% | **-0.00%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.48% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$180.58** / 初期 $100.00 (+80.58%)
- 確定: 1685件 (Win 441 / Loss 526 / Flat 718) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $180.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 68件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-15T21:10:04.967333+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=66425.7
- Funnel: target 772 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +39.88% | $2,145,609.08 |
| HOME/USDT:USDT | +14.24% | $1,037,252.03 |
| XMR/USDT:USDT | +11.00% | $10,528,316.97 |
| SPCXSTOCK/USDT:USDT | +10.01% | $236,813,468.39 |
| EVAA/USDT:USDT | +9.66% | $43,232,374.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_1h_threshold | +2.28% | +2.38% |
| AKT/USDT:USDT | below_1h_threshold | +0.97% | +1.06% |
| ALLO/USDT:USDT | below_1h_threshold | +0.72% | +0.81% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.65% | +0.75% |
| BSB/USDT:USDT | below_1h_threshold | +0.52% | +0.62% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
