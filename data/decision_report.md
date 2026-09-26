# Decision Report

- generated_at: 2026-09-26T21:01:24.697456+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15615**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=15615, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.21% | **+0.97%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.03% | **+0.81%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.47% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.16% | **+0.32%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.12% | **+0.06%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.35% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,252.10** / 初期 $100.00 (+1152.10%)
- 確定: 5976件 (Win 1766 / Loss 1921 / Flat 2289) / skip 6200件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,252.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5493件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0376 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.42** / 初期 $100.00 (+19.42%)
- 確定: 3198件 (Win 941 / Loss 1268 / Flat 989) / pending 6件 / skip 3884件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000225 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GALA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.42

## 6. Latest Market Context

- 更新: 2026-09-26T21:01:11.489554+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=83995.0
- Funnel: target 1070 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +9.31% | $4,159,132.36 |
| MARSCOIN/USDT:USDT | +9.05% | $1,708,655.83 |
| GRAM/USDT:USDT | +5.38% | $4,192,558.24 |
| LSK/USDT:USDT | +4.81% | $3,103,059.34 |
| QNT/USDT:USDT | +3.92% | $19,562,729.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +0.63% | +0.63% |
| KAS/USDT:USDT | below_1h_threshold | +0.33% | +0.33% |
| GRAM/USDT:USDT | below_1h_threshold | +0.19% | +0.19% |
| MUBARAK/USDT:USDT | below_1h_threshold | +0.15% | +0.16% |
| DASH/USDT:USDT | below_1h_threshold | +0.11% | +0.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
