# Decision Report

- generated_at: 2026-08-13T04:21:27.117458+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11420**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11420, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +3.36% | **+1.51%** |
| LIMIT_9PCT | 2/20 | 10.0% | +7.96% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.91% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.98% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.26% | **+2.12%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.18% | **+2.07%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.45% | **+1.35%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.05** / 初期 $100.00 (+503.05%)
- 確定: 3950件 (Win 1232 / Loss 1292 / Flat 1426) / skip 4031件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $603.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.86** / 初期 $100.00 (+47.86%)
- 確定: 1608件 (Win 454 / Loss 378 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1187 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $147.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.10** / 初期 $100.00 (+15.10%)
- 確定: 1428件 (Win 418 / Loss 538 / Flat 472) / pending 5件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $115.10

## 6. Latest Market Context

- 更新: 2026-08-13T04:21:18.789367+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63599.0
- Funnel: target 972 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +34.36% | $8,097,146.67 |
| APR/USDT:USDT | +12.72% | $14,971,232.94 |
| COOKIE/USDT:USDT | +9.00% | $1,045,492.18 |
| CASHCAT/USDT:USDT | +7.52% | $1,012,930.46 |
| CYS/USDT:USDT | +7.26% | $17,527,494.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.25% | +3.28% |
| BMT/USDT:USDT | below_1h_threshold | +3.24% | +3.28% |
| BLESS/USDT:USDT | below_1h_threshold | +2.52% | +2.56% |
| HEI/USDT:USDT | below_1h_threshold | +1.22% | +1.26% |
| COOKIE/USDT:USDT | below_1h_threshold | +0.98% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
