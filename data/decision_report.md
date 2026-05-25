# Decision Report

- generated_at: 2026-05-25T13:04:13.660376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4857**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4857, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-2.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.46% | **-2.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +1.01% | **+0.25%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.87% | **+0.17%** |
| LIMIT_8PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_10PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_9PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +6.84% | **+5.48%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +4.33% | **+2.82%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.53% | **+2.26%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.68% | **+2.21%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +4.18% | **+1.67%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.61** / 初期 $100.00 (+28.61%)
- 確定: 663件 (Win 167 / Loss 208 / Flat 288) / skip 755件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $128.61

## 4. Latest Market Context

- 更新: 2026-05-25T13:04:11.564302+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77362.0
- Funnel: target 764 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +54.49% | $12,383,039.43 |
| PHA/USDT:USDT | +32.32% | $1,478,336.25 |
| XAN/USDT:USDT | +30.55% | $7,291,198.97 |
| SAGA/USDT:USDT | +28.60% | $3,472,671.31 |
| SPORTFUN/USDT:USDT | +20.38% | $1,473,820.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +1.29% | +1.24% |
| IN/USDT:USDT | below_1h_threshold | +1.28% | +1.24% |
| XAN/USDT:USDT | below_1h_threshold | +1.25% | +1.20% |
| SAGA/USDT:USDT | below_1h_threshold | +0.86% | +0.82% |
| NIL/USDT:USDT | below_1h_threshold | +0.80% | +0.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
