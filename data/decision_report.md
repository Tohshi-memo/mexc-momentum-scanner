# Decision Report

- generated_at: 2026-06-24T12:51:47.321905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7475**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7475, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.25** / 初期 $100.00 (+132.25%)
- 確定: 2106件 (Win 624 / Loss 698 / Flat 784) / skip 1930件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BAS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $232.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.34** / 初期 $100.00 (+7.34%)
- 確定: 338件 (Win 96 / Loss 91 / Flat 151) / skip 548件
- 成長率目線: 平均log +0.000210 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0375 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $107.34

## 5. Latest Market Context

- 更新: 2026-06-24T12:51:41.559287+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=62643.7
- Funnel: target 808 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +45.18% | $17,875,910.54 |
| SLX/USDT:USDT | +43.97% | $6,314,036.29 |
| BAS/USDT:USDT | +35.04% | $2,236,740.56 |
| O/USDT:USDT | +25.97% | $4,942,473.61 |
| ID/USDT:USDT | +16.23% | $1,760,422.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +3.83% | +4.22% |
| RAVE/USDT:USDT | below_1h_threshold | +1.82% | +2.21% |
| DEXE/USDT:USDT | below_1h_threshold | +1.67% | +2.06% |
| POPCAT/USDT:USDT | below_1h_threshold | +1.56% | +1.95% |
| CLO/USDT:USDT | below_1h_threshold | +1.46% | +1.85% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
