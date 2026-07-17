# Decision Report

- generated_at: 2026-07-17T06:11:06.439231+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8826**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=8826, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.04% | **+0.61%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.67% | **+0.57%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.18% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.89% | **+0.72%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.79% | **+0.42%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.06% | **+0.05%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$111.26** / 初期 $100.00 (+11.26%)
- 確定トレード: 109件 (TP 41 / SL 64 / EXP 4)
- 最新: EVAA/USDT:USDT TP_HIT PnL +8.00% 残高後 $111.26
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.01** / 初期 $100.00 (+242.01%)
- 確定: 2941件 (Win 916 / Loss 947 / Flat 1078) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $342.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.06** / 初期 $100.00 (+7.06%)
- 確定: 788件 (Win 181 / Loss 171 / Flat 436) / skip 1449件
- 成長率目線: 平均log +0.000087 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.66** / 初期 $100.00 (-1.34%)
- 確定: 93件 (Win 29 / Loss 60 / Flat 4) / pending 4件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000324 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $98.66

## 6. Latest Market Context

- 更新: 2026-07-17T06:11:01.509264+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62800.9
- Funnel: target 884 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +30.47% | $1,454,301.96 |
| T/USDT:USDT | +15.09% | $1,557,020.71 |
| TAC/USDT:USDT | +12.90% | $3,248,810.29 |
| SOXS/USDT:USDT | +12.77% | $1,476,764.84 |
| MYX/USDT:USDT | +12.10% | $2,004,454.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.35% | +2.36% |
| DEXE/USDT:USDT | below_1h_threshold | +1.97% | +1.99% |
| MYX/USDT:USDT | below_1h_threshold | +1.90% | +1.92% |
| VELVET/USDT:USDT | below_1h_threshold | +1.85% | +1.86% |
| BANK/USDT:USDT | below_1h_threshold | +1.58% | +1.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
