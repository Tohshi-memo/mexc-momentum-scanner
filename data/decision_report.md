# Decision Report

- generated_at: 2026-09-13T03:11:23.261849+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14358**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14358, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +3.96% | **+1.39%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.01% | **+0.71%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.31% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/14 | 42.9% | +6.16% | **+2.64%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +4.42% | **+1.99%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.99% | **+1.75%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.41% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5489件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$219.93** / 初期 $100.00 (+119.93%)
- 確定: 2876件 (Win 797 / Loss 672 / Flat 1407) / skip 4893件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0824 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $219.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.71** / 初期 $100.00 (+26.71%)
- 確定: 2809件 (Win 836 / Loss 1080 / Flat 893) / pending 4件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000437 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.71

## 6. Latest Market Context

- 更新: 2026-09-13T03:11:10.687004+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77246.4
- Funnel: target 1068 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +187.48% | $69,836,204.93 |
| POWR/USDT:USDT | +47.04% | $1,476,793.54 |
| ZCAT/USDT:USDT | +39.61% | $1,150,666.11 |
| ALCH/USDT:USDT | +17.36% | $2,727,950.99 |
| STORJ/USDT:USDT | +17.26% | $19,018,323.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VTHO/USDT:USDT | below_1h_threshold | +3.91% | +3.93% |
| UAI/USDT:USDT | below_1h_threshold | +3.83% | +3.85% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.71% | +3.73% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.07% | +2.09% |
| ILV/USDT:USDT | below_1h_threshold | +1.10% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
