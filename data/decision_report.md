# Decision Report

- generated_at: 2026-06-12T08:04:09.800806+00:00
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

- 更新: 2026-06-12T08:04:07.125350+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=63109.4
- Funnel: target 779 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +106.51% | $141,866,916.65 |
| NAORIS/USDT:USDT | +39.12% | $2,455,105.10 |
| XPL/USDT:USDT | +38.48% | $7,906,342.54 |
| H/USDT:USDT | +33.29% | $43,763,612.13 |
| STG/USDT:USDT | +26.03% | $14,521,893.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +2.35% | +2.29% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.69% | +1.62% |
| VELVET/USDT:USDT | below_1h_threshold | +1.40% | +1.33% |
| XPL/USDT:USDT | below_1h_threshold | +1.04% | +0.97% |
| SOXL/USDT:USDT | below_1h_threshold | +1.01% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
