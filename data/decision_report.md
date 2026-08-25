# Decision Report

- generated_at: 2026-08-25T12:06:22.177477+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12598**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=12598, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.72% | **+0.61%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.05% | **+0.26%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.29% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.55% | **+0.42%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$701.28** / 初期 $100.00 (+601.28%)
- 確定: 4578件 (Win 1392 / Loss 1502 / Flat 1684) / skip 4581件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $701.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4032件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0296 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.26** / 初期 $100.00 (+15.26%)
- 確定: 1926件 (Win 564 / Loss 733 / Flat 629) / pending 6件 / skip 2141件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000091 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.26

## 6. Latest Market Context

- 更新: 2026-08-25T12:06:14.201214+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=78889.7
- Funnel: target 1023 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +78.80% | $4,852,823.73 |
| JIMOTHY/USDT:USDT | +70.52% | $1,661,105.81 |
| ONG/USDT:USDT | +33.90% | $8,775,954.83 |
| TAC/USDT:USDT | +32.44% | $6,722,387.28 |
| PONS/USDT:USDT | +16.25% | $1,118,808.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +3.20% | +3.46% |
| HOLO/USDT:USDT | below_1h_threshold | +2.01% | +2.27% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.93% | +2.20% |
| STORJ/USDT:USDT | below_1h_threshold | +1.64% | +1.90% |
| TAC/USDT:USDT | below_1h_threshold | +0.94% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
