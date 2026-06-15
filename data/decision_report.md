# Decision Report

- generated_at: 2026-06-15T07:41:34.456117+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6759**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6759, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_BB3S | 3/15 | 20.0% | +1.17% | **+0.23%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.69% | **+0.17%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.54% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.93% | **+3.15%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.30% | **+1.72%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.80% | **+1.53%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.56% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.49** / 初期 $100.00 (+74.49%)
- 確定: 1632件 (Win 426 / Loss 505 / Flat 701) / skip 1688件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $174.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.88** / 初期 $100.00 (-1.12%)
- 確定: 126件 (Win 25 / Loss 21 / Flat 80) / skip 44件
- 成長率目線: 平均log -0.000089 / 幾何平均 -0.009% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $98.88

## 5. Latest Market Context

- 更新: 2026-06-15T07:41:29.728208+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=65712.3
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +88.28% | $3,824,146.76 |
| EVAA/USDT:USDT | +87.58% | $23,404,251.84 |
| CLO/USDT:USDT | +46.82% | $2,136,472.54 |
| GRASS/USDT:USDT | +26.59% | $1,915,038.14 |
| WLD/USDT:USDT | +18.28% | $110,464,310.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.13% | +3.23% |
| CLO/USDT:USDT | below_1h_threshold | +2.53% | +2.62% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.99% | +2.09% |
| ORDI/USDT:USDT | below_1h_threshold | +1.64% | +1.74% |
| NIL/USDT:USDT | below_1h_threshold | +1.31% | +1.41% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
