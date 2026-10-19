# Decision Report

- generated_at: 2026-10-19T16:36:23.806891+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17018**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.61% / filled 20/20。**
- 全期間 MARKET基準: n=17018, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.80% | **+1.62%** |
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.24% | **+0.93%** |
| LIMIT_BB3S | 4/15 | 26.7% | +1.15% | **+0.31%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.46% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.51% | **-0.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,258.01** / 初期 $100.00 (+1158.01%)
- 確定: 6463件 (Win 1874 / Loss 2063 / Flat 2526) / skip 7116件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVA/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.04% 残高後 $1,258.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.65** / 初期 $100.00 (+177.65%)
- 確定: 3783件 (Win 1039 / Loss 884 / Flat 1860) / skip 6646件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0284 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AVA/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.02% 残高後 $277.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5178件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000094 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T16:36:12.856216+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=81983.3
- Funnel: target 1090 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AVA/USDT:USDT | +6.34% | $1,694,514.48 |
| SOXS/USDT:USDT | +1.98% | $2,909,513.41 |
| VVV/USDT:USDT | +1.84% | $5,308,066.66 |
| BR/USDT:USDT | +1.82% | $26,711,103.25 |
| DOT/USDT:USDT | +1.70% | $20,342,870.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +1.90% | +1.82% |
| VVV/USDT:USDT | below_1h_threshold | +1.85% | +1.77% |
| DOT/USDT:USDT | below_1h_threshold | +1.72% | +1.64% |
| GRASS/USDT:USDT | below_1h_threshold | +1.68% | +1.59% |
| INJ/USDT:USDT | below_1h_threshold | +1.44% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
