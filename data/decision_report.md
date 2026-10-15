# Decision Report

- generated_at: 2026-10-15T05:06:10.571338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16718**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.68% / filled 20/20。**
- 全期間 MARKET基準: n=16718, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.88% | **+1.69%** |
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.93% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +6.96% | **+5.22%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.61% | **+0.56%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 239件 (TP 89 / SL 143 / EXP 7)
- 最新: ARCSOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,299.52** / 初期 $100.00 (+1199.52%)
- 確定: 6300件 (Win 1847 / Loss 2018 / Flat 2435) / skip 6979件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZKSYNC/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $1,299.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.10** / 初期 $100.00 (+174.10%)
- 確定: 3673件 (Win 1023 / Loss 871 / Flat 1779) / skip 6456件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000145 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-15T05:06:01.038162+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=81583.5
- Funnel: target 1085 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARCSOL/USDT:USDT | +23.40% | $1,847,854.63 |
| ZKSYNC/USDT:USDT | +22.76% | $3,118,491.78 |
| ZEREBRO/USDT:USDT | +21.95% | $5,013,646.28 |
| NIL/USDT:USDT | +16.43% | $13,055,131.96 |
| 1000RATS/USDT:USDT | +14.28% | $3,546,076.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +1.13% | +1.10% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +0.82% | +0.80% |
| MUBARAK/USDT:USDT | below_1h_threshold | +0.78% | +0.75% |
| BSPSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.67% |
| MAGIC/USDT:USDT | below_1h_threshold | +0.49% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
