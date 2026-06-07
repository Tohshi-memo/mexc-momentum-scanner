# Decision Report

- generated_at: 2026-06-07T11:24:49.097545+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5951**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5951, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.59% | **+2.59%** |
| ASK_LONG | 20/20 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.14% | **+1.39%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.89% | **+0.95%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.06% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$142.42** / 初期 $100.00 (+42.42%)
- 確定: 1068件 (Win 259 / Loss 326 / Flat 483) / skip 1444件
- 成長率目線: 平均log +0.000331 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $142.42

## 4. Latest Market Context

- 更新: 2026-06-07T11:24:46.003729+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=62498.2
- Funnel: target 768 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +55.24% | $7,488,910.46 |
| SIREN/USDT:USDT | +47.01% | $8,634,749.16 |
| LAB/USDT:USDT | +43.10% | $62,712,522.88 |
| EDEN/USDT:USDT | +37.34% | $4,639,304.07 |
| BSB/USDT:USDT | +31.04% | $6,808,214.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.52% | +3.27% |
| BTW/USDT:USDT | below_1h_threshold | +3.43% | +3.19% |
| ZEST/USDT:USDT | below_1h_threshold | +3.30% | +3.05% |
| LAB/USDT:USDT | below_1h_threshold | +2.53% | +2.28% |
| H/USDT:USDT | below_1h_threshold | +1.94% | +1.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
