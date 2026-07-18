# Decision Report

- generated_at: 2026-07-18T17:46:16.841309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8966**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8966, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.89% | **+1.13%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.94% | **+0.78%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.19% | **+2.87%** |
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.18% | **+2.22%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.32% | **+2.16%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.89% | **+1.01%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2478件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$117.08** / 初期 $100.00 (+17.08%)
- 確定: 927件 (Win 228 / Loss 187 / Flat 512) / skip 1450件
- 成長率目線: 平均log +0.000170 / 幾何平均 +0.017% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1450 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.89** / 初期 $100.00 (-1.11%)
- 確定: 195件 (Win 61 / Loss 107 / Flat 27) / pending 1件 / skip 242件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000481 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.89

## 6. Latest Market Context

- 更新: 2026-07-18T17:46:07.079539+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=64413.4
- Funnel: target 885 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +61.09% | $19,621,943.42 |
| BANK/USDT:USDT | +39.34% | $16,786,952.89 |
| B/USDT:USDT | +9.39% | $26,272,701.00 |
| US/USDT:USDT | +5.61% | $4,598,092.78 |
| BILL/USDT:USDT | +5.56% | $3,477,088.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.00% | +2.79% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.71% | +2.50% |
| US/USDT:USDT | below_1h_threshold | +2.29% | +2.08% |
| TOSHI/USDT:USDT | below_1h_threshold | +1.83% | +1.62% |
| BILL/USDT:USDT | below_1h_threshold | +1.65% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
