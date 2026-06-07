# Decision Report

- generated_at: 2026-06-07T20:54:22.140683+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5999**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=5999, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.76% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.09% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.69% | **+5.69%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.13% | **+0.79%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.56** / 初期 $100.00 (+51.56%)
- 確定: 1116件 (Win 271 / Loss 336 / Flat 509) / skip 1444件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $151.56

## 4. Latest Market Context

- 更新: 2026-06-07T20:54:18.636710+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.89% price=61851.5
- Funnel: target 768 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1, 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +23.44% | $3,581,886.89 |
| BEAT/USDT:USDT | +19.50% | $62,230,619.52 |
| BTW/USDT:USDT | +16.36% | $14,349,451.59 |
| EPIC/USDT:USDT | +14.38% | $1,307,894.09 |
| VELVET/USDT:USDT | +11.44% | $3,010,347.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.61% | +3.71% |
| PIPPIN/USDT:USDT | below_1h_threshold | +3.60% | +2.71% |
| BANK/USDT:USDT | below_1h_threshold | +2.43% | +1.53% |
| VELVET/USDT:USDT | below_1h_threshold | +2.23% | +1.34% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.10% | +1.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
