# Decision Report

- generated_at: 2026-11-19T13:11:07.219437+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19196**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19196, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.46% | **+0.15%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.85% | **+3.51%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.46% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,701.50** / 初期 $100.00 (+1601.50%)
- 確定: 7380件 (Win 2119 / Loss 2375 / Flat 2886) / skip 8377件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,701.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.70** / 初期 $100.00 (+330.70%)
- 確定: 5023件 (Win 1335 / Loss 1087 / Flat 2601) / skip 7584件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7354件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T13:10:58.522702+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63866.7
- Funnel: target 1084 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BITO/USDT:USDT | +101.91% | $1,936,310.15 |
| NAORIS/USDT:USDT | +48.49% | $1,335,653.50 |
| IRYS/USDT:USDT | +33.73% | $10,688,522.53 |
| VELVET/USDT:USDT | +32.49% | $9,003,622.19 |
| EVAA/USDT:USDT | +19.92% | $14,274,239.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +3.27% | +3.24% |
| EVAA/USDT:USDT | below_1h_threshold | +2.89% | +2.86% |
| HUMA/USDT:USDT | below_1h_threshold | +2.63% | +2.60% |
| BTW/USDT:USDT | below_1h_threshold | +1.18% | +1.15% |
| RIVER/USDT:USDT | below_1h_threshold | +0.66% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
