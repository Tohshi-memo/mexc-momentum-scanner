# Decision Report

- generated_at: 2026-09-09T06:36:17.194450+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14039**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14039, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +1.04% | **+0.83%** |
| LIMIT_BB3S | 3/15 | 20.0% | +3.52% | **+0.70%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.82% | **+0.70%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.99% | **+0.69%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.38% | **+0.69%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,007.05** / 初期 $100.00 (+907.05%)
- 確定: 5303件 (Win 1591 / Loss 1709 / Flat 2003) / skip 5297件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,007.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.12** / 初期 $100.00 (+90.12%)
- 確定: 2642件 (Win 727 / Loss 623 / Flat 1292) / skip 4808件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0081 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.81** / 初期 $100.00 (+17.81%)
- 確定: 2618件 (Win 764 / Loss 1000 / Flat 854) / pending 2件 / skip 2890件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.81

## 6. Latest Market Context

- 更新: 2026-09-09T06:36:06.832073+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=79195.6
- Funnel: target 1070 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +70.14% | $1,154,056.55 |
| RAY/USDT:USDT | +27.93% | $3,450,239.30 |
| OL/USDT:USDT | +21.19% | $2,156,648.09 |
| NIULAI/USDT:USDT | +20.71% | $1,440,160.59 |
| CNPY/USDT:USDT | +13.22% | $1,047,736.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOLV/USDT:USDT | below_1h_threshold | +4.53% | +4.16% |
| NIULAI/USDT:USDT | below_1h_threshold | +4.28% | +3.91% |
| BTR/USDT:USDT | below_1h_threshold | +3.73% | +3.36% |
| ARB/USDT:USDT | below_1h_threshold | +3.55% | +3.18% |
| JUP/USDT:USDT | below_1h_threshold | +3.47% | +3.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
