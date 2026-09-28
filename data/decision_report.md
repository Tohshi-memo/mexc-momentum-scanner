# Decision Report

- generated_at: 2026-09-28T06:01:17.530516+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15693**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=15693, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.10% | **+1.89%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.10% | **+1.79%** |
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.58% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.36% | **+0.35%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | -0.18% | **-0.18%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.39% | **-0.18%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5981件 (Win 1766 / Loss 1923 / Flat 2292) / skip 6273件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5570件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.39** / 初期 $100.00 (+19.39%)
- 確定: 3263件 (Win 951 / Loss 1283 / Flat 1029) / pending 2件 / skip 3898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.39

## 6. Latest Market Context

- 更新: 2026-09-28T06:01:09.619592+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=83126.5
- Funnel: target 1069 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +49.98% | $255,063,096.87 |
| ONE/USDT:USDT | +24.50% | $4,813,999.25 |
| BATON/USDT:USDT | +24.22% | $1,255,639.04 |
| GRT/USDT:USDT | +15.55% | $10,175,825.07 |
| BTW/USDT:USDT | +13.92% | $6,612,786.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.06% | +1.08% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +0.74% | +0.76% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +0.44% | +0.46% |
| SEI/USDT:USDT | below_1h_threshold | +0.39% | +0.41% |
| SAGA/USDT:USDT | below_1h_threshold | +0.38% | +0.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
