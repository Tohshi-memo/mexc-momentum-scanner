# Decision Report

- generated_at: 2026-06-27T17:24:04.476839+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7707**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7707, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_BB3S | 3/14 | 21.4% | +2.17% | **+0.46%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.21% | **+0.10%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.55% | **+0.08%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.19% | **+0.83%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.53% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$234.85** / 初期 $100.00 (+134.85%)
- 確定: 2218件 (Win 664 / Loss 739 / Flat 815) / skip 2050件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $234.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定: 438件 (Win 117 / Loss 111 / Flat 210) / skip 680件
- 成長率目線: 平均log +0.000164 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0480 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.44

## 5. Latest Market Context

- 更新: 2026-06-27T17:23:56.259463+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=60563.4
- Funnel: target 806 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +6.34% | $3,140,820.91 |
| LAB/USDT:USDT | +5.67% | $40,429,022.64 |
| MAGMA/USDT:USDT | +3.46% | $7,616,272.99 |
| ALLO/USDT:USDT | +2.57% | $15,676,707.63 |
| RIVER/USDT:USDT | +1.54% | $1,925,176.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +0.60% | +0.96% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +0.24% | +0.61% |
| PI/USDT:USDT | below_1h_threshold | +0.23% | +0.60% |
| RIVER/USDT:USDT | below_1h_threshold | +0.18% | +0.55% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.10% | +0.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
