# Decision Report

- generated_at: 2026-09-05T13:06:20.423375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13733**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13733, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 17/20 | 85.0% | +0.87% | **+0.74%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.42% | **+0.35%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

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
- 確定: 5039件 (Win 1518 / Loss 1647 / Flat 1874) / skip 5255件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $857.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.40** / 初期 $100.00 (+88.40%)
- 確定: 2478件 (Win 696 / Loss 587 / Flat 1195) / skip 4666件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0647 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $188.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.92** / 初期 $100.00 (+18.92%)
- 確定: 2358件 (Win 703 / Loss 901 / Flat 754) / pending 6件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.12% 残高後 $118.92

## 6. Latest Market Context

- 更新: 2026-09-05T13:06:10.540897+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=79671.6
- Funnel: target 1050 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +89.73% | $14,433,304.92 |
| 4/USDT:USDT | +61.75% | $20,746,129.07 |
| BASECAT/USDT:USDT | +44.59% | $1,795,054.08 |
| MARSCOIN/USDT:USDT | +42.39% | $8,464,630.45 |
| AKE/USDT:USDT | +39.16% | $17,626,041.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTER/USDT:USDT | below_1h_threshold | +2.07% | +2.06% |
| USELESS/USDT:USDT | below_1h_threshold | +1.01% | +1.00% |
| UAI/USDT:USDT | below_1h_threshold | +0.96% | +0.95% |
| BASECAT/USDT:USDT | below_1h_threshold | +0.73% | +0.72% |
| BULLA/USDT:USDT | below_1h_threshold | +0.71% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
