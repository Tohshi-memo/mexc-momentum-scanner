# Decision Report

- generated_at: 2026-07-06T11:34:25.875616+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8384**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.02% / filled 20/20。**
- 全期間 MARKET基準: n=8384, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_BB3S | 6/16 | 37.5% | +2.45% | **+0.92%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +3.27% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| ASK_LONG | 20/20 | 100.0% | +0.13% | **+0.13%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.13** / 初期 $100.00 (+217.13%)
- 確定: 2623件 (Win 832 / Loss 887 / Flat 904) / skip 2322件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $317.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1156件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T11:34:20.685170+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=62947.3
- Funnel: target 841 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VANRY/USDT:USDT | +25.43% | $8,410,140.47 |
| ZEROC0MPUTE/USDT:USDT | +21.11% | $1,563,417.79 |
| YFI/USDT:USDT | +19.20% | $2,436,379.23 |
| BEL/USDT:USDT | +15.91% | $1,958,942.04 |
| DEXE/USDT:USDT | +13.16% | $1,630,745.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| YFI/USDT:USDT | below_1h_threshold | +3.53% | +3.29% |
| TRIA/USDT:USDT | below_1h_threshold | +3.10% | +2.86% |
| VANRY/USDT:USDT | below_1h_threshold | +1.47% | +1.23% |
| TRB/USDT:USDT | below_1h_threshold | +1.23% | +0.99% |
| BILL/USDT:USDT | below_1h_threshold | +0.98% | +0.74% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
