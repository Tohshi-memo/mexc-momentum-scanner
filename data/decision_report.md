# Decision Report

- generated_at: 2026-06-16T15:59:14.176614+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6871**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6871, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.05% | **-0.02%** |
| ASK | 20/20 | 100.0% | -0.22% | **-0.22%** |
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +3.85% | **+3.30%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.76% | **+0.49%** |
| ASK_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.54% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.05** / 初期 $100.00 (+84.05%)
- 確定: 1744件 (Win 458 / Loss 547 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000350 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $184.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 126件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0107 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T15:59:08.835410+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=65865.8
- Funnel: target 782 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +48.53% | $37,692,767.38 |
| BR/USDT:USDT | +46.33% | $5,590,747.66 |
| LAB/USDT:USDT | +34.49% | $19,239,153.03 |
| PORTAL/USDT:USDT | +33.36% | $4,635,037.77 |
| GUA/USDT:USDT | +23.89% | $1,046,423.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_relative_strength | +5.34% | +4.98% |
| LAB/USDT:USDT | below_1h_threshold | +4.88% | +4.53% |
| VELVET/USDT:USDT | below_1h_threshold | +4.39% | +4.03% |
| HOME/USDT:USDT | below_1h_threshold | +3.78% | +3.42% |
| STG/USDT:USDT | below_1h_threshold | +2.62% | +2.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
