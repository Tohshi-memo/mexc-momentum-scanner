# Decision Report

- generated_at: 2026-06-17T15:06:38.907948+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6952**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6952, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.15% | **+0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/15 | 26.7% | +4.18% | **+1.11%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.12% | **+1.27%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.97% | **+0.68%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.79% | **+0.67%** |
| ASK_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$196.04** / 初期 $100.00 (+96.04%)
- 確定: 1814件 (Win 494 / Loss 573 / Flat 747) / skip 1699件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTER/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $196.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.29** / 初期 $100.00 (+2.29%)
- 確定: 225件 (Win 57 / Loss 53 / Flat 115) / skip 138件
- 成長率目線: 平均log +0.000101 / 幾何平均 +0.010% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0763 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $102.29

## 5. Latest Market Context

- 更新: 2026-06-17T15:06:34.598444+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=65126.9
- Funnel: target 790 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +106.96% | $5,808,908.49 |
| ESPORTS/USDT:USDT | +46.23% | $12,939,021.84 |
| TAC/USDT:USDT | +36.99% | $1,276,844.21 |
| MAGMA/USDT:USDT | +31.06% | $1,020,669.65 |
| XPL/USDT:USDT | +26.24% | $12,273,731.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.27% | +3.19% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.60% | +2.51% |
| AGT/USDT:USDT | below_1h_threshold | +2.09% | +2.00% |
| WIF/USDT:USDT | below_1h_threshold | +2.07% | +1.99% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +1.00% | +0.92% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
