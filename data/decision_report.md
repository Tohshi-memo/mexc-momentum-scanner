# Decision Report

- generated_at: 2026-05-24T18:19:14.737632+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4831**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4831, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.10% | **-0.06%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -1.16% | **-0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.33% | **+5.33%** |
| ASK_LONG | 20/20 | 100.0% | +1.71% | **+1.71%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.48% | **+1.24%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.29** / 初期 $100.00 (+22.29%)
- 確定: 637件 (Win 156 / Loss 201 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $122.29

## 4. Latest Market Context

- 更新: 2026-05-24T18:19:12.602529+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=76750.3
- Funnel: target 764 → liquid 112 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +9.77% | $9,460,517.36 |
| BEAT/USDT:USDT | +7.13% | $37,840,671.92 |
| UB/USDT:USDT | +5.91% | $3,521,326.93 |
| MYX/USDT:USDT | +3.17% | $2,991,813.54 |
| PHA/USDT:USDT | +2.91% | $1,316,477.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNC/USDT:USDT | below_1h_threshold | +1.64% | +1.52% |
| GMTTOKEN/USDT:USDT | below_1h_threshold | +1.18% | +1.06% |
| NIL/USDT:USDT | below_1h_threshold | +1.01% | +0.90% |
| UB/USDT:USDT | below_1h_threshold | +0.82% | +0.70% |
| IP/USDT:USDT | below_1h_threshold | +0.69% | +0.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
