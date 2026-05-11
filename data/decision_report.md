# Decision Report

- generated_at: 2026-05-11T11:47:48.568443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4027**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4027, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.82% | **+0.66%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.65% | **+0.42%** |
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.18% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.79% | **+0.39%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.71% | **+0.37%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.67% | **+0.34%** |
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.28% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 370件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T11:47:45.409702+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=81097.0
- Funnel: target 762 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +39.01% | $13,465,115.74 |
| PENGUIN/USDT:USDT | +37.91% | $1,104,672.07 |
| SAGA/USDT:USDT | +32.16% | $3,133,894.56 |
| B/USDT:USDT | +28.42% | $11,120,223.34 |
| TROLLSOL/USDT:USDT | +19.66% | $4,539,580.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_relative_strength | +5.02% | +4.78% |
| BANANAS31/USDT:USDT | below_1h_threshold | +3.58% | +3.33% |
| PENGUIN/USDT:USDT | below_1h_threshold | +3.44% | +3.20% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.92% | +2.68% |
| ICP/USDT:USDT | below_1h_threshold | +2.40% | +2.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
