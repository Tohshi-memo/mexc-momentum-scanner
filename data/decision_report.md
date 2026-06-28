# Decision Report

- generated_at: 2026-06-28T02:20:41.072994+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7725**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7725, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.46% | **+1.09%** |
| LIMIT_BB3S | 3/15 | 20.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_6PCT | 6/20 | 30.0% | -1.05% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |
| ASK_LONG | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.35% | **+0.14%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$241.93** / 初期 $100.00 (+141.93%)
- 確定: 2233件 (Win 673 / Loss 745 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $241.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.83** / 初期 $100.00 (+6.83%)
- 確定: 454件 (Win 120 / Loss 118 / Flat 216) / skip 682件
- 成長率目線: 平均log +0.000145 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0059 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.83

## 5. Latest Market Context

- 更新: 2026-06-28T02:20:36.446154+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=60218.2
- Funnel: target 806 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAS/USDT:USDT | +22.43% | $2,770,175.47 |
| LAB/USDT:USDT | +11.69% | $40,981,460.53 |
| VELVET/USDT:USDT | +9.76% | $263,203,556.08 |
| SLX/USDT:USDT | +9.63% | $18,168,527.92 |
| S/USDT:USDT | +9.34% | $4,778,693.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +2.00% | +1.96% |
| BEAT/USDT:USDT | below_1h_threshold | +1.79% | +1.75% |
| BAS/USDT:USDT | below_1h_threshold | +1.79% | +1.75% |
| RE/USDT:USDT | below_1h_threshold | +1.44% | +1.40% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.39% | +1.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
