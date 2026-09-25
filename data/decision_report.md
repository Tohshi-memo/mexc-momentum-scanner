# Decision Report

- generated_at: 2026-09-25T16:01:18.558657+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15534**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15534, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.74% | **-1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +1.15% | **+0.81%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.96% | **+0.29%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.32% | **+0.22%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.16% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.80% | **+1.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.45% | **+1.09%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.72% | **+0.77%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,200.90** / 初期 $100.00 (+1100.90%)
- 確定: 5902件 (Win 1740 / Loss 1891 / Flat 2271) / skip 6193件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,200.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3467件 (Win 952 / Loss 793 / Flat 1722) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0248 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3833件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T16:01:07.357691+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=83808.3
- Funnel: target 1067 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +0.79% | $4,861,727.12 |
| ARK/USDT:USDT | +0.78% | $2,439,708.45 |
| NIL/USDT:USDT | +0.54% | $7,747,921.83 |
| BTW/USDT:USDT | +0.46% | $8,128,099.34 |
| FET/USDT:USDT | +0.29% | $24,387,198.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +0.86% | +0.80% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.82% | +0.76% |
| USELESS/USDT:USDT | below_1h_threshold | +0.80% | +0.74% |
| ARK/USDT:USDT | below_1h_threshold | +0.79% | +0.73% |
| NIL/USDT:USDT | below_1h_threshold | +0.55% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
