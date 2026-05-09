# Decision Report

- generated_at: 2026-05-09T02:22:20.868339+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3839**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3839, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.24% | **-2.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.46% | **+0.28%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.02% | **+0.01%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.08% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.03% | **+2.02%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.35% | **+1.74%** |
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.61% | **+1.57%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.85% | **+1.54%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.91% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 207件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T02:22:17.264343+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=80384.0
- Funnel: target 767 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +25.63% | $6,866,749.43 |
| ICP/USDT:USDT | +23.61% | $233,349,781.53 |
| DEEP/USDT:USDT | +22.04% | $1,286,097.41 |
| AGT/USDT:USDT | +19.67% | $6,726,422.61 |
| SIREN/USDT:USDT | +19.48% | $18,552,854.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +3.58% | +3.45% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.83% | +2.70% |
| JASMY/USDT:USDT | below_1h_threshold | +2.63% | +2.50% |
| BIO/USDT:USDT | below_1h_threshold | +2.31% | +2.18% |
| DYDX/USDT:USDT | below_1h_threshold | +1.57% | +1.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
