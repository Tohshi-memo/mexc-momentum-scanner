# Decision Report

- generated_at: 2026-08-03T14:58:12.498479+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10223**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10223, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.23% | **-2.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.07% | **+0.93%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.35% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.94% | **+2.94%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.65% | **+2.56%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.54% | **+2.50%** |
| MARKET_LONG | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.90% | **+1.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$576.35** / 初期 $100.00 (+476.35%)
- 確定: 3682件 (Win 1168 / Loss 1205 / Flat 1309) / skip 3102件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $576.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2351件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.67** / 初期 $100.00 (+15.67%)
- 確定: 1008件 (Win 324 / Loss 391 / Flat 293) / pending 6件 / skip 683件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000523 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.67

## 6. Latest Market Context

- 更新: 2026-08-03T14:36:28.837152+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.53% price=63652.4
- Funnel: target 929 → liquid 162 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.1 >= 65=1, 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +217.99% | $3,755,336.79 |
| BICO/USDT:USDT | +59.73% | $16,732,774.36 |
| 1000RATS/USDT:USDT | +33.05% | $38,093,193.49 |
| BTW/USDT:USDT | +25.65% | $6,510,811.99 |
| SKYAI/USDT:USDT | +24.01% | $5,510,208.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +4.46% | +3.93% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.29% | +3.76% |
| METASTOCK/USDT:USDT | below_1h_threshold | +4.16% | +3.63% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +3.18% | +2.65% |
| BTW/USDT:USDT | below_1h_threshold | +2.95% | +2.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
