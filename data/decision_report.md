# Decision Report

- generated_at: 2026-07-20T13:41:26.677959+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9112**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9112, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_BB3S | 6/14 | 42.9% | +0.51% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +7.03% | **+3.51%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.84% | **+1.57%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.58% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$405.95** / 初期 $100.00 (+305.95%)
- 確定: 3174件 (Win 992 / Loss 1006 / Flat 1176) / skip 2499件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $405.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.06** / 初期 $100.00 (+27.06%)
- 確定: 1073件 (Win 280 / Loss 219 / Flat 574) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0728 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $127.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.87** / 初期 $100.00 (+1.87%)
- 確定: 311件 (Win 107 / Loss 135 / Flat 69) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000264 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.87

## 6. Latest Market Context

- 更新: 2026-07-20T13:41:17.771633+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=64624.8
- Funnel: target 887 → liquid 151 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.9 >= 65=1, 4h RSI 74.1 >= 65=1, 4h RSI 68.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +78.94% | $25,511,368.13 |
| BANK/USDT:USDT | +70.22% | $123,708,171.81 |
| PROM/USDT:USDT | +60.14% | $5,540,156.51 |
| EVAA/USDT:USDT | +22.62% | $7,863,517.20 |
| ANSEM/USDT:USDT | +16.29% | $2,375,749.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.43% | +4.43% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.11% | +3.12% |
| CHZ/USDT:USDT | below_1h_threshold | +1.84% | +1.84% |
| PI/USDT:USDT | below_1h_threshold | +1.61% | +1.61% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.33% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
