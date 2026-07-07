# Decision Report

- generated_at: 2026-07-07T01:48:57.653951+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8414**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=8414, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| ASK | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_BB3S | 5/11 | 45.5% | +0.84% | **+0.38%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.17% | **+0.29%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| MARKET_LONG | 20/20 | 100.0% | +0.10% | **+0.10%** |
| ASK_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | -0.05% | **-0.03%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.05% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.13** / 初期 $100.00 (+217.13%)
- 確定: 2626件 (Win 833 / Loss 888 / Flat 905) / skip 2349件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDGE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $317.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1186件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T01:48:52.245148+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=63985.1
- Funnel: target 841 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +20.77% | $2,169,062.87 |
| BLUR/USDT:USDT | +19.57% | $6,123,702.75 |
| EDGE/USDT:USDT | +14.27% | $3,046,968.34 |
| ANSEM/USDT:USDT | +13.91% | $5,579,365.97 |
| ALLO/USDT:USDT | +13.70% | $18,594,478.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +4.04% | +4.34% |
| RIF/USDT:USDT | below_1h_threshold | +1.97% | +2.26% |
| AERO/USDT:USDT | below_1h_threshold | +1.69% | +1.98% |
| NES/USDT:USDT | below_1h_threshold | +0.89% | +1.19% |
| BEAT/USDT:USDT | below_1h_threshold | +0.88% | +1.17% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
