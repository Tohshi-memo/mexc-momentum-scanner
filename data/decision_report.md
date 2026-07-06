# Decision Report

- generated_at: 2026-07-06T06:34:33.489738+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8375**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.13% / filled 20/20。**
- 全期間 MARKET基準: n=8375, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.13% | **+2.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.13% | **+2.13%** |
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.79% | **+1.34%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.02% | **-0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.01% | **-0.01%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$318.73** / 初期 $100.00 (+218.73%)
- 確定: 2622件 (Win 832 / Loss 886 / Flat 904) / skip 2314件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $318.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1147件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T06:34:28.478489+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=62953.1
- Funnel: target 836 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEROC0MPUTE/USDT:USDT | +19.06% | $1,619,190.65 |
| BILL/USDT:USDT | +14.90% | $1,715,632.88 |
| UB/USDT:USDT | +10.86% | $1,799,904.54 |
| TRB/USDT:USDT | +8.62% | $10,121,537.07 |
| GOAT/USDT:USDT | +8.50% | $1,021,076.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +3.19% | +3.40% |
| BASED/USDT:USDT | below_1h_threshold | +2.35% | +2.56% |
| BSB/USDT:USDT | below_1h_threshold | +2.18% | +2.39% |
| NES/USDT:USDT | below_1h_threshold | +2.15% | +2.36% |
| LIT/USDT:USDT | below_1h_threshold | +2.03% | +2.24% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
