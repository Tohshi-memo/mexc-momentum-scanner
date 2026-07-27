# Decision Report

- generated_at: 2026-07-27T16:56:18.191827+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9637**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9637, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.16% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.23% | **+1.94%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.99% | **+1.19%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.12% | **+1.16%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.85% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$456.37** / 初期 $100.00 (+356.37%)
- 確定: 3427件 (Win 1085 / Loss 1116 / Flat 1226) / skip 2771件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INFQSTOCK/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $456.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1824件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0011 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.60** / 初期 $100.00 (+8.60%)
- 確定: 657件 (Win 217 / Loss 249 / Flat 191) / pending 5件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000355 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: INFQSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.31% 残高後 $108.60

## 6. Latest Market Context

- 更新: 2026-07-27T16:56:09.042739+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=64780.4
- Funnel: target 902 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +14.47% | $4,222,799.74 |
| JIMOTHY/USDT:USDT | +4.61% | $1,895,807.75 |
| ON/USDT:USDT | +3.69% | $8,687,859.60 |
| ACE/USDT:USDT | +3.22% | $1,189,545.65 |
| ALLO/USDT:USDT | +2.99% | $4,252,097.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.94% | +3.53% |
| ON/USDT:USDT | below_1h_threshold | +3.55% | +3.14% |
| ACE/USDT:USDT | below_1h_threshold | +3.22% | +2.82% |
| ALLO/USDT:USDT | below_1h_threshold | +2.99% | +2.58% |
| 4/USDT:USDT | below_1h_threshold | +2.40% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
