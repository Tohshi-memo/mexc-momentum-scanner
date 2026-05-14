# Decision Report

- generated_at: 2026-05-14T17:43:15.998634+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4308**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4308, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +6.29% | **+1.26%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 4/12 | 33.3% | +2.12% | **+0.71%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.29** / 初期 $100.00 (+19.29%)
- 確定: 362件 (Win 95 / Loss 129 / Flat 138) / skip 507件
- 成長率目線: 平均log +0.000487 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $119.29

## 4. Latest Market Context

- 更新: 2026-05-14T17:43:12.486610+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=81572.1
- Funnel: target 759 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +17.63% | $2,289,749.06 |
| LAB/USDT:USDT | +9.64% | $129,341,961.19 |
| ONDSSTOCK/USDT:USDT | +6.82% | $1,267,957.37 |
| TROLLSOL/USDT:USDT | +4.82% | $2,331,546.58 |
| EIGEN/USDT:USDT | +3.93% | $1,623,291.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.06% | +3.38% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.09% | +2.42% |
| BB/USDT:USDT | below_1h_threshold | +2.07% | +2.40% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.41% | +1.74% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.12% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
