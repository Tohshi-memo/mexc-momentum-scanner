# Decision Report

- generated_at: 2026-06-07T10:56:14.066038+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5948**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5948, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.17% | **+1.58%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.93% | **+1.45%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.97% | **+1.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.75% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$142.78** / 初期 $100.00 (+42.78%)
- 確定: 1065件 (Win 259 / Loss 325 / Flat 481) / skip 1444件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $142.78

## 4. Latest Market Context

- 更新: 2026-06-07T10:56:08.345877+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=62364.7
- Funnel: target 768 → liquid 123 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.4 >= 65=1, 4h RSI 88.3 >= 65=1, 4h RSI 74.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +56.13% | $7,337,891.53 |
| LAB/USDT:USDT | +39.89% | $63,319,741.68 |
| EDEN/USDT:USDT | +38.62% | $4,445,140.96 |
| BSB/USDT:USDT | +29.42% | $6,951,835.36 |
| BTW/USDT:USDT | +28.56% | $12,967,639.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.35% | +4.58% |
| UB/USDT:USDT | below_1h_threshold | +3.61% | +3.84% |
| BTW/USDT:USDT | below_1h_threshold | +3.42% | +3.65% |
| JTO/USDT:USDT | below_1h_threshold | +2.13% | +2.36% |
| BSB/USDT:USDT | below_1h_threshold | +2.11% | +2.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
