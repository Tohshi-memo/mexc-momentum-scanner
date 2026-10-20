# Decision Report

- generated_at: 2026-10-20T09:31:22.329849+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17050**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=17050, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.89% | **+0.80%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.35% | **+0.50%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.65% | **+0.45%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +3.63% | **+3.63%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.84% | **+0.51%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.44% | **+0.33%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.19% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,324.22** / 初期 $100.00 (+1224.22%)
- 確定: 6478件 (Win 1884 / Loss 2066 / Flat 2528) / skip 7133件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $1,324.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.39** / 初期 $100.00 (+178.39%)
- 確定: 3801件 (Win 1044 / Loss 886 / Flat 1871) / skip 6660件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $278.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5210件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T09:31:09.824185+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81412.9
- Funnel: target 1078 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +74.55% | $4,507,473.15 |
| ALT/USDT:USDT | +18.39% | $1,655,175.15 |
| PHA/USDT:USDT | +17.02% | $18,858,690.50 |
| AKE/USDT:USDT | +12.61% | $4,922,344.99 |
| BR/USDT:USDT | +12.08% | $46,477,843.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TIA/USDT:USDT | below_1h_threshold | +2.37% | +2.48% |
| Q/USDT:USDT | below_1h_threshold | +2.29% | +2.40% |
| USOIL/USDT:USDT | below_1h_threshold | +0.91% | +1.02% |
| LIT/USDT:USDT | below_1h_threshold | +0.49% | +0.59% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.46% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
