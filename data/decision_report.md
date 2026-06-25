# Decision Report

- generated_at: 2026-06-25T01:25:25.039750+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7514**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7514, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.52% | **-2.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.05% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.03% | **+0.00%** |
| LIMIT_FIB1272 | 15/20 | 75.0% | -0.49% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.37% | **+3.06%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.55% | **+2.84%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +4.08% | **+2.45%** |
| MARKET_LONG | 20/20 | 100.0% | +1.96% | **+1.96%** |
| ASK_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |

## 2. $100 Live Portfolio

- 残高: **$103.45** / 初期 $100.00 (+3.45%)
- 確定トレード: 38件 (TP 15 / SL 23 / EXP 0)
- 最新: ARMSTOCK/USDT:USDT TP_HIT PnL +7.19% 残高後 $103.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.68** / 初期 $100.00 (+123.68%)
- 確定: 2123件 (Win 628 / Loss 710 / Flat 785) / skip 1952件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $223.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 575件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T01:25:19.475397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=60850.1
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +17.90% | $10,925,832.11 |
| O/USDT:USDT | +15.05% | $11,034,714.58 |
| KORU/USDT:USDT | +14.69% | $5,707,177.24 |
| MUSTOCK/USDT:USDT | +14.63% | $97,758,720.18 |
| BSB/USDT:USDT | +12.86% | $6,314,861.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ID/USDT:USDT | below_1h_threshold | +3.44% | +3.34% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.65% | +2.55% |
| MVLL/USDT:USDT | below_1h_threshold | +2.55% | +2.45% |
| SLX/USDT:USDT | below_1h_threshold | +1.98% | +1.87% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.69% | +1.59% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
