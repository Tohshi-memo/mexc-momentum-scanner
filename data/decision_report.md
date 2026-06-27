# Decision Report

- generated_at: 2026-06-27T02:08:18.893510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7665**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7665, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.39% | **-1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.03% | **+0.01%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.23% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.19% | **+1.44%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.19% | **+1.20%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.70% | **+0.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$234.60** / 初期 $100.00 (+134.60%)
- 確定: 2190件 (Win 654 / Loss 729 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TIA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $234.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.83** / 初期 $100.00 (+7.83%)
- 確定: 396件 (Win 106 / Loss 100 / Flat 190) / skip 680件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TIA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.83

## 5. Latest Market Context

- 更新: 2026-06-27T02:08:14.323996+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=59967.3
- Funnel: target 806 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +42.43% | $4,120,825.12 |
| MYX/USDT:USDT | +28.82% | $2,585,153.56 |
| AGLD/USDT:USDT | +18.76% | $6,998,759.40 |
| VELVET/USDT:USDT | +18.71% | $30,727,788.28 |
| SLX/USDT:USDT | +14.54% | $10,824,411.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGLD/USDT:USDT | below_1h_threshold | +3.84% | +3.77% |
| ARX/USDT:USDT | below_1h_threshold | +2.86% | +2.79% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.28% | +1.20% |
| BICO/USDT:USDT | below_1h_threshold | +1.06% | +0.99% |
| BEAT/USDT:USDT | below_1h_threshold | +1.05% | +0.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
