# Decision Report

- generated_at: 2026-05-17T04:48:28.457828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4383**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4383, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.54% | **+0.41%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.88% | **+0.31%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.46% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.13% | **+0.79%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.27% | **+0.45%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.66% | **+0.30%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.42% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$97.19** / 初期 $100.00 (-2.81%)
- 確定トレード: 50件 (TP 13 / SL 34 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -3.29% 残高後 $97.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 551件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T04:48:24.710549+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=78150.0
- Funnel: target 760 → liquid 125 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +51.75% | $4,942,711.81 |
| CGPT/USDT:USDT | +31.36% | $1,581,175.84 |
| BSB/USDT:USDT | +14.45% | $4,348,241.34 |
| ASTEROID/USDT:USDT | +10.19% | $4,144,982.80 |
| VVV/USDT:USDT | +10.04% | $4,944,094.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.18% | +2.98% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.05% | +2.84% |
| VVV/USDT:USDT | below_1h_threshold | +2.92% | +2.71% |
| LAB/USDT:USDT | below_1h_threshold | +2.06% | +1.85% |
| ZEC/USDT:USDT | below_1h_threshold | +1.89% | +1.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
