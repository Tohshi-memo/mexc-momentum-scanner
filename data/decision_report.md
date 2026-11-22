# Decision Report

- generated_at: 2026-11-22T15:36:25.988474+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19396**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19396, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_ATR | 7/20 | 35.0% | +0.94% | **+0.33%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.38% | **+1.32%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.23% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,826.01** / 初期 $100.00 (+1726.01%)
- 確定: 7506件 (Win 2157 / Loss 2417 / Flat 2932) / skip 8451件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,826.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$461.08** / 初期 $100.00 (+361.08%)
- 確定: 5160件 (Win 1376 / Loss 1113 / Flat 2671) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0419 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $461.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7557件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T15:36:10.877202+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=60820.2
- Funnel: target 1086 → liquid 103 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +47.89% | $36,549,253.81 |
| CLAUDIA/USDT:USDT | +47.48% | $2,714,959.06 |
| DGAI/USDT:USDT | +32.08% | $1,409,692.53 |
| PIEVERSE/USDT:USDT | +17.96% | $30,515,749.98 |
| BR/USDT:USDT | +15.00% | $1,941,306.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLAUDIA/USDT:USDT | below_1h_threshold | +2.99% | +3.12% |
| DGAI/USDT:USDT | below_1h_threshold | +2.98% | +3.11% |
| BEAT/USDT:USDT | below_1h_threshold | +2.17% | +2.31% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.17% | +2.31% |
| BTW/USDT:USDT | below_1h_threshold | +1.41% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
