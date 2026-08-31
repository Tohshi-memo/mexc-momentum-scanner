# Decision Report

- generated_at: 2026-08-31T19:21:18.166406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13201**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13201, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.02% | **-0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.12% | **+0.08%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.07% | **+0.07%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.66% | **+1.60%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.35% | **+1.21%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.83% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 195件 (TP 73 / SL 117 / EXP 5)
- 最新: ARB/USDT:USDT SL_HIT PnL -2.46% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4877件 (Win 1485 / Loss 1609 / Flat 1783) / skip 4885件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.99** / 初期 $100.00 (+73.99%)
- 確定: 2192件 (Win 608 / Loss 528 / Flat 1056) / skip 4420件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 0件 / skip 2587件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000284 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-08-31T19:21:08.876058+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79009.7
- Funnel: target 1031 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +22.46% | $10,124,140.29 |
| DOGS/USDT:USDT | +11.77% | $2,370,370.17 |
| FONE/USDT:USDT | +11.01% | $1,203,549.57 |
| HEMI/USDT:USDT | +10.34% | $9,504,539.14 |
| 0G/USDT:USDT | +9.55% | $13,117,484.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +2.61% | +2.57% |
| RIVER/USDT:USDT | below_1h_threshold | +1.93% | +1.90% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.34% |
| SHEINSTOCK/USDT:USDT | below_1h_threshold | +0.95% | +0.92% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.62% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
