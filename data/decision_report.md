# Decision Report

- generated_at: 2026-09-23T06:51:36.571675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15404**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15404, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.48% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.10% | **+1.37%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.66% | **+1.24%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,181.50** / 初期 $100.00 (+1081.50%)
- 確定: 5877件 (Win 1734 / Loss 1883 / Flat 2260) / skip 6088件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $1,181.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.16** / 初期 $100.00 (+149.16%)
- 確定: 3358件 (Win 927 / Loss 783 / Flat 1648) / skip 5457件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $249.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.15** / 初期 $100.00 (+21.15%)
- 確定: 3131件 (Win 920 / Loss 1232 / Flat 979) / pending 5件 / skip 3749件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000130 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.15

## 6. Latest Market Context

- 更新: 2026-09-23T06:51:21.788476+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=86459.4
- Funnel: target 1061 → liquid 192 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.3 >= 65=1, 4h RSI 84.9 >= 65=1, 4h RSI 67.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +71.45% | $1,271,632.27 |
| LONGXIA/USDT:USDT | +51.04% | $1,568,176.03 |
| NIL/USDT:USDT | +29.51% | $7,849,173.69 |
| SAGA/USDT:USDT | +23.88% | $2,094,410.15 |
| ALLO/USDT:USDT | +19.07% | $2,729,185.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.67% | +3.66% |
| OP/USDT:USDT | below_1h_threshold | +3.12% | +3.11% |
| NIL/USDT:USDT | below_1h_threshold | +3.12% | +3.10% |
| SXT/USDT:USDT | below_1h_threshold | +2.77% | +2.75% |
| CHR/USDT:USDT | below_1h_threshold | +2.70% | +2.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
