# Decision Report

- generated_at: 2026-06-15T21:28:46.120374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6814**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=6814, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +3.23% | **+1.61%** |
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.88% | **+0.58%** |
| ASK | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.38% | **+1.04%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.13% | **+0.96%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.13% | **+0.74%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.43% | **+0.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.01% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$103.53** / 初期 $100.00 (+3.53%)
- 確定トレード: 8件 (TP 5 / SL 3 / EXP 0)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.53
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$181.96** / 初期 $100.00 (+81.96%)
- 確定: 1687件 (Win 442 / Loss 526 / Flat 719) / skip 1688件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $181.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 70件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-15T21:28:40.848673+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=66397.1
- Funnel: target 772 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +34.92% | $2,267,702.64 |
| HOME/USDT:USDT | +14.36% | $1,070,760.92 |
| EVAA/USDT:USDT | +11.63% | $43,627,360.49 |
| SPCXSTOCK/USDT:USDT | +10.61% | $243,391,620.93 |
| FOLKS/USDT:USDT | +9.96% | $2,253,535.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKT/USDT:USDT | below_1h_threshold | +2.30% | +2.44% |
| AERO/USDT:USDT | below_1h_threshold | +2.11% | +2.25% |
| PLAY/USDT:USDT | below_1h_threshold | +1.47% | +1.61% |
| BABY/USDT:USDT | below_1h_threshold | +1.01% | +1.15% |
| CRV/USDT:USDT | below_1h_threshold | +0.96% | +1.10% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
