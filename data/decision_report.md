# Decision Report

- generated_at: 2026-05-24T11:34:14.079445+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4820**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4820, expectancy=-0.09%
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

- 残高: **$123.98** / 初期 $100.00 (+23.98%)
- 確定: 626件 (Win 155 / Loss 197 / Flat 274) / skip 755件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $123.98

## 4. Latest Market Context

- 更新: 2026-05-24T11:34:11.975788+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=77268.7
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +55.38% | $3,665,712.62 |
| NIL/USDT:USDT | +26.43% | $3,762,620.55 |
| BLUAI/USDT:USDT | +18.57% | $1,788,634.49 |
| PLUME/USDT:USDT | +18.56% | $2,510,715.35 |
| PHA/USDT:USDT | +17.42% | $1,021,699.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.48% | +4.34% |
| BILL/USDT:USDT | below_1h_threshold | +2.77% | +2.64% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.46% | +1.33% |
| NEAR/USDT:USDT | below_1h_threshold | +1.40% | +1.27% |
| LIT/USDT:USDT | below_1h_threshold | +1.16% | +1.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
