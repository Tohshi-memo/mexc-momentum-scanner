# Decision Report

- generated_at: 2026-06-16T15:52:36.507491+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6870**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6870, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.96% | **+0.29%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.03% | **+0.01%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| ASK | 20/20 | 100.0% | -0.22% | **-0.22%** |
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +3.45% | **+2.87%** |
| ASK_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.86% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.52% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.98** / 初期 $100.00 (+84.98%)
- 確定: 1743件 (Win 458 / Loss 546 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AERO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $184.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 125件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0243 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T15:52:32.114295+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=65866.4
- Funnel: target 782 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +47.30% | $37,383,866.15 |
| BR/USDT:USDT | +46.06% | $5,499,296.27 |
| PORTAL/USDT:USDT | +34.58% | $4,578,376.42 |
| LAB/USDT:USDT | +32.32% | $18,731,147.00 |
| SKYAI/USDT:USDT | +21.48% | $9,337,474.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.74% | +4.38% |
| HOME/USDT:USDT | below_1h_threshold | +3.63% | +3.27% |
| LAB/USDT:USDT | below_1h_threshold | +3.46% | +3.10% |
| GUA/USDT:USDT | below_1h_threshold | +2.85% | +2.49% |
| STG/USDT:USDT | below_1h_threshold | +2.78% | +2.42% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
