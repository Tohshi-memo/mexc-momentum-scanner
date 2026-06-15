# Decision Report

- generated_at: 2026-06-15T16:45:17.435613+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6797**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6797, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.02% | **+0.36%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.66% | **+0.07%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.16% | **+0.76%** |
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| ASK_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | -0.19% | **-0.06%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | -0.13% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$176.09** / 初期 $100.00 (+76.09%)
- 確定: 1670件 (Win 435 / Loss 520 / Flat 715) / skip 1688件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEGA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account -0.16% 残高後 $176.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 53件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-15T16:45:10.218977+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=67129.2
- Funnel: target 772 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +10.37% | $41,472,693.78 |
| RAVE/USDT:USDT | +5.25% | $1,692,240.93 |
| ASTEROID/USDT:USDT | +4.22% | $6,066,367.77 |
| XLM/USDT:USDT | +3.09% | $59,625,393.47 |
| WLFI/USDT:USDT | +2.41% | $2,648,786.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +4.23% | +4.40% |
| XLM/USDT:USDT | below_1h_threshold | +3.09% | +3.27% |
| WLFI/USDT:USDT | below_1h_threshold | +2.42% | +2.59% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.24% | +2.42% |
| INJ/USDT:USDT | below_1h_threshold | +1.68% | +1.86% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
