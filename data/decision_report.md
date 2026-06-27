# Decision Report

- generated_at: 2026-06-27T18:17:54.643007+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7712**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7712, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +5.04% | **+0.76%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.28% | **-0.11%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.04% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.43% | **+1.43%** |
| ASK_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.85% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.37** / 初期 $100.00 (+138.37%)
- 確定: 2221件 (Win 666 / Loss 740 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $238.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.42** / 初期 $100.00 (+7.42%)
- 確定: 443件 (Win 118 / Loss 113 / Flat 212) / skip 680件
- 成長率目線: 平均log +0.000162 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.42

## 5. Latest Market Context

- 更新: 2026-06-27T18:17:41.384679+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=60532.6
- Funnel: target 806 → liquid 126 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +31.85% | $13,460,631.14 |
| S/USDT:USDT | +10.02% | $1,504,197.43 |
| RE/USDT:USDT | +6.92% | $5,156,147.77 |
| ARX/USDT:USDT | +5.25% | $2,993,332.60 |
| BAS/USDT:USDT | +4.58% | $1,710,288.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +4.44% | +4.38% |
| BAS/USDT:USDT | below_1h_threshold | +1.79% | +1.72% |
| BTW/USDT:USDT | below_1h_threshold | +1.49% | +1.43% |
| RAVE/USDT:USDT | below_1h_threshold | +1.47% | +1.41% |
| PI/USDT:USDT | below_1h_threshold | +1.37% | +1.31% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
