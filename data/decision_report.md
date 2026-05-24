# Decision Report

- generated_at: 2026-05-24T23:09:19.778433+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4836**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4836, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.15% | **-0.09%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| ASK | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| MARKET_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| ASK_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.41** / 初期 $100.00 (+22.41%)
- 確定: 642件 (Win 158 / Loss 204 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000315 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $122.41

## 4. Latest Market Context

- 更新: 2026-05-24T23:09:17.696349+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=76878.9
- Funnel: target 764 → liquid 110 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SUPER/USDT:USDT | +7.63% | $3,137,177.01 |
| BILL/USDT:USDT | +2.33% | $14,388,678.42 |
| SILVER/USDT:USDT | +1.99% | $190,520,769.59 |
| NIL/USDT:USDT | +1.99% | $13,129,415.60 |
| SAGA/USDT:USDT | +1.73% | $1,349,988.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QNT/USDT:USDT | below_1h_threshold | +2.17% | +2.03% |
| AGT/USDT:USDT | below_1h_threshold | +1.88% | +1.74% |
| UB/USDT:USDT | below_1h_threshold | +1.63% | +1.49% |
| BEAT/USDT:USDT | below_1h_threshold | +1.43% | +1.29% |
| BILL/USDT:USDT | below_1h_threshold | +1.04% | +0.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
