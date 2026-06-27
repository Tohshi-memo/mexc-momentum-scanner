# Decision Report

- generated_at: 2026-06-27T17:14:36.284842+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7706**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7706, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +5.45% | **+0.82%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.84% | **+0.42%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_BB3S | 4/14 | 28.6% | +0.63% | **+0.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.59% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.19% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| ASK_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$233.68** / 初期 $100.00 (+133.68%)
- 確定: 2217件 (Win 663 / Loss 739 / Flat 815) / skip 2050件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $233.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定: 437件 (Win 117 / Loss 111 / Flat 209) / skip 680件
- 成長率目線: 平均log +0.000164 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0423 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.44

## 5. Latest Market Context

- 更新: 2026-06-27T17:14:28.409186+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=60546.1
- Funnel: target 806 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +12.99% | $2,520,988.91 |
| ALLO/USDT:USDT | +4.18% | $15,464,291.37 |
| LAB/USDT:USDT | +2.98% | $40,027,652.42 |
| BAS/USDT:USDT | +0.97% | $1,698,271.07 |
| RIVER/USDT:USDT | +0.87% | $1,914,858.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.63% | +4.03% |
| H/USDT:USDT | below_1h_threshold | +0.92% | +1.32% |
| PORTAL/USDT:USDT | below_1h_threshold | +0.91% | +1.30% |
| SPX500/USDT:USDT | below_1h_threshold | +0.03% | +0.42% |
| ASTER/USDT:USDT | below_1h_threshold | +0.02% | +0.41% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
