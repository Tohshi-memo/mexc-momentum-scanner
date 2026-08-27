# Decision Report

- generated_at: 2026-08-27T03:56:24.054182+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12767**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=12767, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.92% | **+0.77%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.78% | **+0.58%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.80% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.25% | **+1.18%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.79% | **+0.63%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.75% | **+0.49%** |
| MARKET_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$730.53** / 初期 $100.00 (+630.53%)
- 確定: 4660件 (Win 1414 / Loss 1528 / Flat 1718) / skip 4668件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: S/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $730.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2002件 (Win 544 / Loss 483 / Flat 975) / skip 4176件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1035 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1982件 (Win 580 / Loss 758 / Flat 644) / pending 2件 / skip 2256件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-27T03:56:15.065138+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=78777.0
- Funnel: target 1023 → liquid 166 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.4 >= 65=1, 4h RSI 83.0 >= 65=1, 4h RSI 71.4 >= 65=1, 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +23.86% | $19,780,827.58 |
| CASHCAT/USDT:USDT | +20.70% | $1,762,770.97 |
| SPX/USDT:USDT | +18.60% | $6,241,534.71 |
| RUNE/USDT:USDT | +18.53% | $1,089,264.32 |
| CHIP/USDT:USDT | +15.05% | $1,894,881.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +4.70% | +4.60% |
| RUNE/USDT:USDT | below_1h_threshold | +3.15% | +3.05% |
| CHIP/USDT:USDT | below_1h_threshold | +3.01% | +2.91% |
| SPX/USDT:USDT | below_1h_threshold | +2.57% | +2.47% |
| VVV/USDT:USDT | below_1h_threshold | +2.35% | +2.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
