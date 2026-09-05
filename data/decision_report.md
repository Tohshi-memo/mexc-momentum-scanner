# Decision Report

- generated_at: 2026-09-05T13:11:29.461513+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13734**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13734, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 17/20 | 85.0% | +0.79% | **+0.67%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.50% | **+0.42%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.38% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.75% | **+2.06%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.37% | **+1.68%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.26% | **+1.47%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.00% | **+1.35%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.94% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.46** / 初期 $100.00 (+757.46%)
- 確定: 5040件 (Win 1518 / Loss 1647 / Flat 1875) / skip 5255件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTER/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $857.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.40** / 初期 $100.00 (+88.40%)
- 確定: 2479件 (Win 696 / Loss 587 / Flat 1196) / skip 4666件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0647 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTER/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.92** / 初期 $100.00 (+18.92%)
- 確定: 2359件 (Win 703 / Loss 901 / Flat 755) / pending 5件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ASTER/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.92

## 6. Latest Market Context

- 更新: 2026-09-05T13:11:18.751966+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=79634.9
- Funnel: target 1050 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +87.52% | $14,528,022.37 |
| 4/USDT:USDT | +62.19% | $20,796,247.31 |
| MARSCOIN/USDT:USDT | +43.07% | $8,487,991.78 |
| BASECAT/USDT:USDT | +42.48% | $1,797,764.99 |
| AKE/USDT:USDT | +41.28% | $17,726,886.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTER/USDT:USDT | below_1h_threshold | +4.10% | +4.14% |
| CAKE/USDT:USDT | below_1h_threshold | +1.44% | +1.48% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.71% | +0.75% |
| FILECOIN/USDT:USDT | below_1h_threshold | +0.62% | +0.66% |
| UAI/USDT:USDT | below_1h_threshold | +0.54% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
