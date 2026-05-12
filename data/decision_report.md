# Decision Report

- generated_at: 2026-05-12T17:43:02.743282+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4149**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4149, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.38% | **-0.10%** |
| ASK | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.69% | **+1.53%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.92% | **+1.34%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.52% | **+1.01%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 285件 (Win 82 / Loss 96 / Flat 107) / skip 425件
- 成長率目線: 平均log +0.000683 / 幾何平均 +0.068% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-12T17:42:59.382464+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.56% price=80416.3
- Funnel: target 759 → liquid 194 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +22.81% | $3,674,172.32 |
| LAB/USDT:USDT | +7.47% | $172,384,789.49 |
| ESPORTS/USDT:USDT | +7.43% | $4,328,968.50 |
| IRYS/USDT:USDT | +6.83% | $2,080,717.67 |
| COAI/USDT:USDT | +5.00% | $1,150,330.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.96% | +3.40% |
| INJ/USDT:USDT | below_1h_threshold | +3.40% | +2.84% |
| KITE/USDT:USDT | below_1h_threshold | +3.11% | +2.55% |
| NEAR/USDT:USDT | below_1h_threshold | +3.00% | +2.44% |
| UB/USDT:USDT | below_1h_threshold | +2.81% | +2.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
