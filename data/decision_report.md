# Decision Report

- generated_at: 2026-10-28T23:31:30.852661+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17739**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17739, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_BB3S | 5/20 | 25.0% | +3.28% | **+0.82%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.24% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.74% | **+0.55%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.84% | **+0.43%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.40% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,545.84** / 初期 $100.00 (+1445.84%)
- 確定: 6783件 (Win 1971 / Loss 2172 / Flat 2640) / skip 7517件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAN/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.06% 残高後 $1,545.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$358.88** / 初期 $100.00 (+258.88%)
- 確定: 4260件 (Win 1155 / Loss 970 / Flat 2135) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0193 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XAN/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.06% 残高後 $358.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5903件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T23:31:18.111527+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=81309.0
- Funnel: target 1083 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +16.00% | $1,973,237.46 |
| XPIN/USDT:USDT | +14.71% | $2,454,671.30 |
| AKE/USDT:USDT | +12.07% | $7,149,913.16 |
| LITESTOCK/USDT:USDT | +11.11% | $1,116,655.91 |
| Q/USDT:USDT | +10.48% | $29,902,714.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INIT/USDT:USDT | below_1h_threshold | +4.45% | +4.36% |
| APR/USDT:USDT | below_1h_threshold | +2.39% | +2.30% |
| SOXS/USDT:USDT | below_1h_threshold | +1.50% | +1.41% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.05% | +0.96% |
| AGT/USDT:USDT | below_1h_threshold | +0.95% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
