# Decision Report

- generated_at: 2026-05-17T20:23:24.534676+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4419**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4419, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.91% | **-0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +1.50% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.69% | **-0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.18% | **+2.22%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.47% | **+1.73%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.26% | **+1.47%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +3.01% | **+1.29%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.41% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.98** / 初期 $100.00 (+21.98%)
- 確定: 416件 (Win 109 / Loss 140 / Flat 167) / skip 564件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $121.98

## 4. Latest Market Context

- 更新: 2026-05-17T20:23:22.025922+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=78249.7
- Funnel: target 760 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +18.88% | $2,525,665.56 |
| UB/USDT:USDT | +14.58% | $13,132,551.02 |
| BUILDONBOB/USDT:USDT | +9.69% | $1,171,069.12 |
| BILL/USDT:USDT | +8.79% | $33,385,806.19 |
| HYPE/USDT:USDT | +6.13% | $256,591,464.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +3.87% | +4.02% |
| UB/USDT:USDT | below_1h_threshold | +2.84% | +2.99% |
| LYN/USDT:USDT | below_1h_threshold | +1.42% | +1.57% |
| AKT/USDT:USDT | below_1h_threshold | +1.13% | +1.28% |
| RIVER/USDT:USDT | below_1h_threshold | +0.45% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
