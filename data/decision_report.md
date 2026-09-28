# Decision Report

- generated_at: 2026-09-28T10:16:22.664459+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15709**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=15709, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.62% | **+1.46%** |
| LIMIT_BB3S | 5/13 | 38.5% | +2.20% | **+0.85%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.46% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.74% | **+0.86%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.79% | **+0.81%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.51% | **+0.10%** |
| MARKET_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,233.41** / 初期 $100.00 (+1133.41%)
- 確定: 5982件 (Win 1766 / Loss 1924 / Flat 2292) / skip 6288件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,233.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5586件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.27** / 初期 $100.00 (+19.27%)
- 確定: 3278件 (Win 953 / Loss 1287 / Flat 1038) / pending 3件 / skip 3898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $119.27

## 6. Latest Market Context

- 更新: 2026-09-28T10:16:13.569552+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=82772.5
- Funnel: target 1059 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +27.23% | $307,385,111.14 |
| HBAR/USDT:USDT | +22.55% | $41,947,612.77 |
| BTW/USDT:USDT | +19.04% | $11,740,599.94 |
| MARSCOIN/USDT:USDT | +14.19% | $2,596,843.19 |
| GRT/USDT:USDT | +12.50% | $12,827,011.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +4.10% | +3.94% |
| IMX/USDT:USDT | below_1h_threshold | +2.62% | +2.46% |
| HBAR/USDT:USDT | below_1h_threshold | +2.22% | +2.05% |
| PYTH/USDT:USDT | below_1h_threshold | +1.78% | +1.61% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.17% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
