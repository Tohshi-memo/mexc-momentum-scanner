# Decision Report

- generated_at: 2026-11-02T00:01:21.199262+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18000**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18000, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.40% | **+1.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.96% | **+1.19%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.93% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.19% | **+1.86%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.74% | **+1.42%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.85% | **+1.29%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.83% | **+1.19%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,530.47** / 初期 $100.00 (+1430.47%)
- 確定: 6852件 (Win 1989 / Loss 2202 / Flat 2661) / skip 7709件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,530.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.35** / 初期 $100.00 (+281.35%)
- 確定: 4440件 (Win 1192 / Loss 986 / Flat 2262) / skip 6971件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1336 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $381.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6158件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000294 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T00:01:08.170167+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78377.9
- Funnel: target 1088 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +27.37% | $11,833,855.28 |
| BEAMX/USDT:USDT | +20.74% | $4,051,549.41 |
| LYN/USDT:USDT | +19.87% | $1,372,634.13 |
| ESPORTS/USDT:USDT | +10.95% | $10,079,651.43 |
| AIN/USDT:USDT | +5.90% | $14,972,059.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +1.53% | +1.45% |
| BEAMX/USDT:USDT | below_1h_threshold | +1.46% | +1.38% |
| MUU/USDT:USDT | below_1h_threshold | +1.45% | +1.36% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.11% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.04% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
