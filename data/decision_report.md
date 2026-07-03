# Decision Report

- generated_at: 2026-07-03T06:16:25.968887+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8137**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8137, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.78% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_BB3S | 2/19 | 10.5% | +2.75% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.98% | **+1.19%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.27% | **+1.15%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.55% | **+1.02%** |
| ASK_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.70% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$288.33** / 初期 $100.00 (+188.33%)
- 確定: 2458件 (Win 758 / Loss 820 / Flat 880) / skip 2240件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $288.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.89** / 初期 $100.00 (+6.89%)
- 確定: 591件 (Win 143 / Loss 139 / Flat 309) / skip 957件
- 成長率目線: 平均log +0.000113 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0096 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.89

## 5. Latest Market Context

- 更新: 2026-07-03T06:16:20.053712+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=61705.9
- Funnel: target 834 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +35.53% | $6,527,772.34 |
| NEX/USDT:USDT | +35.04% | $1,044,804.73 |
| ZKP/USDT:USDT | +29.09% | $2,890,109.99 |
| MAGMA/USDT:USDT | +21.28% | $6,310,686.95 |
| NOM/USDT:USDT | +20.95% | $2,594,489.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.22% | +4.17% |
| ALLO/USDT:USDT | below_1h_threshold | +3.80% | +3.75% |
| POPCAT/USDT:USDT | below_1h_threshold | +3.40% | +3.35% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.55% | +1.49% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.43% | +1.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
