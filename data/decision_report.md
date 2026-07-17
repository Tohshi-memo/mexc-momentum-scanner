# Decision Report

- generated_at: 2026-07-17T11:46:26.211794+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8843**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8843, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +3.64% | **+1.12%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.20% | **+1.10%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.67% | **+0.75%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.10% | **+1.47%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.75% | **+1.40%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.88% | **+0.75%** |
| MARKET_LONG | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.30% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$111.81** / 初期 $100.00 (+11.81%)
- 確定トレード: 111件 (TP 42 / SL 65 / EXP 4)
- 最新: DODO/USDT:USDT TP_HIT PnL +8.00% 残高後 $111.81
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$344.87** / 初期 $100.00 (+244.87%)
- 確定: 2958件 (Win 923 / Loss 947 / Flat 1088) / skip 2446件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LRC/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $344.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.49** / 初期 $100.00 (+8.49%)
- 確定: 805件 (Win 190 / Loss 171 / Flat 444) / skip 1449件
- 成長率目線: 平均log +0.000101 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0462 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $108.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.20** / 初期 $100.00 (-1.80%)
- 確定: 110件 (Win 34 / Loss 70 / Flat 6) / pending 4件 / skip 201件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.20

## 6. Latest Market Context

- 更新: 2026-07-17T11:46:17.463526+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=63305.2
- Funnel: target 885 → liquid 179 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.6 >= 65=1, 4h RSI 78.2 >= 65=1, 4h RSI 94.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +41.97% | $8,746,315.20 |
| LRC/USDT:USDT | +26.05% | $1,894,876.65 |
| XEC/USDT:USDT | +25.05% | $1,652,396.27 |
| BULLA/USDT:USDT | +24.87% | $1,058,569.09 |
| AKE/USDT:USDT | +20.67% | $41,084,539.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.30% | +3.05% |
| DEXE/USDT:USDT | below_1h_threshold | +2.61% | +2.36% |
| VELVET/USDT:USDT | below_1h_threshold | +1.59% | +1.33% |
| TAC/USDT:USDT | below_1h_threshold | +1.45% | +1.20% |
| ENS/USDT:USDT | below_1h_threshold | +1.37% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
