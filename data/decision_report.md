# Decision Report

- generated_at: 2026-06-13T01:43:43.914846+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6556**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.82% / filled 20/20。**
- 全期間 MARKET基準: n=6556, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+3.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.82% | **+3.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.82% | **+3.82%** |
| ASK | 20/20 | 100.0% | +3.28% | **+3.28%** |
| LIMIT_1PCT | 13/20 | 65.0% | +2.39% | **+1.55%** |
| LIMIT_ATR | 4/20 | 20.0% | +4.72% | **+0.94%** |
| LIMIT_2PCT | 10/20 | 50.0% | +1.82% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.97% | **-0.29%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -1.56% | **-0.94%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1429件 (Win 389 / Loss 464 / Flat 576) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +1.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T01:43:40.123573+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=63757.0
- Funnel: target 774 → liquid 157 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDGE/USDT:USDT | +19.12% | $1,214,680.40 |
| ESPORTS/USDT:USDT | +15.23% | $65,010,420.58 |
| RIF/USDT:USDT | +15.16% | $1,216,617.66 |
| SQD/USDT:USDT | +13.98% | $1,021,258.08 |
| H/USDT:USDT | +11.88% | $28,286,573.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +2.64% | +2.35% |
| ORDI/USDT:USDT | below_1h_threshold | +2.34% | +2.04% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.58% | +1.28% |
| WLD/USDT:USDT | below_1h_threshold | +1.55% | +1.25% |
| APT/USDT:USDT | below_1h_threshold | +1.45% | +1.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
