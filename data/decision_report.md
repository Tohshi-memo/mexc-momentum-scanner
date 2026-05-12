# Decision Report

- generated_at: 2026-05-12T09:37:50.895553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4106**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4106, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.91% | **+0.57%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.67% | **+3.67%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.75% | **+2.06%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.25% | **+1.12%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.70% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$113.04** / 初期 $100.00 (+13.04%)
- 確定: 242件 (Win 65 / Loss 83 / Flat 94) / skip 425件
- 成長率目線: 平均log +0.000507 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $113.04

## 4. Latest Market Context

- 更新: 2026-05-12T09:37:47.401215+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=80884.0
- Funnel: target 762 → liquid 193 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.8 >= 65=1, 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +61.12% | $4,229,075.61 |
| SAGA/USDT:USDT | +42.47% | $12,160,608.06 |
| USELESS/USDT:USDT | +38.55% | $7,070,527.10 |
| SKYAI/USDT:USDT | +35.38% | $43,955,666.23 |
| IRYS/USDT:USDT | +30.95% | $1,153,109.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.71% | +4.61% |
| USELESS/USDT:USDT | below_1h_threshold | +4.15% | +4.05% |
| IRYS/USDT:USDT | below_1h_threshold | +2.63% | +2.53% |
| UP/USDT:USDT | below_1h_threshold | +2.36% | +2.25% |
| FF/USDT:USDT | below_1h_threshold | +2.13% | +2.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
