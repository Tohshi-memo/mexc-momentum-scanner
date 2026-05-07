# Decision Report

- generated_at: 2026-05-07T14:57:45.743286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3645**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.53% / filled 20/20。**
- 全期間 MARKET基準: n=3645, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +4.32% | **+1.95%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.06% | **+1.68%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.27% | **+1.48%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.68% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.50** / 初期 $100.00 (+10.50%)
- 確定: 139件 (Win 44 / Loss 52 / Flat 43) / skip 67件
- 成長率目線: 平均log +0.000718 / 幾何平均 +0.072% per trade / maxDD +2.62%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $110.50

## 4. Latest Market Context

- 更新: 2026-05-07T14:57:42.724244+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=80158.7
- Funnel: target 771 → liquid 187 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.5 >= 65=1, 4h RSI 92.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +92.41% | $11,003,705.90 |
| PENGUIN/USDT:USDT | +82.68% | $4,348,861.37 |
| SATO/USDT:USDT | +62.63% | $3,743,839.64 |
| NIL/USDT:USDT | +49.68% | $4,948,415.25 |
| DOGS/USDT:USDT | +47.53% | $17,821,307.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QCOMSTOCK/USDT:USDT | below_1h_threshold | +4.22% | +4.60% |
| NGAS/USDT:USDT | below_1h_threshold | +4.04% | +4.41% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +3.71% | +4.08% |
| JTO/USDT:USDT | below_1h_threshold | +3.66% | +4.04% |
| BLESS/USDT:USDT | below_1h_threshold | +3.07% | +3.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
