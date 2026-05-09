# Decision Report

- generated_at: 2026-05-09T02:32:42.859272+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3841**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3841, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.73% | **+0.26%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.18% | **+0.15%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.30% | **+1.82%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.42% | **+1.54%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.39% | **+1.35%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.98% | **+1.34%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +4.88% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 209件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T02:32:39.207614+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80400.1
- Funnel: target 767 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +25.66% | $6,895,719.76 |
| SATO/USDT:USDT | +23.19% | $3,945,036.64 |
| ICP/USDT:USDT | +22.11% | $233,733,836.83 |
| DEEP/USDT:USDT | +21.09% | $1,376,858.72 |
| SIREN/USDT:USDT | +18.29% | $18,917,644.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.39% | +4.24% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.85% | +2.70% |
| JASMY/USDT:USDT | below_1h_threshold | +2.24% | +2.09% |
| JUP/USDT:USDT | below_1h_threshold | +2.20% | +2.05% |
| ZEC/USDT:USDT | below_1h_threshold | +1.79% | +1.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
