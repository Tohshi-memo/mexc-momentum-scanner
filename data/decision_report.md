# Decision Report

- generated_at: 2026-09-23T07:36:38.521114+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15413**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15413, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +4.57% | **+1.37%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.62% | **+3.00%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.57% | **+1.96%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.27% | **+1.93%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.15% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,210.04** / 初期 $100.00 (+1110.04%)
- 確定: 5886件 (Win 1737 / Loss 1884 / Flat 2265) / skip 6088件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAKE/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.90% 残高後 $1,210.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.45** / 初期 $100.00 (+147.45%)
- 確定: 3365件 (Win 928 / Loss 785 / Flat 1652) / skip 5459件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.98** / 初期 $100.00 (+20.98%)
- 確定: 3133件 (Win 921 / Loss 1233 / Flat 979) / pending 3件 / skip 3754件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000159 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $120.98

## 6. Latest Market Context

- 更新: 2026-09-23T07:36:25.192491+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=86184.6
- Funnel: target 1061 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +167.02% | $1,397,691.06 |
| SHROOM/USDT:USDT | +78.83% | $1,302,793.43 |
| NIL/USDT:USDT | +27.40% | $8,201,372.25 |
| LONGXIA/USDT:USDT | +27.30% | $1,803,946.61 |
| SAGA/USDT:USDT | +24.07% | $1,779,407.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHROOM/USDT:USDT | below_1h_threshold | +3.56% | +3.84% |
| BR/USDT:USDT | below_1h_threshold | +3.26% | +3.54% |
| MYX/USDT:USDT | below_1h_threshold | +2.28% | +2.56% |
| NIL/USDT:USDT | below_1h_threshold | +1.28% | +1.56% |
| ON/USDT:USDT | below_1h_threshold | +0.98% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
