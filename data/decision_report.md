# Decision Report

- generated_at: 2026-06-17T02:45:49.544248+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6897**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6897, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.18% | **-1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.11% | **+0.50%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.09% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.71% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$193.94** / 初期 $100.00 (+93.94%)
- 確定: 1770件 (Win 474 / Loss 553 / Flat 743) / skip 1688件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $193.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.76** / 初期 $100.00 (-0.24%)
- 確定: 170件 (Win 35 / Loss 31 / Flat 104) / skip 138件
- 成長率目線: 平均log -0.000014 / 幾何平均 -0.001% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0861 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $99.76

## 5. Latest Market Context

- 更新: 2026-06-17T02:45:42.338444+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=65825.0
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +36.33% | $7,437,499.39 |
| H/USDT:USDT | +34.45% | $57,726,340.60 |
| SQD/USDT:USDT | +20.76% | $1,357,464.12 |
| ESPORTS/USDT:USDT | +18.87% | $3,501,991.53 |
| UNI/USDT:USDT | +16.41% | $43,421,874.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +3.09% | +3.21% |
| XPL/USDT:USDT | below_1h_threshold | +3.00% | +3.12% |
| GRASS/USDT:USDT | below_1h_threshold | +2.64% | +2.76% |
| ROSE/USDT:USDT | below_1h_threshold | +1.65% | +1.76% |
| BLESS/USDT:USDT | below_1h_threshold | +1.40% | +1.51% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
