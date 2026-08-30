# Decision Report

- generated_at: 2026-08-30T08:06:20.351171+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13036**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=13036, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.46% | **+0.44%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.14% | **+0.34%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_BB3S | 10/17 | 58.8% | +0.46% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$778.63** / 初期 $100.00 (+678.63%)
- 確定: 4806件 (Win 1463 / Loss 1583 / Flat 1760) / skip 4791件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $778.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.48** / 初期 $100.00 (+72.48%)
- 確定: 2120件 (Win 591 / Loss 517 / Flat 1012) / skip 4327件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0387 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $172.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 2078件 (Win 610 / Loss 807 / Flat 661) / pending 4件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000225 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-30T08:06:11.075793+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78109.9
- Funnel: target 1023 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +79.07% | $38,834,746.41 |
| PONS/USDT:USDT | +73.09% | $1,702,009.69 |
| NIULAI/USDT:USDT | +61.30% | $3,232,114.75 |
| FONE/USDT:USDT | +41.84% | $1,448,834.40 |
| PROM/USDT:USDT | +28.87% | $15,647,311.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +2.04% | +2.01% |
| HNT/USDT:USDT | below_1h_threshold | +0.83% | +0.79% |
| NIL/USDT:USDT | below_1h_threshold | +0.75% | +0.71% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.65% | +0.62% |
| FET/USDT:USDT | below_1h_threshold | +0.33% | +0.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
