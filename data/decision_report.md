# Decision Report

- generated_at: 2026-06-25T01:17:13.530625+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7513**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7513, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.52% | **-2.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.32% | **+0.11%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.20% | **-0.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -2.14% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +4.23% | **+2.75%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.45% | **+2.58%** |
| MARKET_LONG | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.90% | **+2.15%** |
| ASK_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |

## 2. $100 Live Portfolio

- 残高: **$103.45** / 初期 $100.00 (+3.45%)
- 確定トレード: 38件 (TP 15 / SL 23 / EXP 0)
- 最新: ARMSTOCK/USDT:USDT TP_HIT PnL +7.19% 残高後 $103.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.57** / 初期 $100.00 (+122.57%)
- 確定: 2122件 (Win 627 / Loss 710 / Flat 785) / skip 1952件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $222.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 574件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T01:17:08.965922+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=60760.2
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +19.77% | $10,865,049.04 |
| O/USDT:USDT | +17.55% | $10,984,962.97 |
| KORU/USDT:USDT | +14.79% | $5,656,997.87 |
| MUSTOCK/USDT:USDT | +14.45% | $97,517,556.66 |
| BSB/USDT:USDT | +13.21% | $6,288,708.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.95% | +5.00% |
| SLX/USDT:USDT | below_1h_threshold | +3.60% | +3.64% |
| MVLL/USDT:USDT | below_1h_threshold | +2.06% | +2.10% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.94% | +1.98% |
| BSB/USDT:USDT | below_1h_threshold | +1.91% | +1.95% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
