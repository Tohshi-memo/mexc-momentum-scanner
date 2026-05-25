# Decision Report

- generated_at: 2026-05-25T16:14:14.305940+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4862**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4862, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.89% | **-1.89%** |

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
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +4.40% | **+3.15%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.04% | **+2.82%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.86% | **+2.12%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.09% | **+1.85%** |
| ASK_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.89** / 初期 $100.00 (+29.89%)
- 確定: 668件 (Win 169 / Loss 210 / Flat 289) / skip 755件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $129.89

## 4. Latest Market Context

- 更新: 2026-05-25T16:14:11.742129+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=77500.5
- Funnel: target 765 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TONCOIN/USDT:USDT | +2.52% | $31,318,616.73 |
| GRASS/USDT:USDT | +2.16% | $3,741,881.57 |
| H/USDT:USDT | +2.03% | $2,026,144.52 |
| AGT/USDT:USDT | +1.68% | $2,022,990.60 |
| ORDI/USDT:USDT | +1.38% | $2,811,745.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +2.46% | +2.58% |
| GRASS/USDT:USDT | below_1h_threshold | +2.25% | +2.36% |
| H/USDT:USDT | below_1h_threshold | +2.04% | +2.15% |
| AGT/USDT:USDT | below_1h_threshold | +1.70% | +1.82% |
| NIL/USDT:USDT | below_1h_threshold | +1.44% | +1.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
