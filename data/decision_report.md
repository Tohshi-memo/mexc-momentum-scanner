# Decision Report

- generated_at: 2026-05-07T03:32:42.668994+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3548**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3548, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +3.43% | **+1.03%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_7PCT | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.28% | **+0.58%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.32% | **+2.16%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.61% | **+1.44%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$102.76** / 初期 $100.00 (+2.76%)
- 確定: 43件 (Win 13 / Loss 16 / Flat 14) / skip 66件
- 成長率目線: 平均log +0.000633 / 幾何平均 +0.063% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $102.76

## 4. Latest Market Context

- 更新: 2026-05-07T03:32:39.396648+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=80906.4
- Funnel: target 770 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1, 4h RSI 81.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +303.21% | $1,339,758.67 |
| DOGS/USDT:USDT | +83.42% | $9,299,700.47 |
| FHE/USDT:USDT | +34.22% | $16,327,801.94 |
| PENGUIN/USDT:USDT | +29.55% | $1,184,997.57 |
| TONCOIN/USDT:USDT | +18.43% | $262,782,787.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +3.07% | +3.28% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.66% | +2.87% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.51% | +1.72% |
| BLESS/USDT:USDT | below_1h_threshold | +1.07% | +1.28% |
| UB/USDT:USDT | below_1h_threshold | +1.04% | +1.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
