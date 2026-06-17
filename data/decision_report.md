# Decision Report

- generated_at: 2026-06-17T01:05:21.789327+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6892**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6892, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.94% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.15% | **+0.12%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 4/19 | 21.1% | -1.05% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$189.17** / 初期 $100.00 (+89.17%)
- 確定: 1765件 (Win 469 / Loss 553 / Flat 743) / skip 1688件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $189.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.82** / 初期 $100.00 (-2.18%)
- 確定: 165件 (Win 31 / Loss 31 / Flat 103) / skip 138件
- 成長率目線: 平均log -0.000134 / 幾何平均 -0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0471 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $97.82

## 5. Latest Market Context

- 更新: 2026-06-17T01:05:15.835086+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=65765.0
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +32.71% | $5,536,620.50 |
| SQD/USDT:USDT | +19.03% | $1,243,332.96 |
| VELVET/USDT:USDT | +16.38% | $29,530,563.51 |
| H/USDT:USDT | +15.89% | $55,388,783.28 |
| ESPORTS/USDT:USDT | +15.86% | $2,284,015.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.91% | +1.78% |
| SQD/USDT:USDT | below_1h_threshold | +1.16% | +1.03% |
| WLD/USDT:USDT | below_1h_threshold | +0.97% | +0.84% |
| SENT/USDT:USDT | below_1h_threshold | +0.94% | +0.81% |
| BR/USDT:USDT | below_1h_threshold | +0.80% | +0.67% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
