# Decision Report

- generated_at: 2026-09-23T07:16:29.235336+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15408**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15408, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.89% | **-0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.61% | **+1.57%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.06% | **+1.55%** |
| MARKET_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.03% | **+1.22%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.19% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,175.60** / 初期 $100.00 (+1075.60%)
- 確定: 5881件 (Win 1734 / Loss 1884 / Flat 2263) / skip 6088件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,175.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.19** / 初期 $100.00 (+149.19%)
- 確定: 3361件 (Win 928 / Loss 783 / Flat 1650) / skip 5458件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.01% 残高後 $249.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.94** / 初期 $100.00 (+20.94%)
- 確定: 3132件 (Win 920 / Loss 1233 / Flat 979) / pending 4件 / skip 3750件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000103 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $120.94

## 6. Latest Market Context

- 更新: 2026-09-23T07:16:18.328689+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=86354.6
- Funnel: target 1061 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +73.58% | $1,285,575.11 |
| LONGXIA/USDT:USDT | +44.41% | $1,701,203.11 |
| SAGA/USDT:USDT | +24.47% | $1,748,544.61 |
| NIL/USDT:USDT | +22.72% | $8,062,673.67 |
| ALLO/USDT:USDT | +19.39% | $2,728,512.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +3.34% | +3.42% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.16% | +2.24% |
| SXT/USDT:USDT | below_1h_threshold | +1.48% | +1.56% |
| MYX/USDT:USDT | below_1h_threshold | +1.33% | +1.41% |
| HNT/USDT:USDT | below_1h_threshold | +1.07% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
