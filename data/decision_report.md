# Decision Report

- generated_at: 2026-07-02T02:17:54.349773+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8040**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8040, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 6/20 | 30.0% | +1.15% | **+0.35%** |
| LIMIT_9PCT | 6/20 | 30.0% | +0.86% | **+0.26%** |
| LIMIT_6PCT | 9/20 | 45.0% | -0.68% | **-0.31%** |
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |
| LIMIT_8PCT | 7/20 | 35.0% | -1.19% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.17% | **+1.41%** |
| ASK_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$289.00** / 初期 $100.00 (+189.00%)
- 確定: 2437件 (Win 752 / Loss 811 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $289.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.51** / 初期 $100.00 (+5.51%)
- 確定: 544件 (Win 136 / Loss 130 / Flat 278) / skip 907件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.19%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.51

## 5. Latest Market Context

- 更新: 2026-07-02T02:17:49.416126+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=60179.6
- Funnel: target 825 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +249.68% | $72,715,506.78 |
| TLM/USDT:USDT | +38.20% | $7,366,832.45 |
| RIF/USDT:USDT | +24.99% | $3,472,788.56 |
| SLX/USDT:USDT | +18.85% | $8,323,198.21 |
| LIT/USDT:USDT | +18.15% | $10,361,650.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +2.49% | +2.44% |
| RIF/USDT:USDT | below_1h_threshold | +2.46% | +2.41% |
| M/USDT:USDT | below_1h_threshold | +1.94% | +1.89% |
| LAB/USDT:USDT | below_1h_threshold | +1.47% | +1.42% |
| UB/USDT:USDT | below_1h_threshold | +1.43% | +1.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
