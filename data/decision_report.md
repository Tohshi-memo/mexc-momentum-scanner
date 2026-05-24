# Decision Report

- generated_at: 2026-05-24T11:49:02.966215+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4821**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4821, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.03% | **+0.15%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.29% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.60% | **+1.69%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.18% | **+1.09%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.36** / 初期 $100.00 (+23.36%)
- 確定: 627件 (Win 155 / Loss 198 / Flat 274) / skip 755件
- 成長率目線: 平均log +0.000335 / 幾何平均 +0.033% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLUME/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $123.36

## 4. Latest Market Context

- 更新: 2026-05-24T11:48:58.706587+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=77246.7
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +57.74% | $3,783,406.70 |
| NIL/USDT:USDT | +25.34% | $3,908,851.51 |
| BLUAI/USDT:USDT | +19.05% | $1,795,639.88 |
| PLUME/USDT:USDT | +18.41% | $2,539,019.55 |
| PHA/USDT:USDT | +17.24% | $1,029,953.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.93% | +3.83% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.91% | +1.80% |
| AGT/USDT:USDT | below_1h_threshold | +1.77% | +1.66% |
| LIT/USDT:USDT | below_1h_threshold | +1.26% | +1.16% |
| ZEC/USDT:USDT | below_1h_threshold | +1.22% | +1.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
