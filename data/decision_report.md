# Decision Report

- generated_at: 2026-08-13T02:51:18.811110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11418**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11418, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +7.96% | **+0.80%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.04% | **+0.71%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.98% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.41% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.18% | **+2.07%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.56% | **+1.41%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.05** / 初期 $100.00 (+503.05%)
- 確定: 3950件 (Win 1232 / Loss 1292 / Flat 1426) / skip 4029件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $603.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.75** / 初期 $100.00 (+47.75%)
- 確定: 1606件 (Win 453 / Loss 377 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1223 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $147.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.30** / 初期 $100.00 (+15.30%)
- 確定: 1426件 (Win 418 / Loss 537 / Flat 471) / pending 4件 / skip 1459件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.30

## 6. Latest Market Context

- 更新: 2026-08-13T02:51:11.963969+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=63514.0
- Funnel: target 972 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +34.17% | $7,696,064.66 |
| APR/USDT:USDT | +30.11% | $13,713,675.77 |
| BTW/USDT:USDT | +20.28% | $22,639,638.16 |
| VELVET/USDT:USDT | +9.89% | $22,157,305.55 |
| BANK/USDT:USDT | +9.46% | $3,641,805.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.88% | +4.75% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +3.02% | +2.89% |
| BTW/USDT:USDT | below_1h_threshold | +2.43% | +2.29% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.00% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
