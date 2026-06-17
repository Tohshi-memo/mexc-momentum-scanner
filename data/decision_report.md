# Decision Report

- generated_at: 2026-06-17T11:50:36.842744+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6928**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6928, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +2.37% | **+1.42%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.69% | **+1.08%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.08% | **+0.86%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$194.84** / 初期 $100.00 (+94.84%)
- 確定: 1801件 (Win 488 / Loss 567 / Flat 746) / skip 1688件
- 成長率目線: 平均log +0.000370 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $194.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.47** / 初期 $100.00 (+1.47%)
- 確定: 201件 (Win 47 / Loss 43 / Flat 111) / skip 138件
- 成長率目線: 平均log +0.000073 / 幾何平均 +0.007% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1426 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $101.47

## 5. Latest Market Context

- 更新: 2026-06-17T11:50:26.385600+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64801.2
- Funnel: target 786 → liquid 163 → pre 50 → checked 50 → surge 4 → strict 4
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +63.16% | $8,642,951.46 |
| HIGH/USDT:USDT | +34.81% | $3,264,320.33 |
| ID/USDT:USDT | +21.74% | $1,392,884.78 |
| BP/USDT:USDT | +20.15% | $1,024,620.45 |
| PLAY/USDT:USDT | +19.50% | $2,782,487.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.86% | +3.81% |
| PLAY/USDT:USDT | below_1h_threshold | +2.69% | +2.64% |
| XLM/USDT:USDT | below_1h_threshold | +2.33% | +2.28% |
| BSB/USDT:USDT | below_1h_threshold | +1.86% | +1.81% |
| CRV/USDT:USDT | below_1h_threshold | +1.71% | +1.67% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
