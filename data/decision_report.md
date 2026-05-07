# Decision Report

- generated_at: 2026-05-07T12:42:38.250490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3626**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=3626, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.23% | **+0.86%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.45% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.84% | **+1.73%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.31% | **+1.27%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.08** / 初期 $100.00 (+6.08%)
- 確定: 120件 (Win 37 / Loss 48 / Flat 35) / skip 67件
- 成長率目線: 平均log +0.000492 / 幾何平均 +0.049% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.42% 残高後 $106.08

## 4. Latest Market Context

- 更新: 2026-05-07T12:42:35.066462+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=80985.6
- Funnel: target 771 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +98.96% | $11,970,704.81 |
| SATO/USDT:USDT | +92.34% | $2,625,197.84 |
| PENGUIN/USDT:USDT | +72.56% | $3,851,306.03 |
| DOGS/USDT:USDT | +52.57% | $16,624,997.71 |
| NIL/USDT:USDT | +34.67% | $3,311,818.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_relative_strength | +5.08% | +4.88% |
| BILL/USDT:USDT | below_1h_threshold | +3.63% | +3.43% |
| POPCAT/USDT:USDT | below_1h_threshold | +3.48% | +3.28% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +3.41% | +3.22% |
| BRETT/USDT:USDT | below_1h_threshold | +3.16% | +2.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
