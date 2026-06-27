# Decision Report

- generated_at: 2026-06-27T01:16:00.175011+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7663**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7663, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 5/18 | 27.8% | +1.62% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.83% | **+1.27%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.50% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$234.61** / 初期 $100.00 (+134.61%)
- 確定: 2188件 (Win 653 / Loss 728 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $234.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.83** / 初期 $100.00 (+7.83%)
- 確定: 394件 (Win 106 / Loss 100 / Flat 188) / skip 680件
- 成長率目線: 平均log +0.000191 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0375 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGLD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.83

## 5. Latest Market Context

- 更新: 2026-06-27T01:15:55.258434+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=59954.9
- Funnel: target 806 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +42.07% | $3,325,592.83 |
| AGLD/USDT:USDT | +19.40% | $6,579,977.24 |
| SLX/USDT:USDT | +14.24% | $10,720,773.31 |
| VELVET/USDT:USDT | +12.30% | $29,006,233.05 |
| NES/USDT:USDT | +11.73% | $2,201,850.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NES/USDT:USDT | below_1h_threshold | +2.62% | +2.75% |
| BEAT/USDT:USDT | below_1h_threshold | +1.70% | +1.83% |
| VELVET/USDT:USDT | below_1h_threshold | +1.25% | +1.39% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.97% | +1.10% |
| LAB/USDT:USDT | below_1h_threshold | +0.84% | +0.97% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
