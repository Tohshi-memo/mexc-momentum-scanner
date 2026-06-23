# Decision Report

- generated_at: 2026-06-23T21:34:17.576013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7444**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=7444, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.82% | **+0.38%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.16% | **+0.16%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.23% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.03%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.03% | **+0.67%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.84% | **+0.55%** |
| MARKET_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |
| ASK_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$101.43** / 初期 $100.00 (+1.43%)
- 確定トレード: 30件 (TP 11 / SL 19 / EXP 0)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.43
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.71** / 初期 $100.00 (+128.71%)
- 確定: 2081件 (Win 617 / Loss 690 / Flat 774) / skip 1924件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $228.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 326件 (Win 92 / Loss 88 / Flat 146) / skip 529件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-23T21:34:13.035549+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=62535.4
- Funnel: target 802 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +39.29% | $5,891,879.87 |
| BEAT/USDT:USDT | +17.68% | $43,883,547.95 |
| ALLO/USDT:USDT | +8.42% | $4,917,693.10 |
| RAVE/USDT:USDT | +7.28% | $2,321,258.94 |
| DYDX/USDT:USDT | +7.20% | $3,023,376.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +4.38% | +4.23% |
| HEI/USDT:USDT | below_1h_threshold | +3.10% | +2.95% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.38% | +2.23% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.33% | +2.18% |
| JASMY/USDT:USDT | below_1h_threshold | +2.15% | +2.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
