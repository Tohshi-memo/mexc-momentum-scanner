# Decision Report

- generated_at: 2026-06-23T04:46:30.056108+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7410**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7410, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +0.33% | **+0.07%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.83% | **+1.72%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.37% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.22% | **+1.13%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.03** / 初期 $100.00 (+135.03%)
- 確定: 2066件 (Win 614 / Loss 680 / Flat 772) / skip 1905件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $235.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 313件 (Win 89 / Loss 87 / Flat 137) / skip 508件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0261 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-23T04:46:25.572593+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=63788.3
- Funnel: target 809 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARX/USDT:USDT | +56.87% | $10,486,133.68 |
| CLO/USDT:USDT | +27.09% | $3,550,350.28 |
| FOLKS/USDT:USDT | +14.38% | $6,252,484.98 |
| LAB/USDT:USDT | +12.94% | $30,804,325.54 |
| ID/USDT:USDT | +9.90% | $2,843,723.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAYER/USDT:USDT | below_1h_threshold | +4.23% | +4.62% |
| BASED/USDT:USDT | below_1h_threshold | +3.21% | +3.60% |
| ID/USDT:USDT | below_1h_threshold | +3.09% | +3.48% |
| SAGA/USDT:USDT | below_1h_threshold | +2.31% | +2.69% |
| GRAM/USDT:USDT | below_1h_threshold | +2.17% | +2.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
