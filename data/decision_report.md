# Decision Report

- generated_at: 2026-11-28T07:21:25.111418+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19826**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=19826, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.98% | **+1.19%** |
| LIMIT_4PCT | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_ATR | 8/20 | 40.0% | +2.46% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.14% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.63% | **+1.18%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.89% | **+0.76%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定トレード: 293件 (TP 107 / SL 176 / EXP 10)
- 最新: EVAA/USDT:USDT TP_HIT PnL +8.00% 残高後 $122.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,948.01** / 初期 $100.00 (+1848.01%)
- 確定: 7653件 (Win 2202 / Loss 2464 / Flat 2987) / skip 8734件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,948.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5298件 (Win 1410 / Loss 1141 / Flat 2747) / skip 7939件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0523 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7985件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000131 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-28T07:21:11.080405+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=59700.0
- Funnel: target 1101 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +31.77% | $24,606,353.80 |
| BTW/USDT:USDT | +19.17% | $12,759,031.24 |
| SKY/USDT:USDT | +7.30% | $4,091,609.15 |
| CFG/USDT:USDT | +5.90% | $1,637,568.07 |
| ACE/USDT:USDT | +5.11% | $3,710,904.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +1.46% | +1.50% |
| SNXX/USDT:USDT | below_1h_threshold | +0.84% | +0.88% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.67% | +0.71% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +0.57% |
| CRV/USDT:USDT | below_1h_threshold | +0.52% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
