# Decision Report

- generated_at: 2026-09-18T08:06:18.219097+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14878**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14878, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.64% | **-0.10%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.31% | **+1.62%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +2.01% | **+1.26%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +2.67% | **+0.40%** |
| LIMIT_2PCT_LONG | 7/20 | 35.0% | +0.75% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5604件 (Win 1679 / Loss 1814 / Flat 2111) / skip 5835件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.37** / 初期 $100.00 (+143.37%)
- 確定: 3167件 (Win 878 / Loss 755 / Flat 1534) / skip 5122件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0982 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $243.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.32** / 初期 $100.00 (+23.32%)
- 確定: 2960件 (Win 878 / Loss 1166 / Flat 916) / pending 0件 / skip 3391件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.32

## 6. Latest Market Context

- 更新: 2026-09-18T08:06:08.197749+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77841.0
- Funnel: target 1047 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| G/USDT:USDT | +61.35% | $4,414,233.02 |
| CNPY/USDT:USDT | +37.91% | $3,696,410.60 |
| ONE/USDT:USDT | +32.97% | $54,221,885.75 |
| ARB/USDT:USDT | +25.27% | $109,349,876.77 |
| UNI/USDT:USDT | +22.77% | $73,511,831.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_1h_threshold | +3.70% | +3.61% |
| ONE/USDT:USDT | below_1h_threshold | +1.54% | +1.45% |
| ARB/USDT:USDT | below_1h_threshold | +1.04% | +0.95% |
| AERO/USDT:USDT | below_1h_threshold | +0.79% | +0.70% |
| APT/USDT:USDT | below_1h_threshold | +0.66% | +0.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
