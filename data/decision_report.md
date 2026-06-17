# Decision Report

- generated_at: 2026-06-17T19:39:28.356316+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6962**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6962, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/17 | 35.3% | +2.12% | **+0.75%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.62% | **+0.25%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.81% | **+4.81%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.37% | **+0.26%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.17% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1816件 (Win 496 / Loss 573 / Flat 747) / skip 1707件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NBISSTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.59% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.20** / 初期 $100.00 (+3.20%)
- 確定: 235件 (Win 62 / Loss 57 / Flat 116) / skip 138件
- 成長率目線: 平均log +0.000134 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0779 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $103.20

## 5. Latest Market Context

- 更新: 2026-06-17T19:39:20.786184+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.79% price=64308.0
- Funnel: target 790 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +79.31% | $1,009,885.80 |
| SYN/USDT:USDT | +32.83% | $1,035,172.58 |
| RE/USDT:USDT | +14.59% | $1,611,000.84 |
| MITO/USDT:USDT | +13.02% | $1,365,930.80 |
| ESPORTS/USDT:USDT | +7.59% | $14,828,868.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.93% | +3.72% |
| UP/USDT:USDT | below_1h_threshold | +1.38% | +3.18% |
| TAC/USDT:USDT | below_1h_threshold | +0.82% | +2.62% |
| AGT/USDT:USDT | below_1h_threshold | +0.68% | +2.47% |
| GUA/USDT:USDT | below_1h_threshold | +0.45% | +2.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
