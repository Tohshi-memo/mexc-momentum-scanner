# Decision Report

- generated_at: 2026-05-19T11:18:41.294732+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4468**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4468, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.90% | **+0.68%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.38% | **+0.17%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.45% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +3.17% | **+1.81%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.79% | **+1.43%** |
| MARKET_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.15% | **+0.63%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.12% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.57** / 初期 $100.00 (+24.57%)
- 確定: 465件 (Win 124 / Loss 159 / Flat 182) / skip 564件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $124.57

## 4. Latest Market Context

- 更新: 2026-05-19T11:18:38.738006+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=76976.2
- Funnel: target 764 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +39.25% | $11,075,557.89 |
| EDEN/USDT:USDT | +37.46% | $3,009,721.75 |
| PLAY/USDT:USDT | +29.28% | $4,538,572.88 |
| ONT/USDT:USDT | +15.99% | $1,549,683.26 |
| LIT/USDT:USDT | +9.63% | $1,436,759.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +1.63% | +1.67% |
| PROM/USDT:USDT | below_1h_threshold | +0.94% | +0.98% |
| CHZ/USDT:USDT | below_1h_threshold | +0.63% | +0.67% |
| ZEC/USDT:USDT | below_1h_threshold | +0.39% | +0.43% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.29% | +0.32% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
