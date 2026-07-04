# Decision Report

- generated_at: 2026-07-04T04:19:26.115341+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8218**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8218, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.90% | **+0.30%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| ASK_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.49% | **+1.12%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.01% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$305.10** / 初期 $100.00 (+205.10%)
- 確定: 2535件 (Win 787 / Loss 844 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $305.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.11** / 初期 $100.00 (+7.11%)
- 確定: 614件 (Win 149 / Loss 148 / Flat 317) / skip 1015件
- 成長率目線: 平均log +0.000112 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0787 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $107.11

## 5. Latest Market Context

- 更新: 2026-07-04T04:19:18.928373+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=62579.3
- Funnel: target 834 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +87.14% | $4,190,103.87 |
| TLM/USDT:USDT | +42.27% | $39,687,472.70 |
| HMSTR/USDT:USDT | +36.04% | $2,670,253.31 |
| BAS/USDT:USDT | +29.89% | $4,147,298.44 |
| MAGMA/USDT:USDT | +23.87% | $15,055,505.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +4.39% | +4.44% |
| ANSEM/USDT:USDT | below_1h_threshold | +3.88% | +3.93% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.46% | +3.51% |
| BASED/USDT:USDT | below_1h_threshold | +3.09% | +3.14% |
| SPX/USDT:USDT | below_1h_threshold | +2.96% | +3.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
