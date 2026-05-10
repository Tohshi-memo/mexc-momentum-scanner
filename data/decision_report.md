# Decision Report

- generated_at: 2026-05-10T18:43:01.971246+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3981**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3981, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.45% | **-1.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.94% | **+0.09%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.17% | **+0.08%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.07% | **+0.04%** |
| LIMIT_BB3S | 4/14 | 28.6% | -0.80% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.90% | **+1.52%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.12% | **+1.38%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.43% | **+0.97%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.92% | **+0.86%** |
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 344件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T18:42:58.848041+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=81225.1
- Funnel: target 769 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALCH/USDT:USDT | +20.49% | $2,006,784.72 |
| B/USDT:USDT | +14.17% | $1,811,507.38 |
| DEEP/USDT:USDT | +13.96% | $1,587,710.98 |
| TRUTH/USDT:USDT | +12.41% | $2,231,559.17 |
| SUI/USDT:USDT | +12.00% | $539,052,277.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000BONK/USDT:USDT | below_1h_threshold | +4.65% | +4.92% |
| DEEP/USDT:USDT | below_1h_threshold | +3.93% | +4.20% |
| TRUTH/USDT:USDT | below_1h_threshold | +3.82% | +4.09% |
| SAHARA/USDT:USDT | below_1h_threshold | +3.68% | +3.94% |
| SEI/USDT:USDT | below_1h_threshold | +3.61% | +3.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
