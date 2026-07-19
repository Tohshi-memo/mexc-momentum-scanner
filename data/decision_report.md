# Decision Report

- generated_at: 2026-07-19T23:46:14.786285+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9069**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.61% / filled 20/20。**
- 全期間 MARKET基準: n=9069, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.61% | **+2.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.61% | **+2.61%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_BB3S | 2/19 | 10.5% | +8.00% | **+0.84%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.05% | **+0.03%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.45% | **-0.05%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.14% | **-0.13%** |
| MARKET_LONG | 20/20 | 100.0% | -0.22% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$400.27** / 初期 $100.00 (+300.27%)
- 確定: 3131件 (Win 984 / Loss 1000 / Flat 1147) / skip 2499件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $400.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.74** / 初期 $100.00 (+25.74%)
- 確定: 1030件 (Win 266 / Loss 218 / Flat 546) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0914 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $125.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.87** / 初期 $100.00 (+0.87%)
- 確定: 269件 (Win 93 / Loss 131 / Flat 45) / pending 1件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $100.87

## 6. Latest Market Context

- 更新: 2026-07-19T23:46:08.017656+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64650.2
- Funnel: target 885 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +36.27% | $81,003,843.28 |
| ACE/USDT:USDT | +35.07% | $1,586,203.82 |
| PUMPFUN/USDT:USDT | +17.84% | $12,735,300.39 |
| B/USDT:USDT | +15.09% | $39,414,306.97 |
| PROM/USDT:USDT | +12.60% | $1,961,898.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +4.27% | +4.26% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.52% | +2.51% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +2.49% | +2.48% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.10% | +2.09% |
| PROM/USDT:USDT | below_1h_threshold | +1.72% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
