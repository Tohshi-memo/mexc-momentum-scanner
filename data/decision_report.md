# Decision Report

- generated_at: 2026-09-21T11:01:14.053318+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15253**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15253, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/13 | 53.8% | +1.56% | **+0.84%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.35% | **+0.21%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.19% | **+0.13%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.16% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.56% | **+0.78%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.00% | **+0.65%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.47% | **+0.42%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.23% | **+0.37%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +0.91% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,170.87** / 初期 $100.00 (+1070.87%)
- 確定: 5744件 (Win 1711 / Loss 1847 / Flat 2186) / skip 6070件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SEI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.15% 残高後 $1,170.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3313件 (Win 915 / Loss 765 / Flat 1633) / skip 5351件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0116 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.47** / 初期 $100.00 (+22.47%)
- 確定: 3030件 (Win 892 / Loss 1187 / Flat 951) / pending 5件 / skip 3691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000101 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.17% 残高後 $122.47

## 6. Latest Market Context

- 更新: 2026-09-21T11:01:04.426361+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=84384.7
- Funnel: target 1050 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +74.10% | $3,242,344.67 |
| ZETA/USDT:USDT | +71.23% | $6,719,197.87 |
| NIL/USDT:USDT | +33.25% | $7,489,198.18 |
| SEI/USDT:USDT | +32.01% | $20,826,034.55 |
| PTB/USDT:USDT | +31.65% | $1,165,428.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +0.74% | +0.76% |
| SEI/USDT:USDT | below_1h_threshold | +0.47% | +0.49% |
| KORU/USDT:USDT | below_1h_threshold | +0.42% | +0.44% |
| PHA/USDT:USDT | below_1h_threshold | +0.36% | +0.38% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.35% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
