# Decision Report

- generated_at: 2026-05-25T16:04:39.468908+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4861**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4861, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-2.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.49% | **-2.49%** |

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
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +4.67% | **+3.50%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.76% | **+3.33%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.95% | **+2.72%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.90% | **+2.34%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +4.23% | **+1.69%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 667件 (Win 169 / Loss 209 / Flat 289) / skip 755件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NEAR/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-05-25T16:04:37.339670+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77546.3
- Funnel: target 765 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MYX/USDT:USDT | +2.86% | $1,412,403.93 |
| GRASS/USDT:USDT | +2.32% | $3,701,694.80 |
| BSB/USDT:USDT | +1.37% | $36,336,863.22 |
| BEAT/USDT:USDT | +0.95% | $30,205,615.06 |
| H/USDT:USDT | +0.81% | $2,011,524.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +3.11% | +3.17% |
| GRASS/USDT:USDT | below_1h_threshold | +2.25% | +2.30% |
| BEAT/USDT:USDT | below_1h_threshold | +0.95% | +1.00% |
| BSB/USDT:USDT | below_1h_threshold | +0.91% | +0.97% |
| H/USDT:USDT | below_1h_threshold | +0.81% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
