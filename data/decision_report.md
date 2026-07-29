# Decision Report

- generated_at: 2026-07-29T00:02:11.118253+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9738**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9738, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.06% | **+0.05%** |
| LIMIT_BB3S | 9/19 | 47.4% | +0.06% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.55% | **+1.09%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.98% | **+0.59%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.54% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$507.15** / 初期 $100.00 (+407.15%)
- 確定: 3508件 (Win 1111 / Loss 1139 / Flat 1258) / skip 2791件
- 成長率目線: 平均log +0.000463 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZIL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $507.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1923件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1057 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.17** / 初期 $100.00 (+10.17%)
- 確定: 754件 (Win 244 / Loss 288 / Flat 222) / pending 6件 / skip 457件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000447 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZIL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.17

## 6. Latest Market Context

- 更新: 2026-07-29T00:01:41.418481+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=63965.0
- Funnel: target 904 → liquid 166 → pre 50 → checked 50 → surge 9 → strict 9
- Surge前reject: below_1h_threshold=41, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +23.45% | $47,651,265.72 |
| RIF/USDT:USDT | +20.22% | $3,430,991.89 |
| JIMOTHY/USDT:USDT | +16.37% | $1,293,673.36 |
| ZIL/USDT:USDT | +14.66% | $8,021,145.70 |
| BTW/USDT:USDT | +13.65% | $6,291,940.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TQQQ/USDT:USDT | below_1h_threshold | +3.53% | +3.44% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.47% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +2.08% | +1.98% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.30% | +1.21% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
