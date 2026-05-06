# Decision Report

- generated_at: 2026-05-06T15:02:29.248338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3474**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3474, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 7/20 | 35.0% | +6.29% | **+2.20%** |
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 8/20 | 40.0% | +3.39% | **+1.36%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.33% | **+1.16%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.90% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.17% | **+3.17%** |
| ASK_LONG | 20/20 | 100.0% | +2.78% | **+2.78%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.44% | **+1.59%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.66% | **+0.30%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.44% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 26件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T15:02:26.621192+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=81508.2
- Funnel: target 770 → liquid 195 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +149.28% | $4,318,494.52 |
| IO/USDT:USDT | +38.26% | $15,363,342.06 |
| LAB/USDT:USDT | +35.49% | $163,278,014.19 |
| ZEC/USDT:USDT | +34.32% | $750,690,567.94 |
| BILL/USDT:USDT | +32.38% | $5,951,324.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IO/USDT:USDT | below_1h_threshold | +1.94% | +1.90% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.91% | +0.87% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.90% | +0.86% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.58% | +0.54% |
| DASH/USDT:USDT | below_1h_threshold | +0.57% | +0.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
