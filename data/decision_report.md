# Decision Report

- generated_at: 2026-09-28T05:16:21.065733+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15691**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=15691, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.98% | **+1.68%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.76% | **+1.49%** |
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.40% | **+0.84%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.36% | **+0.35%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | -0.18% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5981件 (Win 1766 / Loss 1923 / Flat 2292) / skip 6271件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5568件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.60** / 初期 $100.00 (+19.60%)
- 確定: 3261件 (Win 951 / Loss 1282 / Flat 1028) / pending 2件 / skip 3898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000180 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JUP/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $119.60

## 6. Latest Market Context

- 更新: 2026-09-28T05:16:08.308439+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=83309.4
- Funnel: target 1069 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +42.90% | $262,127,616.78 |
| BATON/USDT:USDT | +23.96% | $1,255,295.58 |
| ONE/USDT:USDT | +18.88% | $4,636,854.91 |
| GRT/USDT:USDT | +15.16% | $10,078,798.11 |
| SEI/USDT:USDT | +11.22% | $41,312,199.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +1.18% | +1.34% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +1.03% | +1.19% |
| BTW/USDT:USDT | below_1h_threshold | +0.44% | +0.60% |
| GRASS/USDT:USDT | below_1h_threshold | +0.30% | +0.47% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.20% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
