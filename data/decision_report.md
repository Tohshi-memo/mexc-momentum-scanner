# Decision Report

- generated_at: 2026-09-09T22:21:20.674697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14127**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.68% / filled 20/20。**
- 全期間 MARKET基準: n=14127, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.68% | **+3.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.68% | **+3.68%** |
| LIMIT_1PCT | 18/20 | 90.0% | +4.06% | **+3.66%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.42% | **+2.05%** |
| LIMIT_ATR | 12/20 | 60.0% | +3.08% | **+1.85%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.48% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.05% | **+1.03%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.73% | **-0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5375件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$194.75** / 初期 $100.00 (+94.75%)
- 確定: 2721件 (Win 746 / Loss 637 / Flat 1338) / skip 4817件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0979 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $194.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.33** / 初期 $100.00 (+18.33%)
- 確定: 2632件 (Win 770 / Loss 1007 / Flat 855) / pending 1件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000333 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.33

## 6. Latest Market Context

- 更新: 2026-09-09T22:21:07.061330+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=77951.8
- Funnel: target 1064 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IOST/USDT:USDT | +10.07% | $36,344,424.74 |
| CATE/USDT:USDT | +6.56% | $2,701,433.04 |
| KAS/USDT:USDT | +3.94% | $3,687,200.07 |
| MINA/USDT:USDT | +3.54% | $1,074,047.62 |
| SKHYSTOCK/USDT:USDT | +1.55% | $16,536,161.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MINA/USDT:USDT | below_1h_threshold | +2.11% | +2.30% |
| UAI/USDT:USDT | below_1h_threshold | +1.03% | +1.23% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +0.40% | +0.59% |
| SOXS/USDT:USDT | below_1h_threshold | +0.28% | +0.48% |
| STX/USDT:USDT | below_1h_threshold | +0.26% | +0.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
