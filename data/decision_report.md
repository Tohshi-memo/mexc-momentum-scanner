# Decision Report

- generated_at: 2026-05-17T18:18:30.839154+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4414**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4414, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.55% | **-0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/11 | 36.4% | +1.94% | **+0.71%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.14% | **+0.12%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.31% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.83% | **+1.28%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.77% | **+1.06%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.01% | **+0.76%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.97% | **+0.58%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.26** / 初期 $100.00 (+19.26%)
- 確定: 411件 (Win 106 / Loss 139 / Flat 166) / skip 564件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.26

## 4. Latest Market Context

- 更新: 2026-05-17T18:18:26.462800+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78081.8
- Funnel: target 760 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +20.46% | $1,185,363.75 |
| UB/USDT:USDT | +7.46% | $12,490,416.91 |
| BUILDONBOB/USDT:USDT | +6.86% | $1,013,630.91 |
| ASTEROID/USDT:USDT | +3.78% | $4,082,028.33 |
| SPACE/USDT:USDT | +2.68% | $1,212,976.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.20% | +3.15% |
| CHIP/USDT:USDT | below_1h_threshold | +1.60% | +1.55% |
| FIDA/USDT:USDT | below_1h_threshold | +1.38% | +1.33% |
| BEAT/USDT:USDT | below_1h_threshold | +1.13% | +1.08% |
| BUILDONBOB/USDT:USDT | below_1h_threshold | +0.97% | +0.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
