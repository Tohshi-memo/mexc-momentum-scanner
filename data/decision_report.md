# Decision Report

- generated_at: 2026-06-10T01:36:08.301591+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6174**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6174, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.27% | **+1.28%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| ASK | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.47% | **+0.31%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.41% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.27** / 初期 $100.00 (+47.27%)
- 確定: 1192件 (Win 297 / Loss 375 / Flat 520) / skip 1543件
- 成長率目線: 平均log +0.000325 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $147.27

## 4. Latest Market Context

- 更新: 2026-06-10T01:36:04.994059+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=61859.3
- Funnel: target 778 → liquid 150 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1, 4h RSI 77.9 >= 65=1, 4h RSI 79.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +81.95% | $14,785,354.35 |
| STG/USDT:USDT | +32.81% | $3,421,139.71 |
| HOME/USDT:USDT | +15.02% | $4,422,784.36 |
| UB/USDT:USDT | +12.53% | $1,447,762.38 |
| SENT/USDT:USDT | +10.24% | $1,674,688.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +2.90% | +2.94% |
| LIT/USDT:USDT | below_1h_threshold | +2.30% | +2.35% |
| ZEST/USDT:USDT | below_1h_threshold | +2.15% | +2.19% |
| BEAT/USDT:USDT | below_1h_threshold | +1.70% | +1.74% |
| IO/USDT:USDT | below_1h_threshold | +1.23% | +1.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
