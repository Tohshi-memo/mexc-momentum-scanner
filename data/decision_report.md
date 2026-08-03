# Decision Report

- generated_at: 2026-08-03T14:21:46.686002+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10219**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10219, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.35% | **+0.81%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.43% | **+2.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.64% | **+2.11%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.67% | **+1.59%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.36% | **+0.61%** |
| MARKET_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$571.98** / 初期 $100.00 (+471.98%)
- 確定: 3678件 (Win 1167 / Loss 1205 / Flat 1306) / skip 3102件
- 成長率目線: 平均log +0.000474 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $571.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2347件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0052 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1004件 (Win 323 / Loss 391 / Flat 290) / pending 6件 / skip 682件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000554 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-03T14:21:32.271235+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=63215.6
- Funnel: target 929 → liquid 160 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +196.82% | $3,369,418.21 |
| BICO/USDT:USDT | +59.57% | $16,360,608.93 |
| 1000RATS/USDT:USDT | +30.21% | $37,816,343.26 |
| SKYAI/USDT:USDT | +24.01% | $5,185,705.18 |
| BTW/USDT:USDT | +23.27% | $6,386,009.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +4.46% | +4.62% |
| METASTOCK/USDT:USDT | below_1h_threshold | +4.16% | +4.32% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +3.18% | +3.34% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +2.65% | +2.81% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.60% | +2.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
