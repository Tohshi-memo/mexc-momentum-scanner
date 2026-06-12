# Decision Report

- generated_at: 2026-06-12T07:51:58.257430+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6482**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6482, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/20 | 15.0% | +3.20% | **+0.48%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.21% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.23% | **+1.67%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +4.36% | **+1.53%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +5.98% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.78** / 初期 $100.00 (+64.78%)
- 確定: 1357件 (Win 367 / Loss 434 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HMSTR/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $164.78

## 4. Latest Market Context

- 更新: 2026-06-12T07:51:54.382047+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=62989.0
- Funnel: target 779 → liquid 156 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1, 4h RSI 71.1 >= 65=1, 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +105.97% | $143,746,167.31 |
| NAORIS/USDT:USDT | +41.95% | $2,365,103.47 |
| ESPORTS/USDT:USDT | +36.61% | $35,550,089.36 |
| XPL/USDT:USDT | +34.22% | $7,612,572.34 |
| H/USDT:USDT | +32.89% | $44,828,346.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.43% | +4.38% |
| LAB/USDT:USDT | below_1h_threshold | +3.11% | +3.06% |
| CLO/USDT:USDT | below_1h_threshold | +2.78% | +2.73% |
| PYTH/USDT:USDT | below_1h_threshold | +2.50% | +2.45% |
| XPL/USDT:USDT | below_1h_threshold | +2.39% | +2.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
