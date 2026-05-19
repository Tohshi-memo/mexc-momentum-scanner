# Decision Report

- generated_at: 2026-05-19T19:08:37.474726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4495**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4495, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +1.93% | **+0.97%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.65% | **+0.32%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.24% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +3.39% | **+1.69%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.01% | **+1.51%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.93% | **+1.47%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.68% | **+1.26%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.53% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 583件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T19:08:34.943595+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=76875.5
- Funnel: target 760 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +63.76% | $17,336,105.73 |
| EDEN/USDT:USDT | +35.63% | $10,900,779.07 |
| VVV/USDT:USDT | +13.85% | $9,061,656.97 |
| LIT/USDT:USDT | +8.44% | $1,993,026.18 |
| SKYAI/USDT:USDT | +7.97% | $4,582,505.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.50% | +2.36% |
| VVV/USDT:USDT | below_1h_threshold | +1.56% | +1.41% |
| FIDA/USDT:USDT | below_1h_threshold | +1.27% | +1.13% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.82% | +0.67% |
| RIVER/USDT:USDT | below_1h_threshold | +0.82% | +0.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
