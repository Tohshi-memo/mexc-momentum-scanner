# Decision Report

- generated_at: 2026-08-13T18:11:32.318836+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11466**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11466, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.55% | **+0.49%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.41% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +3.64% | **+3.64%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.65% | **+1.15%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.96% | **+1.08%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.73% | **+0.87%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.37% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$601.25** / 初期 $100.00 (+501.25%)
- 確定: 3981件 (Win 1240 / Loss 1305 / Flat 1436) / skip 4046件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.35% 残高後 $601.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.94** / 初期 $100.00 (+49.94%)
- 確定: 1650件 (Win 471 / Loss 397 / Flat 782) / skip 3227件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0301 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $149.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.38** / 初期 $100.00 (+16.38%)
- 確定: 1466件 (Win 432 / Loss 554 / Flat 480) / pending 4件 / skip 1473件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACU/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.38

## 6. Latest Market Context

- 更新: 2026-08-13T18:11:22.533738+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=63187.2
- Funnel: target 978 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +17.70% | $1,063,805.29 |
| ACU/USDT:USDT | +8.89% | $8,912,298.94 |
| US/USDT:USDT | +5.93% | $4,294,724.95 |
| DEXE/USDT:USDT | +5.38% | $1,145,188.67 |
| BLESS/USDT:USDT | +4.94% | $9,759,242.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACU/USDT:USDT | below_1h_threshold | +2.14% | +2.03% |
| DEXE/USDT:USDT | below_1h_threshold | +1.82% | +1.71% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.63% | +1.52% |
| PROM/USDT:USDT | below_1h_threshold | +1.33% | +1.22% |
| SNXX/USDT:USDT | below_1h_threshold | +1.31% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
