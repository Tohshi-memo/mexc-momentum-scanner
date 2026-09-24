# Decision Report

- generated_at: 2026-09-24T01:26:15.787944+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15455**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15455, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.54%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +4.30% | **+2.15%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.25% | **+1.79%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.97% | **+1.63%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +3.33% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5897件 (Win 1739 / Loss 1890 / Flat 2268) / skip 6119件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.39** / 初期 $100.00 (+152.39%)
- 確定: 3402件 (Win 938 / Loss 791 / Flat 1673) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0684 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $252.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.89** / 初期 $100.00 (+20.89%)
- 確定: 3145件 (Win 927 / Loss 1238 / Flat 980) / pending 2件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000267 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $120.89

## 6. Latest Market Context

- 更新: 2026-09-24T01:26:04.735581+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=84195.4
- Funnel: target 1061 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +39.86% | $1,643,568.05 |
| NIL/USDT:USDT | +36.72% | $14,831,852.99 |
| LSK/USDT:USDT | +14.60% | $4,606,637.87 |
| BTW/USDT:USDT | +12.89% | $4,070,415.15 |
| ZRO/USDT:USDT | +7.92% | $10,059,985.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.12% | +2.22% |
| RAY/USDT:USDT | below_1h_threshold | +1.21% | +1.31% |
| ZRO/USDT:USDT | below_1h_threshold | +1.02% | +1.12% |
| RENDER/USDT:USDT | below_1h_threshold | +0.92% | +1.02% |
| PYTH/USDT:USDT | below_1h_threshold | +0.55% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
