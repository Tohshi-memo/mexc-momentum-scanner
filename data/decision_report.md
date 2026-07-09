# Decision Report

- generated_at: 2026-07-09T07:40:51.043074+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8524**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=8524, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.27% | **+0.13%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +0.36% | **+0.13%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.19% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$104.09** / 初期 $100.00 (+4.09%)
- 確定トレード: 83件 (TP 30 / SL 52 / EXP 1)
- 最新: NES/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.26** / 初期 $100.00 (+221.26%)
- 確定: 2712件 (Win 857 / Loss 908 / Flat 947) / skip 2373件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $321.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1293件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-09T07:40:45.756254+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=62795.7
- Funnel: target 851 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +107.71% | $8,528,078.79 |
| SKYAI/USDT:USDT | +21.00% | $18,866,998.58 |
| VANRY/USDT:USDT | +19.00% | $8,036,094.05 |
| BASED/USDT:USDT | +14.20% | $2,581,721.41 |
| EGLD/USDT:USDT | +13.21% | $1,319,601.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.48% | +2.70% |
| CHIP/USDT:USDT | below_1h_threshold | +1.73% | +1.95% |
| EGLD/USDT:USDT | below_1h_threshold | +1.66% | +1.88% |
| SOXL/USDT:USDT | below_1h_threshold | +1.48% | +1.70% |
| TSEMSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
