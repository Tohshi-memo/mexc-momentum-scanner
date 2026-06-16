# Decision Report

- generated_at: 2026-06-16T23:53:22.814829+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6889**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6889, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.92% | **+0.32%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.15% | **+0.12%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 5/18 | 27.8% | -1.36% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.78% | **+1.25%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.09% | **+0.87%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$186.36** / 初期 $100.00 (+86.36%)
- 確定: 1762件 (Win 466 / Loss 553 / Flat 743) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $186.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.75** / 初期 $100.00 (-2.25%)
- 確定: 162件 (Win 30 / Loss 31 / Flat 101) / skip 138件
- 成長率目線: 平均log -0.000141 / 幾何平均 -0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0247 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $97.75

## 5. Latest Market Context

- 更新: 2026-06-16T23:53:18.663114+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=65624.7
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +22.18% | $3,468,630.02 |
| H/USDT:USDT | +16.68% | $56,483,438.21 |
| VELVET/USDT:USDT | +16.25% | $30,873,538.30 |
| SQD/USDT:USDT | +15.75% | $1,043,367.66 |
| UAI/USDT:USDT | +11.36% | $1,904,596.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +1.55% | +1.73% |
| SQD/USDT:USDT | below_1h_threshold | +1.30% | +1.48% |
| WLD/USDT:USDT | below_1h_threshold | +0.94% | +1.12% |
| UNI/USDT:USDT | below_1h_threshold | +0.67% | +0.86% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.58% | +0.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
