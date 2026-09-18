# Decision Report

- generated_at: 2026-09-18T06:21:25.027490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14868**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=14868, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.39% | **+0.35%** |
| LIMIT_BB3S | 6/16 | 37.5% | +0.65% | **+0.24%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.43% | **+0.29%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.33% | **+0.16%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | -0.00% | **-0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.04% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5604件 (Win 1679 / Loss 1814 / Flat 2111) / skip 5825件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.81** / 初期 $100.00 (+143.81%)
- 確定: 3157件 (Win 877 / Loss 753 / Flat 1527) / skip 5122件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1087 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $243.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.32** / 初期 $100.00 (+23.32%)
- 確定: 2960件 (Win 878 / Loss 1166 / Flat 916) / pending 0件 / skip 3380件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000397 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.32

## 6. Latest Market Context

- 更新: 2026-09-18T06:21:14.289334+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77476.0
- Funnel: target 1054 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +42.44% | $52,658,686.57 |
| CNPY/USDT:USDT | +30.08% | $3,549,920.89 |
| ARB/USDT:USDT | +23.83% | $105,128,667.56 |
| NEAR/USDT:USDT | +20.25% | $138,076,663.28 |
| UNI/USDT:USDT | +18.87% | $70,780,439.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| G/USDT:USDT | below_1h_threshold | +2.41% | +2.39% |
| LIT/USDT:USDT | below_1h_threshold | +2.06% | +2.03% |
| AERO/USDT:USDT | below_1h_threshold | +1.57% | +1.54% |
| COTI/USDT:USDT | below_1h_threshold | +1.36% | +1.34% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.25% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
