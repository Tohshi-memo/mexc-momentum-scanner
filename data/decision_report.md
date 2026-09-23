# Decision Report

- generated_at: 2026-09-23T06:06:39.081049+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15399**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15399, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.50% | **+0.25%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.12% | **+1.49%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.16% | **+1.30%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.58% | **+0.95%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,169.81** / 初期 $100.00 (+1069.81%)
- 確定: 5874件 (Win 1733 / Loss 1883 / Flat 2258) / skip 6086件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $1,169.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.25** / 初期 $100.00 (+149.25%)
- 確定: 3355件 (Win 927 / Loss 782 / Flat 1646) / skip 5455件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $249.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.15** / 初期 $100.00 (+21.15%)
- 確定: 3131件 (Win 920 / Loss 1232 / Flat 979) / pending 5件 / skip 3743件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000074 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.15

## 6. Latest Market Context

- 更新: 2026-09-23T06:06:27.621592+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=86500.0
- Funnel: target 1061 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +57.91% | $1,229,145.32 |
| LONGXIA/USDT:USDT | +47.48% | $1,342,925.19 |
| NIL/USDT:USDT | +35.10% | $7,307,241.91 |
| SAGA/USDT:USDT | +20.63% | $1,966,377.09 |
| ZAMA/USDT:USDT | +18.24% | $2,432,324.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BCH/USDT:USDT | below_1h_threshold | +2.96% | +2.90% |
| ZRO/USDT:USDT | below_1h_threshold | +1.54% | +1.48% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.53% | +1.47% |
| AR/USDT:USDT | below_1h_threshold | +1.44% | +1.38% |
| AAVE/USDT:USDT | below_1h_threshold | +1.37% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
