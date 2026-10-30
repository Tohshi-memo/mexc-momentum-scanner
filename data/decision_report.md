# Decision Report

- generated_at: 2026-10-30T19:31:33.708277+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17863**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.97% / filled 20/20。**
- 全期間 MARKET基準: n=17863, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_7PCT | 6/20 | 30.0% | +5.13% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.07% | **+0.70%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.74% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 19/20 | 95.0% | +2.23% | **+2.12%** |
| LIMIT_4PCT_LONG | 17/20 | 85.0% | +1.85% | **+1.58%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +2.07% | **+1.24%** |
| LIMIT_5PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.92% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.56** / 初期 $100.00 (+1423.56%)
- 確定: 6806件 (Win 1975 / Loss 2181 / Flat 2650) / skip 7618件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,523.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.50** / 初期 $100.00 (+263.50%)
- 確定: 4364件 (Win 1173 / Loss 983 / Flat 2208) / skip 6910件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0311 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $363.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6025件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000239 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T19:31:18.497949+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=76470.5
- Funnel: target 1090 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +9.24% | $11,152,677.25 |
| BTW/USDT:USDT | +8.49% | $10,503,314.71 |
| AIN/USDT:USDT | +6.11% | $4,231,406.83 |
| OP/USDT:USDT | +4.75% | $9,837,305.00 |
| SOXS/USDT:USDT | +3.37% | $51,218,789.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +1.66% | +1.85% |
| TIA/USDT:USDT | below_1h_threshold | +0.95% | +1.14% |
| ASTER/USDT:USDT | below_1h_threshold | +0.92% | +1.11% |
| OP/USDT:USDT | below_1h_threshold | +0.92% | +1.11% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.87% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
