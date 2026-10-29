# Decision Report

- generated_at: 2026-10-29T03:46:46.731104+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17756**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=17756, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.89% | **+0.82%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.32% | **+0.22%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,546.74** / 初期 $100.00 (+1446.74%)
- 確定: 6800件 (Win 1975 / Loss 2177 / Flat 2648) / skip 7517件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,546.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$357.66** / 初期 $100.00 (+257.66%)
- 確定: 4277件 (Win 1157 / Loss 972 / Flat 2148) / skip 6890件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0199 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $357.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5918件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000331 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T03:46:22.718299+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=79820.0
- Funnel: target 1083 → liquid 174 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +60.27% | $2,284,425.01 |
| BULLA/USDT:USDT | +16.07% | $3,067,259.70 |
| AKE/USDT:USDT | +10.57% | $6,897,948.79 |
| INIT/USDT:USDT | +8.96% | $2,193,741.10 |
| IRYS/USDT:USDT | +8.75% | $2,364,219.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.34% | +2.48% |
| BULLA/USDT:USDT | below_1h_threshold | +1.98% | +2.12% |
| BLUR/USDT:USDT | below_1h_threshold | +1.31% | +1.45% |
| BTW/USDT:USDT | below_1h_threshold | +0.92% | +1.05% |
| XPIN/USDT:USDT | below_1h_threshold | +0.55% | +0.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
