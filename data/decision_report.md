# Decision Report

- generated_at: 2026-06-03T04:47:58.592823+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5518**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5518, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| ASK | 20/20 | 100.0% | +0.13% | **+0.13%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.26% | **+0.12%** |
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.00% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.09% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1102件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-03T04:47:55.648018+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.95% price=66442.5
- Funnel: target 773 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.5 >= 65=1, 4h RSI 81.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +35.60% | $13,990,376.62 |
| CLO/USDT:USDT | +25.42% | $2,238,580.63 |
| APR/USDT:USDT | +23.16% | $1,205,047.68 |
| MRVLSTOCK/USDT:USDT | +19.61% | $18,220,293.74 |
| BBSTOCK/USDT:USDT | +19.04% | $1,914,175.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_relative_strength | +5.45% | +4.50% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.50% | +3.55% |
| EPIC/USDT:USDT | below_1h_threshold | +4.29% | +3.34% |
| GUA/USDT:USDT | below_1h_threshold | +4.20% | +3.25% |
| ENA/USDT:USDT | below_1h_threshold | +4.19% | +3.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
