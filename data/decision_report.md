# Decision Report

- generated_at: 2026-06-13T20:45:22.349005+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6610**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6610, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.79% | **+0.99%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.97% | **+0.98%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.26% | **+0.82%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.31** / 初期 $100.00 (+67.31%)
- 確定: 1483件 (Win 399 / Loss 473 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $167.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.06** / 初期 $100.00 (-0.94%)
- 確定: 21件 (Win 6 / Loss 9 / Flat 6) / skip 0件
- 成長率目線: 平均log -0.000450 / 幾何平均 -0.045% per trade / maxDD +1.59%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0190 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $99.06

## 5. Latest Market Context

- 更新: 2026-06-13T20:45:18.394499+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=64205.0
- Funnel: target 770 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +18.75% | $8,828,054.89 |
| MEGA/USDT:USDT | +8.38% | $2,035,752.43 |
| AT/USDT:USDT | +7.04% | $1,087,562.33 |
| VELVET/USDT:USDT | +6.47% | $63,622,281.12 |
| BTW/USDT:USDT | +6.27% | $1,754,029.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.78% | +3.86% |
| BEAT/USDT:USDT | below_1h_threshold | +3.25% | +3.34% |
| RIF/USDT:USDT | below_1h_threshold | +3.06% | +3.14% |
| BRETT/USDT:USDT | below_1h_threshold | +2.22% | +2.31% |
| MEGA/USDT:USDT | below_1h_threshold | +2.12% | +2.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
