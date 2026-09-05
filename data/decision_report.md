# Decision Report

- generated_at: 2026-09-05T12:36:30.006999+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13731**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13731, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.32% | **+1.86%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.36% | **+1.18%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.12% | **+0.89%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.46** / 初期 $100.00 (+757.46%)
- 確定: 5037件 (Win 1518 / Loss 1647 / Flat 1872) / skip 5255件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $857.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.12** / 初期 $100.00 (+88.12%)
- 確定: 2476件 (Win 695 / Loss 587 / Flat 1194) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0642 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.78** / 初期 $100.00 (+18.78%)
- 確定: 2356件 (Win 702 / Loss 901 / Flat 753) / pending 4件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.78

## 6. Latest Market Context

- 更新: 2026-09-05T12:36:18.568117+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79648.4
- Funnel: target 1050 → liquid 153 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1, 4h RSI 66.1 >= 65=1, 4h RSI 79.8 >= 65=1, 4h RSI 76.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +86.21% | $14,144,570.72 |
| 4/USDT:USDT | +60.63% | $20,500,227.85 |
| AKE/USDT:USDT | +45.89% | $17,396,296.65 |
| BASECAT/USDT:USDT | +45.40% | $1,838,558.61 |
| MARSCOIN/USDT:USDT | +43.26% | $8,719,489.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTER/USDT:USDT | below_1h_threshold | +4.98% | +4.89% |
| 4/USDT:USDT | below_1h_threshold | +3.75% | +3.66% |
| DASH/USDT:USDT | below_1h_threshold | +2.84% | +2.75% |
| CAKE/USDT:USDT | below_1h_threshold | +2.30% | +2.21% |
| SUI/USDT:USDT | below_1h_threshold | +1.89% | +1.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
