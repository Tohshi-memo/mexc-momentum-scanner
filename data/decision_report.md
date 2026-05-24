# Decision Report

- generated_at: 2026-05-24T22:04:08.287292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4834**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4834, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.07% | **-0.04%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.60% | **-0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.41% | **+0.70%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.20** / 初期 $100.00 (+22.20%)
- 確定: 640件 (Win 157 / Loss 203 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $122.20

## 4. Latest Market Context

- 更新: 2026-05-24T22:04:06.162306+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.57% price=76537.3
- Funnel: target 764 → liquid 109 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SUPER/USDT:USDT | +9.83% | $2,821,259.42 |
| NIL/USDT:USDT | +3.71% | $12,822,130.82 |
| BILL/USDT:USDT | +1.65% | $13,510,141.47 |
| SAGA/USDT:USDT | +1.31% | $1,360,291.73 |
| LUNC/USDT:USDT | +1.08% | $2,808,985.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SILVER/USDT:USDT | below_1h_threshold | +1.53% | +0.96% |
| ATOM/USDT:USDT | below_1h_threshold | +1.44% | +0.88% |
| NEAR/USDT:USDT | below_1h_threshold | +1.42% | +0.85% |
| SAGA/USDT:USDT | below_1h_threshold | +1.37% | +0.80% |
| INJ/USDT:USDT | below_1h_threshold | +1.26% | +0.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
