# Decision Report

- generated_at: 2026-09-13T01:21:26.087348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14341**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14341, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +2.20% | **+0.88%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.21% | **+0.48%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.03% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.10% | **+2.32%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.73% | **+2.32%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.25% | **+2.28%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.37% | **+1.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5472件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$220.42** / 初期 $100.00 (+120.42%)
- 確定: 2859件 (Win 792 / Loss 664 / Flat 1403) / skip 4893件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1988 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $220.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.41** / 初期 $100.00 (+26.41%)
- 確定: 2792件 (Win 830 / Loss 1072 / Flat 890) / pending 4件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000526 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $126.41

## 6. Latest Market Context

- 更新: 2026-09-13T01:21:12.979884+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77259.2
- Funnel: target 1068 → liquid 124 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.3 >= 65=1, 4h RSI 83.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +124.97% | $64,112,337.48 |
| ZCAT/USDT:USDT | +25.74% | $1,070,915.59 |
| LONGXIA/USDT:USDT | +19.92% | $9,996,431.06 |
| STORJ/USDT:USDT | +18.95% | $19,729,177.55 |
| REZ/USDT:USDT | +15.07% | $2,460,488.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +3.46% | +3.43% |
| VTHO/USDT:USDT | below_1h_threshold | +1.76% | +1.74% |
| CHZ/USDT:USDT | below_1h_threshold | +1.10% | +1.07% |
| RIVER/USDT:USDT | below_1h_threshold | +1.07% | +1.04% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.03% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
