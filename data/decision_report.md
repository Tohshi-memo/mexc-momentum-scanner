# Decision Report

- generated_at: 2026-11-03T01:26:37.659428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18044**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=18044, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.57% | **+1.10%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.21% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.28% | **+1.37%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.63% | **+0.81%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.18% | **+0.77%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.99% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 260件 (TP 96 / SL 156 / EXP 8)
- 最新: EVAA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,540.50** / 初期 $100.00 (+1440.50%)
- 確定: 6896件 (Win 1999 / Loss 2213 / Flat 2684) / skip 7709件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $1,540.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.70** / 初期 $100.00 (+281.70%)
- 確定: 4482件 (Win 1204 / Loss 1000 / Flat 2278) / skip 6973件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0166 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $381.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6204件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000297 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-03T01:26:24.589631+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=77288.3
- Funnel: target 1093 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +34.88% | $17,968,785.82 |
| AGT/USDT:USDT | +19.71% | $3,001,728.58 |
| JCT/USDT:USDT | +11.00% | $2,387,713.79 |
| EVAA/USDT:USDT | +10.91% | $6,954,841.54 |
| SOXS/USDT:USDT | +7.95% | $25,378,719.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +3.44% | +3.21% |
| LSK/USDT:USDT | below_1h_threshold | +1.66% | +1.42% |
| HOT/USDT:USDT | below_1h_threshold | +1.62% | +1.38% |
| JCT/USDT:USDT | below_1h_threshold | +0.91% | +0.67% |
| LIT/USDT:USDT | below_1h_threshold | +0.54% | +0.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
