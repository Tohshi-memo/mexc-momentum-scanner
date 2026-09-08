# Decision Report

- generated_at: 2026-09-08T10:06:28.623215+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13978**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=13978, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.62% | **+0.50%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.06% | **+0.32%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.22% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,016.37** / 初期 $100.00 (+916.37%)
- 確定: 5246件 (Win 1583 / Loss 1704 / Flat 1959) / skip 5293件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,016.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.10** / 初期 $100.00 (+89.10%)
- 確定: 2582件 (Win 720 / Loss 621 / Flat 1241) / skip 4807件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0725 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $189.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.10** / 初期 $100.00 (+22.10%)
- 確定: 2567件 (Win 754 / Loss 963 / Flat 850) / pending 4件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000222 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.10

## 6. Latest Market Context

- 更新: 2026-09-08T10:06:16.613497+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78699.9
- Funnel: target 1065 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +135.04% | $15,663,195.94 |
| BNCSTOCK/USDT:USDT | +43.95% | $1,569,826.31 |
| FORM/USDT:USDT | +27.24% | $3,730,045.84 |
| USELESS/USDT:USDT | +18.53% | $11,329,658.33 |
| BTR/USDT:USDT | +17.09% | $1,065,036.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +4.34% | +4.37% |
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +2.16% | +2.20% |
| USELESS/USDT:USDT | below_1h_threshold | +1.31% | +1.35% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.32% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
