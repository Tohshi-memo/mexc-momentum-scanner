# Decision Report

- generated_at: 2026-08-18T19:51:26.639891+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11921**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11921, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.90% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.97% | **+0.34%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.33% | **+0.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.89% | **+1.44%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.37% | **+0.95%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.18% | **+0.95%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.67% | **+0.75%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.71% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.51** / 初期 $100.00 (+514.51%)
- 確定: 4210件 (Win 1295 / Loss 1375 / Flat 1540) / skip 4272件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.19% 残高後 $614.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1820件 (Win 502 / Loss 427 / Flat 891) / skip 3512件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0077 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.10** / 初期 $100.00 (+18.10%)
- 確定: 1723件 (Win 515 / Loss 657 / Flat 551) / pending 1件 / skip 1668件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000308 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.10

## 6. Latest Market Context

- 更新: 2026-08-18T19:51:17.773798+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=64636.7
- Funnel: target 993 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +8.02% | $18,788,304.15 |
| GPS/USDT:USDT | +4.40% | $21,550,283.34 |
| PRL/USDT:USDT | +2.75% | $4,521,829.94 |
| CAKE/USDT:USDT | +2.27% | $1,011,760.93 |
| CYS/USDT:USDT | +1.81% | $13,817,156.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +1.87% | +2.04% |
| CAP/USDT:USDT | below_1h_threshold | +1.74% | +1.91% |
| HEI/USDT:USDT | below_1h_threshold | +1.55% | +1.71% |
| CAKE/USDT:USDT | below_1h_threshold | +1.32% | +1.49% |
| CIENSTOCK/USDT:USDT | below_1h_threshold | +1.32% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
