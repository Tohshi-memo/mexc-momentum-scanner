# Decision Report

- generated_at: 2026-06-10T19:25:49.509043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6248**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6248, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.07% | **-0.02%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.46% | **+1.46%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.99% | **+0.39%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +1.19% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.49** / 初期 $100.00 (+50.49%)
- 確定: 1236件 (Win 308 / Loss 384 / Flat 544) / skip 1573件
- 成長率目線: 平均log +0.000331 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $150.49

## 4. Latest Market Context

- 更新: 2026-06-10T19:25:45.516396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=61728.9
- Funnel: target 785 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1, 4h RSI 84.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +55.16% | $20,978,125.60 |
| FOLKS/USDT:USDT | +18.11% | $8,146,835.01 |
| BEAT/USDT:USDT | +13.64% | $118,529,398.79 |
| ESPORTS/USDT:USDT | +12.61% | $25,242,022.56 |
| JCT/USDT:USDT | +8.41% | $2,509,265.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +3.75% | +3.95% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.33% | +3.53% |
| BSB/USDT:USDT | below_1h_threshold | +2.35% | +2.55% |
| BTW/USDT:USDT | below_1h_threshold | +2.17% | +2.36% |
| HOME/USDT:USDT | below_1h_threshold | +1.38% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
