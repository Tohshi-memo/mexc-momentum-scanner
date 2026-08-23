# Decision Report

- generated_at: 2026-08-23T22:06:26.114901+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12474**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12474, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 9/14 | 64.3% | +1.20% | **+0.77%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +5.34% | **+4.45%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +3.76% | **+2.26%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.93% | **+2.22%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.80% | **+1.54%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.83% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$725.31** / 初期 $100.00 (+625.31%)
- 確定: 4501件 (Win 1375 / Loss 1471 / Flat 1655) / skip 4534件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.23% 残高後 $725.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.26** / 初期 $100.00 (+57.26%)
- 確定: 1950件 (Win 536 / Loss 469 / Flat 945) / skip 3935件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0085 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $157.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.75** / 初期 $100.00 (+16.75%)
- 確定: 1868件 (Win 551 / Loss 708 / Flat 609) / pending 3件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000089 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.75

## 6. Latest Market Context

- 更新: 2026-08-23T22:06:17.198959+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=77649.3
- Funnel: target 1018 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +20.28% | $56,217,875.14 |
| 1000RATS/USDT:USDT | +11.35% | $2,166,738.10 |
| SPK/USDT:USDT | +11.20% | $5,958,868.80 |
| GRASS/USDT:USDT | +10.80% | $1,957,389.05 |
| PENGU/USDT:USDT | +10.24% | $21,199,031.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPK/USDT:USDT | below_1h_threshold | +1.38% | +1.59% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.80% | +1.00% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.49% | +0.70% |
| CAP/USDT:USDT | below_1h_threshold | +0.31% | +0.52% |
| 1000RATS/USDT:USDT | below_1h_threshold | +0.29% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
