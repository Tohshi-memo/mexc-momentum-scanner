# Decision Report

- generated_at: 2026-07-30T21:01:28.631866+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9925**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9925, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-3.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.53% | **-3.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.38% | **+0.15%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.43% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +4.19% | **+3.77%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +5.14% | **+3.60%** |
| MARKET_LONG | 20/20 | 100.0% | +2.92% | **+2.92%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.88% | **+2.52%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.43% | **+2.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$515.46** / 初期 $100.00 (+415.46%)
- 確定: 3525件 (Win 1118 / Loss 1147 / Flat 1260) / skip 2961件
- 成長率目線: 平均log +0.000465 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $515.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2093件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1547 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.61** / 初期 $100.00 (+10.61%)
- 確定: 804件 (Win 262 / Loss 319 / Flat 223) / pending 1件 / skip 602件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000616 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $110.61

## 6. Latest Market Context

- 更新: 2026-07-30T21:01:19.652337+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64750.1
- Funnel: target 920 → liquid 169 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1, 4h RSI 79.9 >= 65=1, 4h RSI 77.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AXTISTOCK/USDT:USDT | +33.79% | $1,547,998.98 |
| MMT/USDT:USDT | +18.79% | $6,590,483.05 |
| ROBO/USDT:USDT | +16.18% | $2,961,838.02 |
| ESPORTS/USDT:USDT | +14.91% | $4,611,453.45 |
| AMZU/USDT:USDT | +13.38% | $2,379,354.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +3.67% | +3.67% |
| MUU/USDT:USDT | below_1h_threshold | +3.42% | +3.42% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.32% | +3.32% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.93% | +2.93% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.59% | +2.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
