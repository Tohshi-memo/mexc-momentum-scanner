# Decision Report

- generated_at: 2026-05-19T21:13:45.400493+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4502**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4502, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_BB3S | 6/10 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.55% | **+0.52%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.74% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.54% | **+1.31%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.30% | **+1.27%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +5.83% | **+1.17%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.81% | **+0.91%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.45% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 590件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T21:13:42.321007+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=76981.0
- Funnel: target 759 → liquid 136 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.1 >= 65=1, 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +34.77% | $14,169,651.47 |
| PROMPT/USDT:USDT | +26.12% | $1,499,832.31 |
| BSB/USDT:USDT | +19.24% | $30,910,615.01 |
| VVV/USDT:USDT | +13.65% | $11,126,592.69 |
| BANANAS31/USDT:USDT | +13.03% | $1,144,206.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +0.91% | +0.90% |
| FIGHT/USDT:USDT | below_1h_threshold | +0.89% | +0.88% |
| PYTH/USDT:USDT | below_1h_threshold | +0.77% | +0.77% |
| CFX/USDT:USDT | below_1h_threshold | +0.63% | +0.63% |
| PENGU/USDT:USDT | below_1h_threshold | +0.52% | +0.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
