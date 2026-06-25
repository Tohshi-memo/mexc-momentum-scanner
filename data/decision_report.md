# Decision Report

- generated_at: 2026-06-25T06:03:22.348776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7529**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7529, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/15 | 20.0% | +1.63% | **+0.33%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.35% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.87% | **+2.32%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.68% | **+1.48%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.15% | **+1.26%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.35% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$221.45** / 初期 $100.00 (+121.45%)
- 確定: 2129件 (Win 629 / Loss 713 / Flat 787) / skip 1961件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $221.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 590件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T06:03:16.711891+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=61632.9
- Funnel: target 807 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +38.93% | $14,249,577.17 |
| H/USDT:USDT | +21.50% | $23,993,994.17 |
| KORU/USDT:USDT | +19.81% | $5,420,055.22 |
| MUSTOCK/USDT:USDT | +18.84% | $111,732,834.29 |
| RESOLV/USDT:USDT | +17.88% | $2,622,554.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.62% | +1.51% |
| ICP/USDT:USDT | below_1h_threshold | +1.52% | +1.41% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.20% | +1.09% |
| ENA/USDT:USDT | below_1h_threshold | +0.98% | +0.87% |
| FET/USDT:USDT | below_1h_threshold | +0.96% | +0.85% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
