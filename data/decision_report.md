# Decision Report

- generated_at: 2026-07-20T22:11:15.372631+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9131**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9131, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT | 16/20 | 80.0% | -0.09% | **-0.07%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -0.75% | **-0.11%** |
| LIMIT_BB3S | 2/14 | 14.3% | -0.79% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.26% | **+1.35%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.40% | **+1.26%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.73% | **+1.12%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.59% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$407.99** / 初期 $100.00 (+307.99%)
- 確定: 3193件 (Win 999 / Loss 1013 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $407.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$128.54** / 初期 $100.00 (+28.54%)
- 確定: 1092件 (Win 285 / Loss 221 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000230 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1301 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $128.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定: 329件 (Win 117 / Loss 143 / Flat 69) / pending 5件 / skip 270件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000368 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.99

## 6. Latest Market Context

- 更新: 2026-07-20T22:11:08.823928+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=65182.4
- Funnel: target 885 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +78.81% | $2,315,413.70 |
| HEMI/USDT:USDT | +23.56% | $2,423,893.00 |
| BLESS/USDT:USDT | +9.83% | $1,167,943.11 |
| MONAD/USDT:USDT | +7.13% | $1,362,029.94 |
| LDO/USDT:USDT | +6.95% | $4,757,479.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.62% | +3.74% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.54% | +2.66% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.00% | +2.12% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +1.21% | +1.33% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.19% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
