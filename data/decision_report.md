# Decision Report

- generated_at: 2026-06-10T20:16:49.490323+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6258**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6258, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.66% | **-0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.77% | **+0.27%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| ASK | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.31% | **+0.65%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.44% | **+0.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.73** / 初期 $100.00 (+49.73%)
- 確定: 1244件 (Win 309 / Loss 387 / Flat 548) / skip 1575件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $149.73

## 4. Latest Market Context

- 更新: 2026-06-10T20:16:43.511837+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=61785.5
- Funnel: target 785 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1, 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +55.93% | $24,948,196.12 |
| BEAT/USDT:USDT | +25.29% | $127,851,814.43 |
| JCT/USDT:USDT | +11.20% | $2,168,418.53 |
| STRAX/USDT:USDT | +9.68% | $1,199,926.65 |
| LAB/USDT:USDT | +6.03% | $22,385,480.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +3.67% | +3.87% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.94% | +3.14% |
| VELVET/USDT:USDT | below_1h_threshold | +2.52% | +2.72% |
| TXNSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.85% |
| JCT/USDT:USDT | below_1h_threshold | +1.60% | +1.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
