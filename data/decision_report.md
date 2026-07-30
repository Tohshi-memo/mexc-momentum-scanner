# Decision Report

- generated_at: 2026-07-30T21:41:46.235700+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9931**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9931, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-3.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.42% | **-3.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.26% | **+0.12%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +3.55% | **+3.55%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +4.38% | **+3.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.72% | **+2.61%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.45% | **+2.45%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +5.42% | **+2.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$523.44** / 初期 $100.00 (+423.44%)
- 確定: 3529件 (Win 1121 / Loss 1148 / Flat 1260) / skip 2963件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $523.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2099件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2152 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.61** / 初期 $100.00 (+10.61%)
- 確定: 804件 (Win 262 / Loss 319 / Flat 223) / pending 1件 / skip 607件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000609 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $110.61

## 6. Latest Market Context

- 更新: 2026-07-30T21:41:34.973929+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64765.5
- Funnel: target 920 → liquid 174 → pre 50 → checked 50 → surge 6 → strict 2
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 82.4 >= 65=1, 4h RSI 79.6 >= 65=1, 4h RSI 66.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AXTISTOCK/USDT:USDT | +26.63% | $1,986,760.36 |
| MMT/USDT:USDT | +22.96% | $7,017,312.21 |
| AMZU/USDT:USDT | +17.26% | $2,511,267.73 |
| JIMOTHY/USDT:USDT | +16.82% | $1,680,481.99 |
| SNXX/USDT:USDT | +16.70% | $10,399,081.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +3.67% | +3.65% |
| MUU/USDT:USDT | below_1h_threshold | +3.42% | +3.40% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.32% | +3.30% |
| MMT/USDT:USDT | below_1h_threshold | +3.05% | +3.02% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.93% | +2.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
