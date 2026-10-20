# Decision Report

- generated_at: 2026-10-20T07:46:23.329096+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17046**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.66% / filled 20/20。**
- 全期間 MARKET基準: n=17046, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.66% | **+2.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.66% | **+2.66%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.57% | **+2.32%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.99% | **+1.19%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.35% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +0.36% | **+0.27%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,289.19** / 初期 $100.00 (+1189.19%)
- 確定: 6475件 (Win 1881 / Loss 2066 / Flat 2528) / skip 7132件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.52% 残高後 $1,289.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.39** / 初期 $100.00 (+178.39%)
- 確定: 3800件 (Win 1044 / Loss 886 / Flat 1870) / skip 6657件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $278.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5206件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T07:46:10.168347+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=81539.3
- Funnel: target 1078 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +42.71% | $1,392,161.00 |
| ALT/USDT:USDT | +25.13% | $1,237,469.89 |
| PHA/USDT:USDT | +23.53% | $17,531,028.32 |
| BR/USDT:USDT | +16.04% | $43,833,203.14 |
| A/USDT:USDT | +12.05% | $23,160,389.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALT/USDT:USDT | below_1h_threshold | +3.20% | +3.49% |
| BR/USDT:USDT | below_1h_threshold | +2.52% | +2.81% |
| AKE/USDT:USDT | below_1h_threshold | +2.43% | +2.72% |
| UNITREE/USDT:USDT | below_1h_threshold | +1.04% | +1.34% |
| A/USDT:USDT | below_1h_threshold | +0.67% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
