# Decision Report

- generated_at: 2026-04-30T16:57:46.492457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2719**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2719, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.61% | **+0.46%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.85% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +5.89% | **+2.95%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.98% | **+2.19%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.84% | **+1.42%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.00% | **+1.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T16:57:41.864339+00:00 / 保存件数 50/288
- BTC: BULLISH 1h -0.30% price=76197.3
- Funnel: target 761 → liquid 229 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +9.37% | $4,203,222.05 |
| ASTEROID/USDT:USDT | +8.39% | $3,649,146.73 |
| BIO/USDT:USDT | +4.21% | $3,649,931.36 |
| AIOT/USDT:USDT | +3.64% | $12,823,787.03 |
| ZEREBRO/USDT:USDT | +2.97% | $3,602,508.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +4.19% | +4.49% |
| AIOT/USDT:USDT | below_1h_threshold | +3.66% | +3.96% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.97% | +3.27% |
| ENSO/USDT:USDT | below_1h_threshold | +2.60% | +2.90% |
| ZBT/USDT:USDT | below_1h_threshold | +2.42% | +2.73% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
