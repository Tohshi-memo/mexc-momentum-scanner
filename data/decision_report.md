# Decision Report

- generated_at: 2026-06-01T15:27:49.571033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5329**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5329, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 7/19 | 36.8% | -0.42% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.28% | **+0.77%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.79% | **+0.67%** |
| ASK_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.18% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 996件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T15:27:44.652517+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=71153.6
- Funnel: target 776 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +88.45% | $235,896,383.03 |
| SLX/USDT:USDT | +77.71% | $10,336,213.11 |
| H/USDT:USDT | +76.80% | $47,952,883.30 |
| HOME/USDT:USDT | +50.90% | $7,444,969.28 |
| PORTAL/USDT:USDT | +36.92% | $42,164,887.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.26% | +4.81% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.59% | +4.14% |
| CTR/USDT:USDT | below_1h_threshold | +2.69% | +3.24% |
| BILL/USDT:USDT | below_1h_threshold | +2.53% | +3.08% |
| STG/USDT:USDT | below_1h_threshold | +2.42% | +2.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
