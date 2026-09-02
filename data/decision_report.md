# Decision Report

- generated_at: 2026-09-02T21:56:49.891309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13393**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13393, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.38% | **-2.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.65% | **+0.99%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.24% | **+0.49%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_BB3S | 6/15 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.06% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.74% | **+1.66%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.57% | **+1.10%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.68% | **+1.09%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$870.32** / 初期 $100.00 (+770.32%)
- 確定: 4994件 (Win 1514 / Loss 1638 / Flat 1842) / skip 4960件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $870.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2372件 (Win 671 / Loss 576 / Flat 1125) / skip 4432件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1229 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.56** / 初期 $100.00 (+14.56%)
- 確定: 2105件 (Win 614 / Loss 825 / Flat 666) / pending 6件 / skip 2760件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000429 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.56

## 6. Latest Market Context

- 更新: 2026-09-02T21:56:33.100744+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=77307.3
- Funnel: target 1044 → liquid 160 → pre 50 → checked 50 → surge 7 → strict 1
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1, 4h RSI 91.8 >= 65=1, 4h RSI 92.6 >= 65=1, 4h RSI 89.0 >= 65=1, 4h RSI n/a=1, 4h RSI 78.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +98.51% | $62,572,723.88 |
| BULLA/USDT:USDT | +24.88% | $3,376,631.38 |
| SNOWSTOCK/USDT:USDT | +21.51% | $1,318,246.02 |
| BONER/USDT:USDT | +21.04% | $2,350,053.60 |
| BTW/USDT:USDT | +19.11% | $9,892,566.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +3.99% | +4.06% |
| BTW/USDT:USDT | below_1h_threshold | +3.17% | +3.25% |
| CRV/USDT:USDT | below_1h_threshold | +2.69% | +2.76% |
| DASH/USDT:USDT | below_1h_threshold | +1.60% | +1.67% |
| KITE/USDT:USDT | below_1h_threshold | +1.38% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
