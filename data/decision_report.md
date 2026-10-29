# Decision Report

- generated_at: 2026-10-29T04:26:35.114156+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17759**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=17759, expectancy=+0.01%
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
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_BB3S | 3/18 | 16.7% | +2.52% | **+0.42%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.32% | **+0.22%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.31** / 初期 $100.00 (+1431.31%)
- 確定: 6802件 (Win 1975 / Loss 2179 / Flat 2648) / skip 7518件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,531.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$357.66** / 初期 $100.00 (+257.66%)
- 確定: 4280件 (Win 1157 / Loss 972 / Flat 2151) / skip 6890件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0211 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $357.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T04:26:17.823567+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=79908.1
- Funnel: target 1083 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +55.88% | $2,593,696.62 |
| BULLA/USDT:USDT | +26.34% | $2,871,394.96 |
| INIT/USDT:USDT | +12.17% | $2,204,758.13 |
| Q/USDT:USDT | +8.83% | $31,184,090.52 |
| ORCLSTOCK/USDT:USDT | +7.77% | $5,071,129.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INIT/USDT:USDT | below_1h_threshold | +4.15% | +4.05% |
| PEPE/USDT:USDT | below_1h_threshold | +1.47% | +1.36% |
| ENA/USDT:USDT | below_1h_threshold | +0.46% | +0.36% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +0.34% | +0.24% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.33% | +0.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
