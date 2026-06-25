# Decision Report

- generated_at: 2026-06-25T21:04:49.854052+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7585**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=7585, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| ASK | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.20% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.47% | **+0.24%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.07% | **+0.02%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.08% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$103.17** / 初期 $100.00 (+3.17%)
- 確定トレード: 40件 (TP 15 / SL 24 / EXP 1)
- 最新: DRAM/USDT:USDT EXPIRED PnL +1.79% 残高後 $103.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 2014件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 375件 (Win 103 / Loss 100 / Flat 172) / skip 621件
- 成長率目線: 平均log +0.000195 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0490 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-25T21:04:45.248122+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=59450.0
- Funnel: target 807 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +16.27% | $1,510,143.28 |
| IP/USDT:USDT | +10.29% | $2,082,242.58 |
| VVV/USDT:USDT | +8.50% | $3,438,777.28 |
| UB/USDT:USDT | +8.04% | $2,230,377.13 |
| XPL/USDT:USDT | +7.60% | $10,321,897.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +1.14% | +1.10% |
| SLX/USDT:USDT | below_1h_threshold | +0.90% | +0.87% |
| IDOL/USDT:USDT | below_1h_threshold | +0.74% | +0.71% |
| XPL/USDT:USDT | below_1h_threshold | +0.70% | +0.67% |
| BTW/USDT:USDT | below_1h_threshold | +0.37% | +0.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
