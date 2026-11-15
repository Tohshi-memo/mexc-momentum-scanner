# Decision Report

- generated_at: 2026-11-15T08:46:33.521965+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18944**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=18944, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.87% | **+0.65%** |
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.68% | **+0.42%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.42% | **+0.36%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.17% | **+6.17%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.70% | **+0.27%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,711.71** / 初期 $100.00 (+1611.71%)
- 確定: 7335件 (Win 2106 / Loss 2348 / Flat 2881) / skip 8170件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,711.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$427.40** / 初期 $100.00 (+327.40%)
- 確定: 4952件 (Win 1323 / Loss 1081 / Flat 2548) / skip 7403件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0158 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $427.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7105件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000236 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T08:46:14.334882+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.27% price=64796.6
- Funnel: target 1066 → liquid 136 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1, 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +34.39% | $3,378,128.83 |
| EVAA/USDT:USDT | +18.26% | $11,551,990.54 |
| PIEVERSE/USDT:USDT | +11.04% | $1,918,058.21 |
| ARIA/USDT:USDT | +8.66% | $2,577,163.15 |
| VVV/USDT:USDT | +8.19% | $3,212,327.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.85% | +3.59% |
| BEAT/USDT:USDT | below_1h_threshold | +3.97% | +2.70% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.71% | +0.45% |
| VVV/USDT:USDT | below_1h_threshold | +1.47% | +0.21% |
| JCT/USDT:USDT | below_1h_threshold | +1.34% | +0.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
