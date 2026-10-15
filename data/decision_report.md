# Decision Report

- generated_at: 2026-10-15T08:21:33.001117+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16728**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=16728, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.48% | **+2.35%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.35% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.35% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 239件 (TP 89 / SL 143 / EXP 7)
- 最新: ARCSOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,293.03** / 初期 $100.00 (+1193.03%)
- 確定: 6302件 (Win 1847 / Loss 2019 / Flat 2436) / skip 6987件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGIC/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,293.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.10** / 初期 $100.00 (+174.10%)
- 確定: 3673件 (Win 1023 / Loss 871 / Flat 1779) / skip 6466件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4888件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-15T08:21:17.297226+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=81199.5
- Funnel: target 1085 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUFFER/USDT:USDT | +72.90% | $1,112,417.63 |
| ARCSOL/USDT:USDT | +32.14% | $2,236,375.61 |
| NIL/USDT:USDT | +20.40% | $14,997,638.49 |
| ZKSYNC/USDT:USDT | +18.37% | $5,221,080.82 |
| ZEREBRO/USDT:USDT | +18.22% | $5,690,896.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZKSYNC/USDT:USDT | below_1h_threshold | +2.71% | +3.07% |
| STRK/USDT:USDT | below_1h_threshold | +2.69% | +3.05% |
| BAT/USDT:USDT | below_1h_threshold | +1.54% | +1.90% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.78% | +1.14% |
| CRV/USDT:USDT | below_1h_threshold | +0.78% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
