# Decision Report

- generated_at: 2026-07-01T14:46:41.606966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7994**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7994, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.47% | **+0.65%** |
| LIMIT_8PCT | 2/20 | 10.0% | +6.03% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.01% | **+0.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.40% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| ASK_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$266.73** / 初期 $100.00 (+166.73%)
- 確定: 2392件 (Win 727 / Loss 791 / Flat 874) / skip 2163件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $266.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.42** / 初期 $100.00 (+6.42%)
- 確定: 513件 (Win 129 / Loss 123 / Flat 261) / skip 892件
- 成長率目線: 平均log +0.000121 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0313 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VVV/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $106.42

## 5. Latest Market Context

- 更新: 2026-07-01T14:46:31.557086+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=59488.9
- Funnel: target 825 → liquid 150 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +86.85% | $16,395,473.97 |
| M/USDT:USDT | +60.62% | $7,137,026.08 |
| BASED/USDT:USDT | +28.56% | $14,480,247.28 |
| ZBT/USDT:USDT | +25.81% | $3,093,097.99 |
| BAS/USDT:USDT | +25.11% | $5,188,469.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| METASTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.35% |
| RIF/USDT:USDT | below_1h_threshold | +2.13% | +2.09% |
| ZBT/USDT:USDT | below_1h_threshold | +2.03% | +1.98% |
| BCH/USDT:USDT | below_1h_threshold | +1.94% | +1.90% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.66% | +1.62% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
