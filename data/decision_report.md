# Decision Report

- generated_at: 2026-06-18T13:14:47.486633+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7046**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7046, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.06% | **+0.03%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.62% | **+1.45%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.55% | **+1.17%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.76% | **+1.14%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.14%** |
| ASK_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$100.46** / 初期 $100.00 (+0.46%)
- 確定トレード: 14件 (TP 5 / SL 9 / EXP 0)
- 最新: ALLO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.71** / 初期 $100.00 (+115.71%)
- 確定: 1882件 (Win 530 / Loss 601 / Flat 751) / skip 1725件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $215.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 149件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0876 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T13:14:42.216794+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64372.9
- Funnel: target 795 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +90.57% | $11,204,159.53 |
| O/USDT:USDT | +74.85% | $6,578,302.53 |
| H/USDT:USDT | +35.34% | $33,504,324.51 |
| GUA/USDT:USDT | +24.04% | $2,653,647.13 |
| FOLKS/USDT:USDT | +20.75% | $4,253,316.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +3.83% | +3.79% |
| GUN/USDT:USDT | below_1h_threshold | +2.64% | +2.60% |
| UP/USDT:USDT | below_1h_threshold | +2.02% | +1.98% |
| SIREN/USDT:USDT | below_1h_threshold | +1.99% | +1.95% |
| MITO/USDT:USDT | below_1h_threshold | +1.74% | +1.70% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
