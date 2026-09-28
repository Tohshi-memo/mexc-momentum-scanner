# Decision Report

- generated_at: 2026-09-28T08:51:38.060437+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15703**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.97% / filled 20/20。**
- 全期間 MARKET基準: n=15703, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.65% | **+1.40%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.04% | **+0.57%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.56% | **+0.39%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.05% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.44% | **+0.52%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.90% | **+0.41%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.20% | **+0.05%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.38% | **-0.17%** |
| MARKET_LONG | 20/20 | 100.0% | -0.31% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,233.41** / 初期 $100.00 (+1133.41%)
- 確定: 5982件 (Win 1766 / Loss 1924 / Flat 2292) / skip 6282件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,233.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5580件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.87** / 初期 $100.00 (+18.87%)
- 確定: 3272件 (Win 952 / Loss 1287 / Flat 1033) / pending 3件 / skip 3898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000118 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HBAR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $118.87

## 6. Latest Market Context

- 更新: 2026-09-28T08:51:23.199474+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=82884.3
- Funnel: target 1059 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.1 >= 65=1, 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +41.08% | $290,631,296.59 |
| MARSCOIN/USDT:USDT | +20.11% | $2,288,621.97 |
| HBAR/USDT:USDT | +17.80% | $22,639,544.31 |
| BTW/USDT:USDT | +16.78% | $10,950,377.54 |
| BATON/USDT:USDT | +14.01% | $1,448,365.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JASMY/USDT:USDT | below_1h_threshold | +1.39% | +1.43% |
| APT/USDT:USDT | below_1h_threshold | +1.13% | +1.17% |
| BR/USDT:USDT | below_1h_threshold | +1.05% | +1.09% |
| SKY/USDT:USDT | below_1h_threshold | +0.94% | +0.98% |
| USOIL/USDT:USDT | below_1h_threshold | +0.90% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
