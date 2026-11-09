# Decision Report

- generated_at: 2026-11-09T15:17:39.367087+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18534**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=18534, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_BB3S | 5/16 | 31.2% | +1.26% | **+0.40%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.55% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.78%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.92% | **+0.55%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.26% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 266件 (TP 97 / SL 161 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,626.14** / 初期 $100.00 (+1526.14%)
- 確定: 7163件 (Win 2057 / Loss 2285 / Flat 2821) / skip 7932件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RITUAL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,626.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4757件 (Win 1277 / Loss 1047 / Flat 2433) / skip 7188件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0851 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6705件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-09T15:16:52.888809+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=74797.6
- Funnel: target 1094 → liquid 148 → pre 50 → checked 50 → surge 11 → strict 11
- Surge前reject: below_1h_threshold=39, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +23.63% | $3,632,711.05 |
| RITUAL/USDT:USDT | +20.76% | $1,688,348.02 |
| MVLL/USDT:USDT | +18.14% | $2,001,371.38 |
| SOXL/USDT:USDT | +17.31% | $398,946,792.02 |
| EDGE/USDT:USDT | +17.07% | $1,629,079.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +4.94% | +5.03% |
| TESLA/USDT:USDT | below_1h_threshold | +4.90% | +5.00% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.86% | +4.95% |
| SNOWSTOCK/USDT:USDT | below_1h_threshold | +4.68% | +4.77% |
| DRAM/USDT:USDT | below_1h_threshold | +4.31% | +4.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
