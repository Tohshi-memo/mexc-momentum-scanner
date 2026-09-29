# Decision Report

- generated_at: 2026-09-29T21:11:36.800009+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15801**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15801, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_8PCT | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_9PCT | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.39% | **+0.69%** |
| LIMIT_10PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +2.86% | **+2.50%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.85% | **+2.42%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.23% | **+2.12%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.02% | **+2.12%** |
| MARKET_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5987件 (Win 1766 / Loss 1925 / Flat 2296) / skip 6375件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRASS/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3535件 (Win 974 / Loss 812 / Flat 1749) / skip 5677件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0560 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000239 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T21:11:24.300139+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=83510.6
- Funnel: target 1073 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +136.63% | $3,851,970.49 |
| GRASS/USDT:USDT | +8.43% | $11,854,040.86 |
| QNT/USDT:USDT | +7.42% | $328,549,915.45 |
| SOONNETWORK/USDT:USDT | +5.42% | $2,929,210.33 |
| BTW/USDT:USDT | +5.30% | $14,099,206.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOONNETWORK/USDT:USDT | below_1h_threshold | +1.44% | +1.53% |
| ICP/USDT:USDT | below_1h_threshold | +0.81% | +0.89% |
| JTO/USDT:USDT | below_1h_threshold | +0.68% | +0.76% |
| QNT/USDT:USDT | below_1h_threshold | +0.63% | +0.71% |
| A/USDT:USDT | below_1h_threshold | +0.56% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
