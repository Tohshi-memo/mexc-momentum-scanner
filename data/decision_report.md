# Decision Report

- generated_at: 2026-08-03T14:06:30.349235+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10218**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10218, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +2.35% | **+1.41%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.45% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.94% | **+2.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.03% | **+1.01%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.04% | **+0.99%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.49% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3677件 (Win 1166 / Loss 1205 / Flat 1306) / skip 3102件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2346件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0056 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.97** / 初期 $100.00 (+14.97%)
- 確定: 1003件 (Win 322 / Loss 391 / Flat 290) / pending 5件 / skip 682件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000545 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $114.97

## 6. Latest Market Context

- 更新: 2026-08-03T14:06:18.392513+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=63224.9
- Funnel: target 929 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +150.20% | $2,861,601.80 |
| BICO/USDT:USDT | +61.71% | $15,853,104.05 |
| 1000RATS/USDT:USDT | +32.50% | $37,509,225.16 |
| BTW/USDT:USDT | +23.32% | $6,250,968.50 |
| SKYAI/USDT:USDT | +21.13% | $4,982,443.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| METASTOCK/USDT:USDT | below_1h_threshold | +4.16% | +4.31% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +3.18% | +3.33% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.71% |
| AMZNSTOCK/USDT:USDT | below_1h_threshold | +2.53% | +2.68% |
| BASTOCK/USDT:USDT | below_1h_threshold | +2.44% | +2.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
