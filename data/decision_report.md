# Decision Report

- generated_at: 2026-07-19T05:01:15.609076+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8999**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8999, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.62% | **-0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.56% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.74% | **+2.05%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.02% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.62% | **+0.89%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$369.21** / 初期 $100.00 (+269.21%)
- 確定: 3061件 (Win 952 / Loss 977 / Flat 1132) / skip 2499件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $369.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$122.50** / 初期 $100.00 (+22.50%)
- 確定: 960件 (Win 242 / Loss 197 / Flat 521) / skip 1450件
- 成長率目線: 平均log +0.000211 / 幾何平均 +0.021% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2070 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FWDISTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.15% 残高後 $122.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.55** / 初期 $100.00 (-0.45%)
- 確定: 202件 (Win 65 / Loss 109 / Flat 28) / pending 5件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000609 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $99.55

## 6. Latest Market Context

- 更新: 2026-07-19T05:01:09.256637+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64709.5
- Funnel: target 885 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +126.64% | $37,778,222.71 |
| BANK/USDT:USDT | +42.09% | $17,783,374.03 |
| B/USDT:USDT | +29.46% | $35,966,162.56 |
| TLM/USDT:USDT | +16.69% | $3,160,776.06 |
| TAG/USDT:USDT | +15.67% | $1,154,527.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.98% | +0.96% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.73% | +0.71% |
| TAG/USDT:USDT | below_1h_threshold | +0.64% | +0.61% |
| BULLA/USDT:USDT | below_1h_threshold | +0.61% | +0.58% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.54% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
