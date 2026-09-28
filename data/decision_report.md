# Decision Report

- generated_at: 2026-09-28T08:06:31.396748+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15702**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.94% / filled 20/20。**
- 全期間 MARKET基準: n=15702, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.55% | **+1.32%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.88% | **+0.48%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.52% | **+0.36%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.05% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.44% | **+0.52%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.90% | **+0.41%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.20% | **+0.05%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.38% | **-0.17%** |
| MARKET_LONG | 20/20 | 100.0% | -0.28% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,233.41** / 初期 $100.00 (+1133.41%)
- 確定: 5982件 (Win 1766 / Loss 1924 / Flat 2292) / skip 6281件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,233.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5579件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.87** / 初期 $100.00 (+18.87%)
- 確定: 3271件 (Win 952 / Loss 1287 / Flat 1032) / pending 0件 / skip 3898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000125 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.87

## 6. Latest Market Context

- 更新: 2026-09-28T08:06:16.189013+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=83012.9
- Funnel: target 1059 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +47.93% | $277,845,094.21 |
| BATON/USDT:USDT | +26.71% | $1,390,064.86 |
| MARSCOIN/USDT:USDT | +16.52% | $1,915,656.37 |
| ONE/USDT:USDT | +14.77% | $5,829,727.04 |
| BTW/USDT:USDT | +13.73% | $9,769,451.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.12% | +2.00% |
| MONAD/USDT:USDT | below_1h_threshold | +1.53% | +1.41% |
| GRASS/USDT:USDT | below_1h_threshold | +1.30% | +1.18% |
| USOIL/USDT:USDT | below_1h_threshold | +0.90% | +0.78% |
| GRAM/USDT:USDT | below_1h_threshold | +0.87% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
