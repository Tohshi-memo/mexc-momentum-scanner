# Decision Report

- generated_at: 2026-05-12T09:28:02.287926+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4105**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4105, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.76% | **+0.44%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.75% | **-0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.67% | **+3.67%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.96% | **+2.37%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.16% | **+1.40%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.45% | **+1.37%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$113.04** / 初期 $100.00 (+13.04%)
- 確定: 241件 (Win 65 / Loss 83 / Flat 93) / skip 425件
- 成長率目線: 平均log +0.000509 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KITE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.11% 残高後 $113.04

## 4. Latest Market Context

- 更新: 2026-05-12T09:27:58.971000+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80676.7
- Funnel: target 762 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +58.40% | $3,937,391.86 |
| SAGA/USDT:USDT | +42.14% | $12,030,988.58 |
| USELESS/USDT:USDT | +36.10% | $6,818,179.00 |
| SKYAI/USDT:USDT | +34.24% | $43,815,761.04 |
| IRYS/USDT:USDT | +31.23% | $1,129,358.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_1h_threshold | +3.84% | +4.00% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.81% | +3.97% |
| UP/USDT:USDT | below_1h_threshold | +3.17% | +3.32% |
| IRYS/USDT:USDT | below_1h_threshold | +2.85% | +3.01% |
| SAPIEN/USDT:USDT | below_1h_threshold | +2.55% | +2.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
