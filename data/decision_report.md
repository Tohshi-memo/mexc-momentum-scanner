# Decision Report

- generated_at: 2026-05-28T18:18:26.615996+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4985**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4985, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.84% | **-0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.38% | **+1.09%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.76% | **+0.83%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.25% | **+2.02%** |
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +2.22% | **+1.97%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.51% | **+1.50%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.14% | **+1.50%** |
| MARKET_LONG | 20/20 | 100.0% | +1.45% | **+1.45%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.69** / 初期 $100.00 (+28.69%)
- 確定: 720件 (Win 174 / Loss 221 / Flat 325) / skip 826件
- 成長率目線: 平均log +0.000350 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.69

## 4. Latest Market Context

- 更新: 2026-05-28T18:18:21.507313+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=73645.5
- Funnel: target 773 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +25.02% | $3,602,724.81 |
| ESPORTS/USDT:USDT | +23.32% | $8,313,595.00 |
| SWARMS/USDT:USDT | +11.96% | $1,206,544.18 |
| XPL/USDT:USDT | +11.13% | $3,019,526.60 |
| AR/USDT:USDT | +9.56% | $1,872,992.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +2.90% | +2.73% |
| LIT/USDT:USDT | below_1h_threshold | +2.82% | +2.65% |
| GRASS/USDT:USDT | below_1h_threshold | +2.74% | +2.57% |
| ZEC/USDT:USDT | below_1h_threshold | +2.73% | +2.56% |
| AR/USDT:USDT | below_1h_threshold | +2.49% | +2.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
