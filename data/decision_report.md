# Decision Report

- generated_at: 2026-06-27T01:41:13.115096+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7664**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7664, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.17% | **-1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 5/19 | 26.3% | +1.62% | **+0.43%** |
| LIMIT_1PCT | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.68% | **+1.47%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| MARKET_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.78** / 初期 $100.00 (+135.78%)
- 確定: 2189件 (Win 654 / Loss 728 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $235.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.83** / 初期 $100.00 (+7.83%)
- 確定: 395件 (Win 106 / Loss 100 / Flat 189) / skip 680件
- 成長率目線: 平均log +0.000191 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.83

## 5. Latest Market Context

- 更新: 2026-06-27T01:41:08.562209+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=59939.8
- Funnel: target 806 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +39.26% | $3,713,811.83 |
| SLX/USDT:USDT | +16.57% | $10,963,381.23 |
| VELVET/USDT:USDT | +16.35% | $29,941,874.34 |
| AGLD/USDT:USDT | +15.11% | $6,788,096.96 |
| MYX/USDT:USDT | +11.45% | $1,937,799.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.78% | +4.93% |
| MYX/USDT:USDT | below_1h_threshold | +4.09% | +4.25% |
| NES/USDT:USDT | below_1h_threshold | +1.90% | +2.06% |
| JTO/USDT:USDT | below_1h_threshold | +1.89% | +2.05% |
| BEAT/USDT:USDT | below_1h_threshold | +1.70% | +1.86% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
