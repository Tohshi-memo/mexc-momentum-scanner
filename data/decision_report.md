# Decision Report

- generated_at: 2026-06-18T10:04:13.831163+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7035**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7035, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.05% | **+0.01%** |
| LIMIT_ATR | 12/20 | 60.0% | -0.07% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +4.23% | **+1.06%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.78% | **+0.89%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.71%** |
| MARKET_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$216.79** / 初期 $100.00 (+116.79%)
- 確定: 1881件 (Win 530 / Loss 600 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MITO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $216.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 138件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0517 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T10:04:08.627772+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64158.5
- Funnel: target 793 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +75.59% | $44,584,372.53 |
| O/USDT:USDT | +72.65% | $4,625,194.92 |
| SYN/USDT:USDT | +64.79% | $6,198,144.74 |
| RE/USDT:USDT | +48.87% | $2,762,022.30 |
| HOME/USDT:USDT | +40.94% | $2,520,245.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +2.84% | +2.86% |
| EVAA/USDT:USDT | below_1h_threshold | +2.01% | +2.03% |
| CLO/USDT:USDT | below_1h_threshold | +1.65% | +1.68% |
| H/USDT:USDT | below_1h_threshold | +1.61% | +1.63% |
| SYN/USDT:USDT | below_1h_threshold | +1.57% | +1.60% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
