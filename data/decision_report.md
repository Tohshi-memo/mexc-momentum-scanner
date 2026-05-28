# Decision Report

- generated_at: 2026-05-28T18:08:39.059798+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4984**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4984, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-1.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.44% | **-1.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.38% | **+1.09%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.31% | **+0.81%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.61% | **+2.22%** |
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +2.22% | **+1.97%** |
| MARKET_LONG | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.10% | **+1.70%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.62% | **+1.70%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.69** / 初期 $100.00 (+28.69%)
- 確定: 719件 (Win 174 / Loss 221 / Flat 324) / skip 826件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XPL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.69

## 4. Latest Market Context

- 更新: 2026-05-28T18:08:33.529020+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=73639.4
- Funnel: target 773 → liquid 157 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.0 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +22.98% | $3,335,160.01 |
| ESPORTS/USDT:USDT | +16.82% | $8,083,091.15 |
| UB/USDT:USDT | +16.47% | $7,001,601.26 |
| XPL/USDT:USDT | +10.09% | $2,822,107.24 |
| XLM/USDT:USDT | +9.08% | $336,654,213.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +2.66% | +2.50% |
| ZEC/USDT:USDT | below_1h_threshold | +2.38% | +2.21% |
| JTO/USDT:USDT | below_1h_threshold | +2.17% | +2.01% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.06% | +1.90% |
| SWARMS/USDT:USDT | below_1h_threshold | +1.98% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
