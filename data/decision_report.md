# Decision Report

- generated_at: 2026-10-30T13:56:35.322785+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17849**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17849, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.69% | **+1.88%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.45% | **+1.84%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.51% | **+1.63%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.52% | **+1.37%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.56** / 初期 $100.00 (+1423.56%)
- 確定: 6806件 (Win 1975 / Loss 2181 / Flat 2650) / skip 7604件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,523.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$361.74** / 初期 $100.00 (+261.74%)
- 確定: 4355件 (Win 1170 / Loss 982 / Flat 2203) / skip 6905件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAMX/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $361.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6011件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T13:56:21.558493+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.86% price=76768.1
- Funnel: target 1090 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.0 >= 65=1, 4h RSI 79.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +51.99% | $9,856,240.07 |
| BEAMX/USDT:USDT | +51.26% | $1,302,338.04 |
| MAGMA/USDT:USDT | +31.09% | $1,555,117.46 |
| SOXS/USDT:USDT | +23.66% | $67,890,527.92 |
| IDOL/USDT:USDT | +20.79% | $3,288,023.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.38% | +4.24% |
| BR/USDT:USDT | below_1h_threshold | +1.69% | +2.55% |
| LSK/USDT:USDT | below_1h_threshold | +1.62% | +2.48% |
| NIL/USDT:USDT | below_1h_threshold | +1.37% | +2.23% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.92% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
