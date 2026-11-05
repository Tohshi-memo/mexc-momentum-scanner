# Decision Report

- generated_at: 2026-11-05T05:36:25.021125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18159**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.37% / filled 20/20。**
- 全期間 MARKET基準: n=18159, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.32% | **+0.21%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.13% | **+0.06%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,508.30** / 初期 $100.00 (+1408.30%)
- 確定: 6978件 (Win 2018 / Loss 2241 / Flat 2719) / skip 7742件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,508.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$372.01** / 初期 $100.00 (+272.01%)
- 確定: 4557件 (Win 1223 / Loss 1030 / Flat 2304) / skip 7013件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0065 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MVLL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $372.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6320件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000188 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T05:36:14.270926+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=80489.8
- Funnel: target 1078 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELSA/USDT:USDT | +27.66% | $3,354,627.25 |
| JCT/USDT:USDT | +23.05% | $7,489,630.52 |
| APPSTOCK/USDT:USDT | +20.63% | $1,426,080.94 |
| UAI/USDT:USDT | +20.04% | $5,419,347.80 |
| FLUID/USDT:USDT | +18.00% | $4,609,334.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.05% | +4.05% |
| ELSA/USDT:USDT | below_1h_threshold | +3.82% | +3.82% |
| SOXS/USDT:USDT | below_1h_threshold | +0.97% | +0.97% |
| AIN/USDT:USDT | below_1h_threshold | +0.84% | +0.84% |
| APPSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
