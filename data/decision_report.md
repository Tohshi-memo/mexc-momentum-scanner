# Decision Report

- generated_at: 2026-05-22T17:27:34.698235+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4726**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4726, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +4.23% | **+1.06%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.46% | **+0.80%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.83% | **+0.71%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.98% | **+0.50%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.34% | **+0.74%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.51% | **+0.60%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.98% | **+0.44%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.21** / 初期 $100.00 (+23.21%)
- 確定: 572件 (Win 147 / Loss 187 / Flat 238) / skip 715件
- 成長率目線: 平均log +0.000365 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $123.21

## 4. Latest Market Context

- 更新: 2026-05-22T17:27:32.787072+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=76807.0
- Funnel: target 768 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +64.07% | $29,133,675.97 |
| GENIUS/USDT:USDT | +4.93% | $5,658,896.56 |
| GUA/USDT:USDT | +4.40% | $1,060,636.44 |
| INJ/USDT:USDT | +3.73% | $35,244,559.43 |
| PEAQ/USDT:USDT | +3.23% | $1,304,186.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +2.11% | +2.25% |
| GRASS/USDT:USDT | below_1h_threshold | +1.89% | +2.03% |
| AGT/USDT:USDT | below_1h_threshold | +1.82% | +1.96% |
| GUA/USDT:USDT | below_1h_threshold | +1.19% | +1.33% |
| PEAQ/USDT:USDT | below_1h_threshold | +0.75% | +0.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
