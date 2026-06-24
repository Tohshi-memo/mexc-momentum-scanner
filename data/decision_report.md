# Decision Report

- generated_at: 2026-06-24T11:12:54.214354+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7473**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7473, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| ASK | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.39% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.96** / 初期 $100.00 (+131.96%)
- 確定: 2104件 (Win 623 / Loss 697 / Flat 784) / skip 1930件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $231.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.26** / 初期 $100.00 (+7.26%)
- 確定: 336件 (Win 95 / Loss 90 / Flat 151) / skip 548件
- 成長率目線: 平均log +0.000209 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0327 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: O/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $107.26

## 5. Latest Market Context

- 更新: 2026-06-24T11:12:49.712315+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=62367.3
- Funnel: target 808 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +49.60% | $16,610,555.67 |
| SLX/USDT:USDT | +42.06% | $4,233,285.16 |
| O/USDT:USDT | +30.92% | $2,211,787.80 |
| SAHARA/USDT:USDT | +20.75% | $2,703,096.11 |
| ID/USDT:USDT | +19.61% | $1,648,702.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +1.54% | +1.62% |
| INX/USDT:USDT | below_1h_threshold | +0.86% | +0.94% |
| SYN/USDT:USDT | below_1h_threshold | +0.84% | +0.92% |
| LIGHT/USDT:USDT | below_1h_threshold | +0.63% | +0.71% |
| DEXE/USDT:USDT | below_1h_threshold | +0.52% | +0.60% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
