# Decision Report

- generated_at: 2026-06-07T09:55:28.398854+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5942**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5942, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/19 | 47.4% | +2.34% | **+1.11%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.74% | **+1.39%** |
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.82% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.31% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$143.00** / 初期 $100.00 (+43.00%)
- 確定: 1059件 (Win 258 / Loss 324 / Flat 477) / skip 1444件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LUNC/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $143.00

## 4. Latest Market Context

- 更新: 2026-06-07T09:55:22.742879+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.45% price=62541.0
- Funnel: target 771 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +56.19% | $6,869,378.50 |
| LAB/USDT:USDT | +40.69% | $63,938,451.78 |
| EDEN/USDT:USDT | +39.17% | $3,611,390.54 |
| B/USDT:USDT | +27.43% | $2,016,743.45 |
| BSB/USDT:USDT | +26.59% | $6,727,676.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.72% | +4.17% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +3.50% | +3.95% |
| BEAT/USDT:USDT | below_1h_threshold | +2.51% | +2.96% |
| LAB/USDT:USDT | below_1h_threshold | +1.99% | +2.44% |
| SIREN/USDT:USDT | below_1h_threshold | +1.09% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
