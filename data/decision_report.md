# Decision Report

- generated_at: 2026-07-27T15:56:16.030833+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9635**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9635, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.51% | **-0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.67% | **+0.27%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.15% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.76% | **+1.24%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.99% | **+1.19%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.16% | **+1.08%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.85% | **+1.02%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.42% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$456.37** / 初期 $100.00 (+356.37%)
- 確定: 3426件 (Win 1085 / Loss 1116 / Flat 1225) / skip 2770件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $456.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1822件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0011 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.26** / 初期 $100.00 (+8.26%)
- 確定: 656件 (Win 216 / Loss 249 / Flat 191) / pending 5件 / skip 446件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000348 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.26

## 6. Latest Market Context

- 更新: 2026-07-27T15:56:09.447134+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=64578.5
- Funnel: target 902 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.4 >= 65=1, 4h RSI 67.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +49.33% | $46,131,690.17 |
| ON/USDT:USDT | +48.56% | $8,915,096.21 |
| BTW/USDT:USDT | +30.95% | $10,628,531.60 |
| BEAT/USDT:USDT | +25.24% | $29,757,608.74 |
| TAG/USDT:USDT | +23.50% | $2,448,106.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +3.75% | +3.88% |
| CELHSTOCK/USDT:USDT | below_1h_threshold | +2.48% | +2.61% |
| EVAA/USDT:USDT | below_1h_threshold | +2.04% | +2.17% |
| BEAT/USDT:USDT | below_1h_threshold | +1.86% | +1.99% |
| AAPU/USDT:USDT | below_1h_threshold | +1.65% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
