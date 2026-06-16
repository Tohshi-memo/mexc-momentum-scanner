# Decision Report

- generated_at: 2026-06-16T16:05:54.060976+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6872**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6872, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.96% | **+0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.19% | **+0.06%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| ASK | 20/20 | 100.0% | -0.22% | **-0.22%** |
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +3.85% | **+3.30%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.32% | **+0.92%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.15% | **+0.81%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.82% | **+0.66%** |
| ASK_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.97** / 初期 $100.00 (+84.97%)
- 確定: 1745件 (Win 459 / Loss 547 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $184.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 127件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0023 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T16:05:46.130073+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=65886.0
- Funnel: target 782 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +6.99% | $62,987,955.55 |
| BTW/USDT:USDT | +4.22% | $2,806,141.63 |
| BSB/USDT:USDT | +3.20% | $36,313,867.19 |
| SOXL/USDT:USDT | +3.00% | $2,815,595.15 |
| STG/USDT:USDT | +2.91% | $2,829,332.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.60% | +4.53% |
| BSB/USDT:USDT | below_1h_threshold | +3.13% | +3.06% |
| SOXL/USDT:USDT | below_1h_threshold | +3.00% | +2.94% |
| STG/USDT:USDT | below_1h_threshold | +2.92% | +2.85% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.44% | +2.37% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
