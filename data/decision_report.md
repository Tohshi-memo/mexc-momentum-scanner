# Decision Report

- generated_at: 2026-08-13T01:56:34.813461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11416**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11416, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +3.98% | **+0.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.59% | **+0.56%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.70% | **+0.49%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.98% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.33% | **+2.22%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.57% | **+1.96%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.31% | **+1.66%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.05** / 初期 $100.00 (+503.05%)
- 確定: 3950件 (Win 1232 / Loss 1292 / Flat 1426) / skip 4027件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $603.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.63** / 初期 $100.00 (+47.63%)
- 確定: 1604件 (Win 452 / Loss 376 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1128 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $147.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.20** / 初期 $100.00 (+15.20%)
- 確定: 1424件 (Win 417 / Loss 536 / Flat 471) / pending 4件 / skip 1459件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000119 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $115.20

## 6. Latest Market Context

- 更新: 2026-08-13T01:56:20.691162+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63482.3
- Funnel: target 972 → liquid 178 → pre 50 → checked 49 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=1
- Strict後reject: 4h RSI 84.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +35.63% | $7,532,012.66 |
| APR/USDT:USDT | +33.24% | $13,270,960.84 |
| BTW/USDT:USDT | +17.05% | $22,366,129.80 |
| BANK/USDT:USDT | +11.66% | $3,332,563.89 |
| COOKIE/USDT:USDT | +11.29% | $1,024,190.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.11% | +4.18% |
| CYS/USDT:USDT | below_1h_threshold | +2.34% | +2.42% |
| ONE/USDT:USDT | below_1h_threshold | +2.27% | +2.34% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.75% | +1.83% |
| JTO/USDT:USDT | below_1h_threshold | +1.16% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
