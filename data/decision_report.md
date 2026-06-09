# Decision Report

- generated_at: 2026-06-09T08:17:52.024228+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6122**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6122, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.07% | **-1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.46% | **+1.36%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.20% | **+1.21%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.65% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$155.00** / 初期 $100.00 (+55.00%)
- 確定: 1162件 (Win 291 / Loss 357 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $155.00

## 4. Latest Market Context

- 更新: 2026-06-09T08:17:49.438778+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=62913.2
- Funnel: target 774 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +60.04% | $22,468,257.74 |
| SLX/USDT:USDT | +49.40% | $2,959,000.16 |
| POWER/USDT:USDT | +15.99% | $1,865,700.17 |
| LIGHT/USDT:USDT | +10.56% | $1,098,333.48 |
| SKHYNIXSTOCK/USDT:USDT | +9.10% | $4,295,242.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +3.14% | +3.54% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.08% | +2.49% |
| SLX/USDT:USDT | below_1h_threshold | +2.02% | +2.43% |
| POWER/USDT:USDT | below_1h_threshold | +2.01% | +2.42% |
| MOVE/USDT:USDT | below_1h_threshold | +1.43% | +1.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
