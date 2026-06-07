# Decision Report

- generated_at: 2026-06-07T13:34:48.144030+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5960**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5960, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/12 | 58.3% | +0.92% | **+0.54%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.38% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.34% | **+1.84%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.84% | **+1.71%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.58% | **+1.61%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.95% | **+1.33%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.94% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.65** / 初期 $100.00 (+47.65%)
- 確定: 1077件 (Win 263 / Loss 327 / Flat 487) / skip 1444件
- 成長率目線: 平均log +0.000362 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $147.65

## 4. Latest Market Context

- 更新: 2026-06-07T13:34:45.744634+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=61807.0
- Funnel: target 768 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SIREN/USDT:USDT | +60.25% | $19,134,364.77 |
| FIDA/USDT:USDT | +55.80% | $8,614,046.89 |
| BSB/USDT:USDT | +38.92% | $8,034,781.70 |
| LAB/USDT:USDT | +37.78% | $63,721,894.35 |
| EDEN/USDT:USDT | +34.65% | $5,405,614.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.58% | +2.69% |
| WLD/USDT:USDT | below_1h_threshold | +2.45% | +2.55% |
| BLESS/USDT:USDT | below_1h_threshold | +2.13% | +2.23% |
| VELVET/USDT:USDT | below_1h_threshold | +1.95% | +2.06% |
| GUN/USDT:USDT | below_1h_threshold | +1.62% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
