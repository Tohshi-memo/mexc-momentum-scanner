# Decision Report

- generated_at: 2026-05-28T04:39:33.197056+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4953**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.89% / filled 20/20。**
- 全期間 MARKET基準: n=4953, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +4.50% | **+3.15%** |
| LIMIT_2PCT | 17/20 | 85.0% | +3.57% | **+3.03%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.27% | **+1.93%** |
| LIMIT_4PCT | 9/20 | 45.0% | +3.64% | **+1.64%** |
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.74% | **+1.43%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +3.14% | **+1.41%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.36% | **+1.18%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.15% | **+0.63%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.68% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$98.12** / 初期 $100.00 (-1.88%)
- 確定トレード: 69件 (TP 20 / SL 46 / EXP 3)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 688件 (Win 172 / Loss 220 / Flat 296) / skip 826件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T04:39:28.509710+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=73061.3
- Funnel: target 777 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +33.63% | $7,394,904.85 |
| BILL/USDT:USDT | +11.61% | $8,049,843.67 |
| NBISSTOCK/USDT:USDT | +11.31% | $1,619,287.58 |
| BUILDONBOB/USDT:USDT | +7.63% | $1,054,070.18 |
| XLM/USDT:USDT | +5.97% | $89,040,795.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.94% | +3.16% |
| UB/USDT:USDT | below_1h_threshold | +1.79% | +2.02% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.84% | +1.07% |
| XLM/USDT:USDT | below_1h_threshold | +0.56% | +0.78% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.56% | +0.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
