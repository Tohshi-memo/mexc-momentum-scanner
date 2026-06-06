# Decision Report

- generated_at: 2026-06-06T19:53:01.036468+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5894**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5894, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +6.33% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.26% | **+3.50%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +5.00% | **+2.00%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +5.00% | **+2.00%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.61% | **+1.44%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$136.55** / 初期 $100.00 (+36.55%)
- 確定: 1027件 (Win 246 / Loss 315 / Flat 466) / skip 1428件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $136.55

## 4. Latest Market Context

- 更新: 2026-06-06T19:52:54.615061+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=60570.1
- Funnel: target 771 → liquid 135 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=1, 4h RSI 85.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +36.29% | $48,348,793.70 |
| SKYAI/USDT:USDT | +31.34% | $15,196,194.71 |
| FIDA/USDT:USDT | +26.76% | $1,614,122.60 |
| BTW/USDT:USDT | +25.89% | $17,798,998.07 |
| BLUAI/USDT:USDT | +9.18% | $7,203,390.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.56% | +4.62% |
| BABY/USDT:USDT | below_1h_threshold | +2.22% | +2.28% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.51% | +1.57% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +1.44% | +1.50% |
| LUNC/USDT:USDT | below_1h_threshold | +1.38% | +1.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
