# Decision Report

- generated_at: 2026-06-09T13:47:34.486150+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6139**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=6139, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.89% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.64% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.86% | **+0.56%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.43% | **+0.21%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.20% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.38** / 初期 $100.00 (+50.38%)
- 確定: 1179件 (Win 296 / Loss 369 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $150.38

## 4. Latest Market Context

- 更新: 2026-06-09T13:47:32.477323+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=62362.8
- Funnel: target 774 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +42.99% | $23,622,594.25 |
| SLX/USDT:USDT | +30.48% | $5,590,453.80 |
| JCT/USDT:USDT | +29.09% | $1,092,629.90 |
| POWER/USDT:USDT | +21.65% | $3,901,176.84 |
| IO/USDT:USDT | +20.30% | $1,011,010.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.98% | +5.38% |
| BSB/USDT:USDT | below_1h_threshold | +4.56% | +4.95% |
| BTW/USDT:USDT | below_1h_threshold | +3.83% | +4.23% |
| CTR/USDT:USDT | below_1h_threshold | +3.75% | +4.14% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.57% | +3.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
