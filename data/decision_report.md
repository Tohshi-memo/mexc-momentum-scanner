# Decision Report

- generated_at: 2026-10-27T16:36:40.460054+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17627**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17627, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.30% | **-2.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +5.20% | **+2.08%** |
| LIMIT_9PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +3.15% | **+1.58%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +4.33% | **+3.46%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.29% | **+2.79%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +4.60% | **+2.30%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +5.38% | **+2.15%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.04% | **+1.94%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 254件 (TP 94 / SL 152 / EXP 8)
- 最新: APR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,573.37** / 初期 $100.00 (+1473.37%)
- 確定: 6736件 (Win 1963 / Loss 2157 / Flat 2616) / skip 7452件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,573.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$346.41** / 初期 $100.00 (+246.41%)
- 確定: 4156件 (Win 1138 / Loss 963 / Flat 2055) / skip 6882件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1042 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $346.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5788件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000430 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T16:36:18.777002+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=80611.6
- Funnel: target 1083 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +47.74% | $11,144,419.72 |
| AKE/USDT:USDT | +22.35% | $4,787,492.65 |
| AIN/USDT:USDT | +5.86% | $12,930,688.39 |
| CBRSSTOCK/USDT:USDT | +5.34% | $1,772,067.41 |
| LAB/USDT:USDT | +4.20% | $1,058,432.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.21% | +4.10% |
| AGT/USDT:USDT | below_1h_threshold | +2.19% | +2.09% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.15% | +2.05% |
| ZEC/USDT:USDT | below_1h_threshold | +1.80% | +1.70% |
| NEAR/USDT:USDT | below_1h_threshold | +1.67% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
