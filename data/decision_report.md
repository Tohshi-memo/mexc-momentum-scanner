# Decision Report

- generated_at: 2026-05-31T04:45:12.995201+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5169**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5169, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.78% | **+0.56%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.84% | **+0.79%** |
| ASK_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.00% | **+0.70%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.65% | **+0.52%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 805件 (Win 184 / Loss 243 / Flat 378) / skip 925件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +6.32%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NFP/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T04:45:09.936288+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=74154.6
- Funnel: target 773 → liquid 127 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1, 4h RSI 89.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +33.16% | $10,313,225.73 |
| PUNDIX/USDT:USDT | +32.39% | $1,056,544.22 |
| TA/USDT:USDT | +19.86% | $2,341,317.07 |
| STG/USDT:USDT | +9.49% | $4,129,226.84 |
| BASED/USDT:USDT | +8.91% | $1,811,140.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.92% | +3.86% |
| RIVER/USDT:USDT | below_1h_threshold | +2.99% | +2.93% |
| UP/USDT:USDT | below_1h_threshold | +2.50% | +2.44% |
| PI/USDT:USDT | below_1h_threshold | +2.29% | +2.23% |
| LIT/USDT:USDT | below_1h_threshold | +1.96% | +1.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
