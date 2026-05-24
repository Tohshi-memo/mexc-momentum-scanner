# Decision Report

- generated_at: 2026-05-24T11:14:00.181262+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4819**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4819, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.20% | **+0.02%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.09% | **-0.07%** |
| LIMIT_BB3S | 4/17 | 23.5% | -1.89% | **-0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.15% | **+1.29%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.78% | **+0.71%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.53% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.76** / 初期 $100.00 (+22.76%)
- 確定: 625件 (Win 154 / Loss 197 / Flat 274) / skip 755件
- 成長率目線: 平均log +0.000328 / 幾何平均 +0.033% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $122.76

## 4. Latest Market Context

- 更新: 2026-05-24T11:13:58.046085+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=77280.8
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +50.51% | $3,407,762.14 |
| NIL/USDT:USDT | +27.77% | $3,448,271.51 |
| PLUME/USDT:USDT | +20.15% | $2,471,212.06 |
| PHA/USDT:USDT | +18.22% | $1,005,771.28 |
| UB/USDT:USDT | +17.42% | $2,148,449.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +1.86% | +1.70% |
| PLAY/USDT:USDT | below_1h_threshold | +1.52% | +1.37% |
| BILL/USDT:USDT | below_1h_threshold | +1.12% | +0.97% |
| GENIUS/USDT:USDT | below_1h_threshold | +0.82% | +0.67% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.67% | +0.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
