# Decision Report

- generated_at: 2026-09-21T10:51:37.494836+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15251**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15251, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/14 | 42.9% | +1.75% | **+0.75%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.56% | **+0.78%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.00% | **+0.65%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.23% | **+0.37%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.91% | **+0.36%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,174.95** / 初期 $100.00 (+1074.95%)
- 確定: 5742件 (Win 1710 / Loss 1846 / Flat 2186) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,174.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3313件 (Win 915 / Loss 765 / Flat 1633) / skip 5349件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0155 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.69** / 初期 $100.00 (+22.69%)
- 確定: 3029件 (Win 892 / Loss 1186 / Flat 951) / pending 6件 / skip 3690件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.69

## 6. Latest Market Context

- 更新: 2026-09-21T10:51:24.616090+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.54% price=84168.1
- Funnel: target 1050 → liquid 158 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.9 >= 65=1, 4h RSI 68.9 >= 65=1, 4h RSI 87.9 >= 65=1, 4h RSI 66.9 >= 65=1, 4h RSI 71.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +74.16% | $6,628,032.87 |
| PHA/USDT:USDT | +63.28% | $2,732,372.75 |
| NIL/USDT:USDT | +32.33% | $7,479,867.11 |
| PTB/USDT:USDT | +31.13% | $1,163,388.44 |
| SEI/USDT:USDT | +29.34% | $21,364,820.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.69% | +5.23% |
| ONDO/USDT:USDT | below_1h_threshold | +4.30% | +4.84% |
| ENA/USDT:USDT | below_1h_threshold | +3.43% | +3.97% |
| ZRO/USDT:USDT | below_1h_threshold | +3.15% | +3.69% |
| XLM/USDT:USDT | below_1h_threshold | +2.78% | +3.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
