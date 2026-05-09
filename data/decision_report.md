# Decision Report

- generated_at: 2026-05-09T03:52:59.752795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3851**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3851, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.06% | **-2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.35% | **+0.29%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.51% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +6.25% | **+2.19%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.93% | **+1.46%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.09% | **+1.25%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.51% | **+1.25%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +5.73% | **+1.15%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 219件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T03:52:53.366943+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80307.9
- Funnel: target 767 → liquid 178 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.3 >= 65=1, 4h RSI 84.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +27.59% | $4,284,771.63 |
| COLLECT/USDT:USDT | +25.63% | $7,388,856.27 |
| CORE/USDT:USDT | +21.55% | $1,965,564.74 |
| DEEP/USDT:USDT | +20.57% | $1,814,308.26 |
| ICP/USDT:USDT | +19.38% | $234,066,380.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +2.73% | +2.82% |
| MONAD/USDT:USDT | below_1h_threshold | +2.20% | +2.28% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.16% | +2.25% |
| BRETT/USDT:USDT | below_1h_threshold | +2.15% | +2.24% |
| GALA/USDT:USDT | below_1h_threshold | +2.06% | +2.14% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
