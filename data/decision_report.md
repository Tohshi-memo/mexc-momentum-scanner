# Decision Report

- generated_at: 2026-06-17T23:59:31.899141+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6978**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6978, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.81% | **+0.68%** |
| ASK | 20/20 | 100.0% | +0.17% | **+0.17%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.23% | **+0.16%** |
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.23% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.07% | **+0.70%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.63% | **+0.35%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.16% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$199.68** / 初期 $100.00 (+99.68%)
- 確定: 1825件 (Win 498 / Loss 576 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $199.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.86** / 初期 $100.00 (+2.86%)
- 確定: 251件 (Win 66 / Loss 65 / Flat 120) / skip 138件
- 成長率目線: 平均log +0.000113 / 幾何平均 +0.011% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0548 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $102.86

## 5. Latest Market Context

- 更新: 2026-06-17T23:59:20.712781+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=64447.7
- Funnel: target 790 → liquid 175 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +96.88% | $21,338,614.29 |
| O/USDT:USDT | +82.32% | $1,452,647.88 |
| SYN/USDT:USDT | +44.99% | $4,212,253.35 |
| RE/USDT:USDT | +16.71% | $1,828,817.05 |
| MITO/USDT:USDT | +15.01% | $1,663,614.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +3.56% | +3.28% |
| RAVE/USDT:USDT | below_1h_threshold | +3.33% | +3.05% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.81% | +2.53% |
| UP/USDT:USDT | below_1h_threshold | +2.57% | +2.29% |
| ENA/USDT:USDT | below_1h_threshold | +2.42% | +2.13% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
