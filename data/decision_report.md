# Decision Report

- generated_at: 2026-08-23T22:51:26.348359+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12476**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12476, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 9/16 | 56.2% | +1.20% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +5.33% | **+4.00%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.88% | **+1.73%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.69% | **+1.66%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.71% | **+0.94%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.05% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$721.69** / 初期 $100.00 (+621.69%)
- 確定: 4503件 (Win 1375 / Loss 1472 / Flat 1656) / skip 4534件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $721.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.26** / 初期 $100.00 (+57.26%)
- 確定: 1952件 (Win 536 / Loss 469 / Flat 947) / skip 3935件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0072 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $157.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.75** / 初期 $100.00 (+16.75%)
- 確定: 1870件 (Win 551 / Loss 708 / Flat 611) / pending 1件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000080 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.75

## 6. Latest Market Context

- 更新: 2026-08-23T22:51:17.545051+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=77624.2
- Funnel: target 1018 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +22.16% | $58,007,511.42 |
| SPK/USDT:USDT | +11.50% | $6,129,367.71 |
| GRASS/USDT:USDT | +11.14% | $2,080,595.65 |
| PENGU/USDT:USDT | +10.52% | $23,595,719.60 |
| 1000RATS/USDT:USDT | +8.45% | $2,218,812.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +2.80% | +3.04% |
| SPK/USDT:USDT | below_1h_threshold | +1.96% | +2.20% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.83% | +2.07% |
| STX/USDT:USDT | below_1h_threshold | +1.38% | +1.62% |
| NEAR/USDT:USDT | below_1h_threshold | +1.20% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
